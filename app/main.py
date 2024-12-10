import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import process_data

data= pd.read_csv('https://github.com/basleal22/kaim-week-0/blob/task1/data/benin-malanville.csv')

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
# Ensure the date column is in datetime format
data['date'] = pd.to_datetime(data['date_column_name'])  # Replace with your date column name
# Add a sidebar for the date range slider
st.sidebar.header("Filter by Date Range")
date_range = st.sidebar.slider(
    "Select Date Range:",
    min_value=data['date'].min().date(),
    max_value=data['date'].max().date(),
    value=(data['date'].min().date(), data['date'].max().date()),
    format="YYYY-MM-DD"
)
filtered_data = data[(data['date'] >= pd.Timestamp(date_range[0])) & (data['date'] <= pd.Timestamp(date_range[1]))]
st.write(f"Showing data from {date_range[0]} to {date_range[1]}")

# Example: Line chart for GHI, DNI, DHI, and Tamb over time
st.line_chart(filtered_data[['date', 'GHI', 'DNI', 'DHI', 'Tamb']].set_index('date'))

