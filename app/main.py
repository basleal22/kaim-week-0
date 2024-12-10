import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import process_data

# Title and description
st.title("Data Insights Dashboard")
st.markdown("This dashboard visualizes various data insights from the dataset.")

# Load data
df = process_data()  # Write your data processing function in utils.py

# Sidebar for user input
st.sidebar.title("Filter options")
option = st.sidebar.selectbox("Select a variable to visualize:", ["GHI", "DNI", "DHI", "Tamb"])

# Main plot
st.subheader(f"{option} over time")
st.line_chart(df[option])
