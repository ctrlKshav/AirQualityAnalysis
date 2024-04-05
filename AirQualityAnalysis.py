import numpy as np 
import pandas as pd 
import os

# Visualisation libraries
import matplotlib.pyplot as plt

import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.simplefilter(action='ignore', category=(FutureWarning,DeprecationWarning))

pd.options.mode.chained_assignment = None  # default='warn'

url='city_day.csv'
city_day_data=pd.read_csv(url)

# Extract delhi's data 

delhi_data=city_day_data.groupby('City').get_group('Delhi')

def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns

delhi_data.interpolate(limit_direction="both",inplace=True)

for i,each in enumerate(delhi_data['AQI_Bucket']):
    if pd.isnull(delhi_data['AQI_Bucket'].iloc[i]):
        if delhi_data['AQI'].iloc[i]>=0.0 and delhi_data['AQI'].iloc[i]<=50.0:
            delhi_data['AQI_Bucket'].iloc[i]='Good'
        elif delhi_data['AQI'].iloc[i]>=51.0 and delhi_data['AQI'].iloc[i]<=100.0:
            delhi_data['AQI_Bucket'].iloc[i]='Satisfactory'
        elif delhi_data['AQI'].iloc[i]>=101.0 and delhi_data['AQI'].iloc[i]<=200.0:
            delhi_data['AQI_Bucket'].iloc[i]='Moderate'
        elif delhi_data['AQI'].iloc[i]>=201.0 and delhi_data['AQI'].iloc[i]<=300.0:
            delhi_data['AQI_Bucket'][i]='Poor'
        elif delhi_data['AQI'].iloc[i]>=301.0 and delhi_data['AQI'].iloc[i]<=400.0:
            delhi_data['AQI_Bucket'].iloc[i]='Very Poor'
        else:
            delhi_data['AQI_Bucket'].iloc[i]='Severe'


delhi_data['Date'] = pd.to_datetime(delhi_data.Date, format='%Y-%m-%d')
delhi_data['Year'] = delhi_data['Date'].dt.year
delhi_data['Month'] = delhi_data['Date'].dt.month