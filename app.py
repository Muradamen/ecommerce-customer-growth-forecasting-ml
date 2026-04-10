import streamlit as st
import pandas as pd

st.title("📈 Customer Growth Forecast")

st.write("This is your first Streamlit app!")

# Simple input
year = st.slider("Select a year", 2025, 2035)

st.write(f"Predicted customers for {year}: {year * 1000}")