# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:56:55 2022

@author: Nikhil
"""

""" Importing libraries and loading datasets """

# importing the libraries
import pandas as pd

# importing the dataset
data = pd.read_csv("../../data/data_set_regression_analysis.csv")



""" Dropping irrelevant columns 

Primary keys (irrelavant) - Id, Host_id
Categorical variables (irrelevant) - neighbourhood_group, room_type
Removing one category type from each categories - Staten Island, Shared Room

"""

del data['id']
del data['host_id']
del data['neighbourhood_group']
del data['room_type']

del data['Staten Island']
del data['Shared room']








