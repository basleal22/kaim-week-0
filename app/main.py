import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import process_data
# Load your dataset
data_path = "path/to/your/dataset.csv"  # Replace with the correct path
data = pd.read_csv(data_path)

# Ensure the date column is in datetime format
data['date'] = pd.to_datetime(data['date_column_name'])  # Replace with your date column name


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
# Sidebar or main interface for date range selection
st.sidebar.header("Filter Data")
date_range = st.sidebar.slider(
    "Select Date Range:",
    min_value=data['date'].min(),  # Replace with your dataset's earliest date
    max_value=data['date'].max(),  # Replace with your dataset's latest date
    value=(data['date'].min(), data['date'].max()),  # Default range
    format="YYYY-MM-DD"  # Adjust format as needed
)

