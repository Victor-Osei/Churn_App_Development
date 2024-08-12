import streamlit as st
import pandas as pd
import pyodbc # type: ignore

#  create connection by inputting the credentials
def create_connection():
    """Create a connection to the SQL Server"""
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=dap-projects-database.database.windows.net;'
            'DATABASE=dapDB;'
            'UID=LP2_project;'
            'PWD=Stat$AndD@t@Rul3;'
        )
        return conn
    except pyodbc.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# load data from the server
def load_data(connection, query):
    """Load data from SQL Server using the provided query"""
    try:
        df = pd.read_sql(query, connection)
        return df
    except pyodbc.Error as e:
        st.error(f"Error executing query: {e}")
        return None

def main():
    st.title("👁️ Welcome to the Data page")
    st.write("Here you can view the data from our SQL Server database.")

    # Create connection
    conn = create_connection()
    if conn is not None:
        # Query the data
        query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
        df = load_data(conn, query)

        if df is not None:
            # Display data
            st.subheader("Data Preview")
            st.write(df.head())

            # Display full dataset in an expandable section
            with st.expander("View Full Dataset"):
                st.write(df)

            # Basic data info
            st.subheader("Data Information")
            st.write(f"Total rows: {df.shape[0]}")
            st.write(f"Total columns: {df.shape[1]}")

            # Example charts
            # st.subheader("Data Visualization")
            
            # # Assuming 'TotalCharges' is a numeric column in your dataset
            # if 'TotalCharges' in df.columns:
            #     st.line_chart(df['TotalCharges'])
            #     st.caption("Line chart of Total Charges")

            
        # Close the connection
    conn.close()

if __name__ == "__main__":
    main()

