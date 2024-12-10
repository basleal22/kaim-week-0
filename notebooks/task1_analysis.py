import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import plotly.epress as px
import seaborn as sns
import scipy.stats as stats
from scipy.stats import zscore

data=pd.read_csv('C:/Users/hp/Desktop/tutorial/kaim-week-0/data/benin-malanville.csv')
#summary statistics
print(data.describe())
#data quality check, missing values
missing_values=data.isnull().sum()
#print(missing_values)
#plot bar charts or line charts of GHI, DNI, DHI and tamb over time
data['date']=pd.to_datetime(data['date'])#parse date column as datetime
data.set_index('date', inplace=True)
monthly_data=data.resample('M').mean()
#plot line charts for GHI, DNI, DHI and tamb over time
plt.figure(figsize=(10,6))
for column in ['GHI','DNI','DHI','Tamb']:
    plt.plot(monthly_data[column], label=column)
plt.title('Monthly Average of GHI, DNI, DHI and Tamb')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.savefig('monthly_average_plots.png')
plt.close()
#look for anomalies in the data
anomalies=monthly_data['GHI'][monthly_data['GHI']>1000]
anomalies.plot(kind='scatter', figsize=(10,6), title='Anomalies in GHI')
plt.savefig('anomalies_ghi.png')
anomalies_temp=monthly_data['Tamb'][monthly_data['Tamb']>50]
anomalies_temp.plot(kind='scatter', figsize=(10,6), title='Anomalies in Tamb')
plt.savefig('anomalies_temp.png')
plt.close()
# Filter data based on Cleaning column
cleaned_data = data[data["Cleaning"] == True]
uncleaned_data = data[data["Cleaning"] == False]

# Plot ModA and ModB over time for both cleaned and uncleaned data
plt.plot(cleaned_data['time'], cleaned_data['ModA'], label='Cleaned ModA')
plt.plot(uncleaned_data['time'], uncleaned_data['ModB'], label='Uncleaned ModB')

plt.title('Impact of Cleaning on ModA sensor over time')
plt.show()
# Calculate correlation matrix
corr_matrix = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()

# Plot correlation matrix heatmap
import seaborn as sns
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Create pair plot
sns.pairplot(data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']])
plt.show()
# Filter data based on Cleaning column
cleaned_data = data[data["Cleaning"] == True]
uncleaned_data = data[data["Cleaning"] == False]

# Plot ModA and ModB over time for both cleaned and uncleaned data
plt.plot(cleaned_data['time'], cleaned_data['ModA'], label='Cleaned ModA')
plt.plot(uncleaned_data['time'], uncleaned_data['ModA'], label='Uncleaned ModA')
plt.legend()
plt.title('Impact of Cleaning on ModA sensor over time')
plt.show()
# Scatter plot for RH vs Temperature (TModA)
plt.scatter(data['RH'], data['TModA'])
plt.title('RH vs Temperature (TModA)')
plt.xlabel('Relative Humidity (RH)')
plt.ylabel('Temperature (TModA)')
plt.show()
# Plot histograms for GHI, DNI, and DHI
plt.hist(data['GHI'], bins=20, alpha=0.5, label='GHI')
plt.hist(data['DNI'], bins=20, alpha=0.5, label='DNI')
plt.hist(data['DHI'], bins=20, alpha=0.5, label='DHI')
plt.legend(loc='best')
plt.title('Distribution of Solar Irradiance')
plt.show()
from scipy.stats import zscore

# Calculate Z-scores for variables
z_scores = zscore(data[['GHI', 'DNI', 'DHI', 'WS']])

# Flag outliers with Z-scores > 3
outliers = data[(z_scores > 3).any(axis=1)]
print(outliers)
# Bubble chart for GHI vs Tamb vs WS
plt.scatter(data['GHI'], data['Tamb'], s=data['RH']*10, alpha=0.5)  # s is bubble size
plt.title('GHI vs Tamb with Bubble Size Representing RH')
plt.xlabel('GHI')
plt.ylabel('Tamb')
plt.show()
# Drop rows with missing values in critical columns
data_cleaned = data.dropna(subset=['GHI', 'DNI', 'DHI'])

# Remove columns with only null values
data_cleaned = data_cleaned.drop(columns=['Comments'])

# Handle outliers or anomalies based on thresholds

data_cleaned = data_cleaned[data_cleaned['GHI'] <= 1200]