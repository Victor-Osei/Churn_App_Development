# import streamlit as st 

# def home():
#     # Set the title with a larger font and center alignment
#     st.markdown("<h1 style='text-align: center; color: #2c3e50;'>Customer Churn Prediction App</h1>", unsafe_allow_html=True)
    
#     # Add a subtitle
#     st.markdown("<h3 style='text-align: center; color: #2c3e50;'>Victor Osei Duah</h3>", unsafe_allow_html=True)
    
#     # Add a nice visual (banner image or illustration)
#     st.image("Reducing Customer Churn Rate.webp", use_column_width=True, caption="Predicting customer churn to retain valuable customers.")

#     # Provide a brief introduction or description of the app
#     st.write("""
#     Welcome to the Customer Churn Prediction App! This application helps you analyze customer behavior and predict churn using advanced machine learning algorithms. 
#     Navigate through the app using the sidebar to view data, explore the dashboard, or make predictions.
#     """)

# # Display the home page
# home()


import streamlit as st
import hashlib
import json
import os

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to load user data
def load_user_data():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return json.load(f)
    return {"users": []}

# Function to save user data
def save_user_data(user_data):
    with open('users.json', 'w') as f:
        json.dump(user_data, f)

# Function to create a new user
def create_user(username, password):
    user_data = load_user_data()
    for user in user_data["users"]:
        if user["username"] == username:
            st.warning("Username already exists.")
            return False
    hashed_password = hash_password(password)
    user_data["users"].append({"username": username, "password": hashed_password})
    save_user_data(user_data)
    st.success("Account created successfully.")
    return True

# Function to authenticate user
def authenticate_user(username, password):
    user_data = load_user_data()
    hashed_password = hash_password(password)
    for user in user_data["users"]:
        if user["username"] == username and user["password"] == hashed_password:
            return True
    return False

# Main application
def main():
    st.title("Authentication")

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the app!")
    elif choice == "Login":
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_user(username, password):
                st.success(f"Welcome {username}")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
            else:
                st.error("Invalid credentials")

        if "logged_in" in st.session_state and st.session_state["logged_in"]:
            if st.button("Logout"):
                st.session_state["logged_in"] = False
                st.session_state["username"] = None
                st.success("You have logged out.")

    elif choice == "SignUp":
        st.subheader("Create Account")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("SignUp"):
            create_user(new_user, new_password)

    # Access control: Restrict access to authenticated users only
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        st.write(f"Hello, {st.session_state['username']}! You are logged in.")
    else:
        st.warning("Please log in to access this page.")

if __name__ == '__main__':
    main()




