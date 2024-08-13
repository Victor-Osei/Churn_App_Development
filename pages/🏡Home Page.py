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
            This app uses machine learning model to predict whether a customer will churn or not
            """)


# Key Features
st.subheader("Key Features")
st.markdown("""
- Read data from SQL Server
- Select the features for classification
- From the dropdown choose a machine learning model of your choice
- This app also provide a comprehensive report on the performance of the model
- Metrics like accuracy score, precision, recall and f1-score are included in the report 
- The app provides interactive charts for feature importance and churn probability
""")


# App features
st.subheader("App Features")
st.markdown("""
1. **View Data**: Access proprietary data
            
2. **Dashboard**: Explore interactive visuals for insights
            
3. **Prediction Page**: Shows the result using the machine learning model of whether a customer churned or not
""")


# How to run the app
st.subheader("How to run Churn App")
st.code(""" 
        # activate virtual environment
        venv/Scripts/activate
        streamlit run app.py
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
st.markdown("For collaboration, contact Me")

# Email contact
st.markdown("📧 Email: victor.duah@azubiafrica.org")

# GitHub repository
github_repo = "https://github.com/Victor-Osei/Churn_App_Development"

if st.button("View Repository on GitHub"):
    webbrowser.open_new_tab(github_repo)

# ... (rest of your code)
# st.subheader("Ask for Help")
# st.markdown("For collaboration contact Team Fiji")
# st.button("Repository on Github")
