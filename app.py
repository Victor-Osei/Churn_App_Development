import streamlit as st 

def home():
    # Set the title with a larger font and center alignment
    st.markdown("<h1 style='text-align: center; color: #2c3e50;'>Customer Churn Prediction App</h1>", unsafe_allow_html=True)
    
    # Add a subtitle
    st.markdown("<h3 style='text-align: center; color: #2c3e50;'>Victor Osei Duah</h3>", unsafe_allow_html=True)
    
    # Add a nice visual (banner image or illustration)
    st.image("Reducing Customer Churn Rate.webp", use_column_width=True, caption="Predicting customer churn to retain valuable customers.")

    # Provide a brief introduction or description of the app
    st.write("""
    Welcome to the Customer Churn Prediction App! This application helps you analyze customer behavior and predict churn using advanced machine learning algorithms. 
    Navigate through the app using the sidebar to view data, explore the dashboard, or make predictions.
    """)

# Display the home page
home()




    



