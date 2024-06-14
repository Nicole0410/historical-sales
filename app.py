# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:47:12 2024

@author: nicole.chuang
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:47:12 2024
@author: nicole.chuang
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import requests
from io import BytesIO

secret_value = st.secrets["MY_SECRET"]
st.write("Secret Value:", secret_value)

# URL of the files in the private repository (use GitHub token)
file_url_2021_2023 = 'https://raw.githubusercontent.com/Nicole0410/private-data/main/product_sales_2021-2023.xlsx'

def fetch_data(file_url, token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        return pd.read_excel(BytesIO(response.content))
    else:
        st.error(f"Failed to retrieve data from {file_url}. Status code: {response.status_code}")
# Main Streamlit app
st.title('Time Series Plot')

# Get GitHub PAT from GitHub Secrets
github_token = st.secrets['MY_SECRET']

# Fetch data from private repository
df = fetch_data(file_url_2021_2023, github_token)

# Function to plot time series
def plot_time_series(df, item_num):
    # Select data for the specified item number
    item_data = df[df['Item_num'] == item_num]

    if item_data.empty:
        st.warning(f"No data found for Item Number {item_num}")
        return
    
    # Transpose the DataFrame for easier plotting
    item_data = item_data.set_index('Item_num').drop(['Description', 'Total'], axis=1).T

    # Plot time series for the specified item
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=item_data[item_num], dashes=False, color='orange')
    plt.title(f'Time Series for Item Number {item_num}')
    plt.xlabel('Month')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Display plot in Streamlit
    st.pyplot()

# Main Streamlit app
st.title('Time Series Plot')

# Dropdown to select item number
item_num = st.selectbox('Select Item Number:', df['Item_num'].unique())

# Check if an item number is selected
if item_num:
    plot_time_series(df, item_num)
