import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Prediction History",
    page_icon="🕰️",
    layout="wide",
)

# Display history if available
st.header("Prediction History")
if 'history' in st.session_state and not st.session_state.history.empty:
    st.write(st.session_state.history)
else:
    st.write("No predictions have been made yet.")