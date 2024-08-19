import streamlit as st 
import webbrowser 

st.set_page_config(
    page_title="Home Page",
    page_icon="🏡",
    layout="wide"
)
# Main Content
st.title("Customer Churn Prediction")
st.markdown("""
            This application leverages machine learning models to predict customer churn. It helps businesses identify potential churn risks and take proactive measures to retain valuable customers.
            """)


# Key Features
st.subheader("Key Features")
st.markdown("""
- **Data Integration**: Connect to SQL Server to fetch and analyze customer data.
- **Feature Selection**: Choose relevant features for classification.
- **Model Performance Report**: Access a detailed report on model performance.
- **Interactive Charts**: Visualize feature importance and churn probabilities with interactive charts.
""")


# App features
st.subheader("App Features")
st.markdown("""        

""")


# How to run the app
st.subheader("How to run Churn App")
st.code(""" 
        # activate virtual environment
        venv/Scripts/activate
        streamlit run app.py 

        OR

        # activate virtual environment
        venv/Scripts/activate
        python -m streamlit run app.py

        """, language= 'python')



# Machine Learning Integration
st.subheader("Machine Learning Integration")
st.markdown("""
3. **Model Selection**: Choice of machine learning model
   **Prediction**: Individual customer prediction
   **Seamless Integration**: Integrate predictions into your workflow
   **Insights and Visualization**: Interactive charts and graphs 
""")


# Contact and Github Repository
st.subheader("Contact and GitHub Repository")
st.markdown("For collaboration, contact Victor")

# Email contact
st.markdown("📧 Email: victor.duah@azubiafrica.org")

# Linkedin
linkedin = "https://www.linkedin.com/in/victor-osei-duah-a9182a13a/"

if st.button("To Linkedin"):
    webbrowser.open_new_tab(linkedin)

# GitHub repository
github_repo = "https://github.com/Victor-Osei/Churn_App_Development"

if st.button("View Repository on GitHub"):
    webbrowser.open_new_tab(github_repo)

# ... (rest of your code)
# st.subheader("Ask for Help")
# st.markdown("For collaboration contact Team Fiji")
# st.button("Repository on Github")
