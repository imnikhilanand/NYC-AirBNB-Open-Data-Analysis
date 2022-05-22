# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:06:36 2022

@author: Nikhil
"""

# importing the dataset
import pandas as pd
import numpy as np

# class to clean the data
class clean_data:

    # clean the data     
    def __init__(self, data):
        self.data = pd.read_csv(data)
        self.raw_data = pd.read_csv(data)

    # returning the data
    def return_data(self):
        return self.data

    # returning the raw data 
    def return_raw_data(self):
        return self.raw_data

    # cleaning the data
    def check_num_of_columns(self):
        return self.data.columns
    
    # drop irrelevant columns
    def drop_columns(self, col_name):
        del self.data[col_name]
        
    # replacing nan values with something
    def replacing_nan_values(self,col_name,replaced_with):
        self.data[col_name] = self.data[col_name].replace(np.nan, replaced_with)
    
    # save the data
    def save_dataset(self,name_of_the_file):
        self.data.to_csv(name_of_the_file, index=False)


# calling the objeect with the dataset   
obj = clean_data("../../data/AB_NYC_2019.csv") 

# checking different columns in the database
obj.check_num_of_columns()   

# dropping the name
obj.drop_columns("name")

# dropping the host name
obj.drop_columns("host_name")

# dropping the last reviewed at
obj.drop_columns("last_review")

# fetching the data
data = obj.return_data()

# replace nan values with 0
obj.replacing_nan_values("reviews_per_month",0)

# checked all the null values
data.info()

# saving the dataset after dropping the irrelvant columns
obj.save_dataset("../../data/data_set_for_visualization.csv")


