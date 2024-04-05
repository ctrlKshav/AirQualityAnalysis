import numpy as np 
import pandas as pd 
import os

# Visualisation libraries
import matplotlib.pyplot as plt
#matplotlib inline
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

url='city_day.csv'
city_day_data=pd.read_csv(url)

# Extract delhi's data 

delhi_data=city_day_data.groupby('City').get_group('Delhi')

print(delhi_data.head())

def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        print(mis_val)
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        print(mis_val_percent)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        print(mis_val_table)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        print(mis_val_table_ren_columns)
        
        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns
print(missing_values_table(delhi_data))