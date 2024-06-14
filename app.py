# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:47:12 2024

@author: nicole.chuang
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df1 = pd.read_excel('C:/Users/nicole.chuang/Desktop/Item_performance/Jan-June/product_sales_2021-2023.xlsx')

# Function to plot time series
def plot_time_series(df, item_num):
    # Select data for the specified item number
    item_data = df[df['Item_num'] == item_num]

    # Transpose the DataFrame for easier plotting
    item_data = item_data.set_index('Item_num').drop(['Description', 'Total'], axis=1).T

    # Plot time series for the specified item
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=item_data[item_num], dashes=False, color='orange')
    plt.title(f'Time Series for {item_num}')
    plt.xlabel('Month')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    st.pyplot(plt)  # Display plot in Streamlit

df = pd.read_excel('C:/Users/nicole.chuang/Desktop/Item_performance/Jan-June/product_sales_1-5_2024.xlsx')
df1 = pd.read_excel('C:/Users/nicole.chuang/Desktop/Item_performance/Jan-June/product_sales_2021-2023.xlsx')

# Main Streamlit app
st.title('Time Series Plot')

# Dropdown to select item number
item_num = st.selectbox('Select Item Number:', df['Item_num'].unique())

# Check if an item number is selected
if item_num:
    plot_time_series(df, item_num)
