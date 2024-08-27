import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊", 
    layout="wide",
)

# Load the CSV file from the repo
file_path = 'main_df.csv' 
main_df = pd.read_csv(file_path)

# Title and Introduction
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("""
    ## Welcome to the Customer Churn Prediction Dashboard

    This dashboard provides insightful visualizations and detailed metrics to help you understand and predict customer churn. 
    Here, you can explore key performance indicators, analyze the impact of various factors on churn, and gain actionable insights from the data.
    
    ### What You Can Do:
    - **View KPIs:** Get an overview of the key performance indicators related to churn.
    - **Explore Data:** Analyze the distribution of factors contributing to customer churn.
    - **Compare Metrics:** Assess model performance through precision, recall, and F1-score metrics.

    Use the tabs to navigate through the different sections of the dashboard.
""")


# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["EDA Dashboard", "Analytics Dashboard"])

if options == "EDA Dashboard":
    st.header("🔍 EDA Dashboard")

    # Visualization: Types of Contracts
    if 'Contract' in main_df.columns:
        st.markdown("### Types of Contracts")
        value_counts = main_df['Contract'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        value_counts.plot(kind='barh', color='skyblue', ax=ax)
        ax.set_title('Types of Contracts')
        st.pyplot(fig)
        plt.close(fig)  # Close the figure


    # Create histogram plot of Monthly Charges using seaborn
    if 'Monthly_Charges' in main_df.columns:
        st.markdown("### Distribution of Monthly Charges")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(data=main_df['Monthly_Charges'], kde=True, ax=ax)
        ax.set_title('Distribution of Monthly Charges')
        st.pyplot(fig)
        plt.close(fig)  # Close the figure
    else:
        st.info("No 'Monthly_Charges' column in the dataset.")

    # Create histogram plot of Total Charges using seaborn
    if 'Total_Charges' in main_df.columns:
        st.markdown("### Distribution of Total Charges")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(data=main_df['Total_Charges'], kde=True, ax=ax)
        ax.set_title('Distribution of Total Charges')
        st.pyplot(fig)
        plt.close(fig)  # Close the figure
    else:
        st.info("No 'Total_Charges' column in the dataset.")

    # Count and create pie chart of the 'SeniorCitizen' column
    if 'Senior_Citizen' in main_df.columns:
        st.markdown("### Distribution of Senior Citizens")
        senior_citizen_counts = main_df['Senior_Citizen'].value_counts()
        labels = ['Non-Senior Citizen', 'Senior Citizen']
        counts = [senior_citizen_counts.get(0, 0), senior_citizen_counts.get(1, 0)]
        colors = ['#009ACD', '#ADD8E6']
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(counts, labels=labels, colors=colors, autopct='%1.0f%%', shadow=False)
        ax.axis('equal')
        ax.set_title('Distribution of Senior Citizens')
        st.pyplot(fig)
        plt.close(fig)  # Close the figure
    else:
        st.info("No 'Senior_Citizen' column in the dataset.")

    # Visualization: Gender Distribution
    if 'Gender' in main_df.columns:
        st.markdown("### Distribution of Gender")
        value_counts = main_df['Gender'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        value_counts.plot(kind='bar', color='red', ax=ax)
        ax.set_title('Distribution of Gender')
        st.pyplot(fig)
        plt.close(fig)  # Close the figure
    else:
        st.info("No 'Gender' column in the dataset.")

    # Calculate churn rates by payment method
    if 'Churn' in main_df.columns and 'Payment_Method' in main_df.columns:
        st.markdown("### Churn Rate by Payment Method")
        churn_counts = main_df.groupby('Payment_Method')['Churn'].value_counts(normalize=True).unstack()
        fig, ax = plt.subplots(figsize=(10, 6))
        churn_counts.plot(kind='bar', stacked=True, color=['green', 'red'], ax=ax)
        ax.set_title('Churn Rate by Payment Method')
        ax.set_xlabel('Payment Method')
        ax.set_ylabel('Churn Rate')
        ax.legend(title='Churn')
        st.pyplot(fig)
        plt.close(fig)  # Close the figure
    else:
        st.info("No 'Churn' or 'Payment_Method' column in the dataset.")


    # Multivariate analysis of Partner, Tenure, Monthly Charges, and Churn
    if all(col in main_df.columns for col in ['Partner', 'Churn', 'Tenure_Months', 'Monthly_Charges']):
        st.markdown("### Multivariate Analysis: Partner, Tenure, Monthly Charges and Churn")
        multivariate_df = main_df.groupby(['Partner', 'Churn']).agg({'Tenure_Months': 'mean', 'Monthly_Charges': 'mean'}).reset_index()
        fig, ax = plt.subplots(figsize=(12, 8))

        # Tenure vs Churn
        plt.subplot(2, 1, 1)
        sns.barplot(data=multivariate_df, x='Partner', y='Tenure_Months', hue='Churn', palette='pastel')
        plt.title('Tenure vs Churn by Partner Status')
        plt.xlabel('Partner Status')
        plt.ylabel('Average Tenure')

        # Monthly Charges vs Churn
        plt.subplot(2, 1, 2)
        sns.barplot(data=multivariate_df, x='Partner', y='Monthly_Charges', hue='Churn', palette='pastel')
        plt.title('Monthly Charges vs Churn by Partner Status')
        plt.xlabel('Partner Status')
        plt.ylabel('Average Monthly Charges')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)  
    else:
        st.info("One or more columns for multivariate analysis are missing.")

    # Grouping by tenure and calculating the mean Total Charges
    if 'Tenure_Months' in main_df.columns and 'Total_Charges' in main_df.columns:
        st.markdown("### Mean Total Charges by Tenure")
        df_grp_tenure = main_df.groupby('Tenure_Months')['Total_Charges'].mean().reset_index()
        df_grp_tenure_15 = df_grp_tenure.head(15)
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.pointplot(data=df_grp_tenure_15, x='Tenure_Months', y='Total_Charges', color='steelblue', ax=ax)
        ax.set_title('Mean Total Charges by Tenure')
        ax.set_xlabel('Tenure')
        ax.set_ylabel('Mean Total Charges')
        st.pyplot(fig)
        plt.close(fig)  # Close the figure
    else:
        st.info("No 'Tenure_Months' or 'Total_Charges' column in the dataset.")


elif options == "Analytics Dashboard":
    st.header("📈 Comprehensive Analytics Dashboard")
    st.markdown("""
        ### Dive into the Analytics

        The Analytics Dashboard provides an in-depth view of customer churn predictions. Here, you'll find a comprehensive analysis of the model's performance, including key metrics and visualizations that highlight the effectiveness of the churn prediction model.

        #### What You'll Find:
        - **Key Performance Indicators:** Overview of accuracy, precision, recall, and F1-score.
        - **Detailed Metrics:** Breakdown of model performance across different classes.
        - **Visual Insights:** Graphical representations to help interpret the model's predictions and their implications.

        Use this dashboard to explore how well the model performs and to gain a deeper understanding of the factors influencing customer churn.
    """)


# Metrics and confusion matrix defined as variables from LP2
accuracy_score = 82.43
precision_no = 0.87
recall_no = 0.87
f1_no = 0.87
precision_yes = 0.74
recall_yes = 0.73
f1_yes = 0.73
conf_matrix = [[645, 95], [100, 270]]

# Function to display KPIs
def display_kpis():
    st.header('Model Performance KPIs')

    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Accuracy", f"{accuracy_score:.2f}%")
        st.metric("Precision (No)", f"{precision_no:.2f}")
        st.metric("Recall (No)", f"{recall_no:.2f}")
        st.metric("F1-Score (No)", f"{f1_no:.2f}")

    with col2:
        st.metric("Precision (Yes)", f"{precision_yes:.2f}")
        st.metric("Recall (Yes)", f"{recall_yes:.2f}")
        st.metric("F1-Score (Yes)", f"{f1_yes:.2f}")

# Function to display confusion matrix
def display_confusion_matrix():
    st.header('Confusion Matrix')
    cm_df = pd.DataFrame(conf_matrix, index=['No', 'Yes'], columns=['Predicted No', 'Predicted Yes'])
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues', ax=ax)
    st.pyplot(fig)

# Add the KPI and confusion matrix display to the page
def main():
    st.title('Analytics Dashboard')
    
    # Display KPIs
    display_kpis()
    
    # Display confusion matrix
    display_confusion_matrix()

if __name__ == "__main__":
    main()