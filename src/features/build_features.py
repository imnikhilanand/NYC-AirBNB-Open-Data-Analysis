# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:42:35 2022

@author: Nikhil
"""

# importing libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# importing the dataset
data = pd.read_csv("../../data/data_set_for_visualization.csv")

# dropping columns neighboorhood to reduce the sparsity
del data["neighbourhood"]

# checking the correlation of continuous variables
corr = data.corr()

# one hot encoding the neigbhorhood_group
le_ng = LabelEncoder()
le_ng.fit(data["neighbourhood_group"])
le_ng_df = le_ng.transform(data["neighbourhood_group"])
le_ng_df_ohe = OneHotEncoder(sparse=False)
le_ng_df = le_ng_df.reshape(len(le_ng_df), 1)
le_ng_df_ohe = le_ng_df_ohe.fit_transform(le_ng_df)
le_ng_df_ohe = pd.DataFrame(le_ng_df_ohe, columns = le_ng.classes_)

# one hot encoding the room_type
le_rt = LabelEncoder()
le_rt.fit(data["room_type"])
le_rt_df = le_rt.transform(data["room_type"])
le_rt_df_ohe = OneHotEncoder(sparse=False)
le_rt_df = le_rt_df.reshape(len(le_rt_df), 1)
le_rt_df_ohe = le_rt_df_ohe.fit_transform(le_rt_df)
le_rt_df_ohe = pd.DataFrame(le_rt_df_ohe, columns = le_rt.classes_)

# joining the tables
temp_merged = pd.merge(le_ng_df_ohe, le_rt_df_ohe, left_index=True, right_index=True, how='inner')
data = pd.merge(data, temp_merged, left_index=True, right_index=True, how='inner')

# saving the processed dataframe
data.to_csv("../../data/data_set_regression_analysis.csv", index=False)