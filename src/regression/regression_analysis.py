# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:56:55 2022

@author: Nikhil
"""

# importing the libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tools.eval_measures import rmse
from scipy.stats import levene

# importing the dataset
data = pd.read_csv("../../data/data_set_regression_analysis.csv")


""" Dropping irrelevant columns 

 - Primary keys (irrelavant) - Id, Host_id

 - Categorical variables (irrelevant) - neighbourhood_group, room_type
   (We have label encoded these groups)

 - Removing one category type from each categories - Staten Island, Shared Room
   (As these are additional group in the predictors)

"""

# dropping the columns
del data['id']
del data['host_id']
del data['neighbourhood_group']
del data['room_type']
del data['Staten Island']
del data['Shared room']


""" modeling only those AirBNB's that are within the range of 0 and 200 """
data = data.query('price>0 and price<200')


""" taking random sample of 3000 datapoints for modeling """
data_sample = data.sample(n=3000, random_state=49)


###############################################################################
############################ REGRESSION ANALYSIS ##############################
###############################################################################

""" Performing STEPWISE modeling """

# split the dataset into predictors and response
# predictors
X = data_sample[['latitude', 
          'longitude', 
          'minimum_nights',
          'number_of_reviews',
          'reviews_per_month', 
          'calculated_host_listings_count',
          'availability_365', 
          'Bronx', 
          'Brooklyn', 
          'Manhattan', 
          'Queens',
          'Entire home/apt', 
          'Private room']]

# response
y = data_sample['price']

# adding the constant terms as a predictor
X = sm.add_constant(X)

# we will have dropped some predictors based on the correlations

''' First Model with latitude as feature '''

# building the model
est_1 = sm.OLS(y, X[['const','latitude']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.003

''' First Model with longitude as feature '''
# building the model
est_1 = sm.OLS(y, X[['const','longitude']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.000

''' First Model with minimum_nights as feature '''
# building the model
est_1 = sm.OLS(y, X[['const','minimum_nights']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.687

''' First Model with number_of_reviews as feature '''
# building the model
est_1 = sm.OLS(y, X[['const','number_of_reviews']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.010

''' First Model with calculated_host_listings_count as feature '''
# building the model
est_1 = sm.OLS(y, X[['const','calculated_host_listings_count']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.037

''' First Model with availability_365 as feature '''
# building the model
est_1 = sm.OLS(y, X[['const','availability_365']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.291

''' First Model with Entire home/apt as feature '''
# building the model
est_1 = sm.OLS(y, X[['const','Entire home/apt']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.000

''' First Model with Manhattan as feature '''
# building the model
est_1 = sm.OLS(y, X[['const','Manhattan']]).fit()
# summarizing the model
est_1.summary()
# p value of 0.000


###############################################################################

''' Second Model with Entire home/apt as first feature and longitude'''
# building the model
est_2 = sm.OLS(y, X[['const','Entire home/apt','longitude']]).fit()
# summarizing the model
est_2.summary()
# p value of 0.000 (44.633) and 0.000(-14.688)

''' Second Model with Entire home/apt as first feature and latitude'''
# building the model
est_2 = sm.OLS(y, X[['const','Entire home/apt','latitude']]).fit()
# summarizing the model
est_2.summary()
# p value of 0.000 (45.399) and 0.000(4.747)

''' Second Model with Entire home/apt as first feature and number_of_reviews'''
# building the model
est_2 = sm.OLS(y, X[['const','Entire home/apt','number_of_reviews']]).fit()
# summarizing the model
est_2.summary()
# p value of 0.000 (45.105) and 0.000(2.193)

''' Second Model with Entire home/apt as first feature and calculated_host_listings_count'''
# building the model
est_2 = sm.OLS(y, X[['const','Entire home/apt','calculated_host_listings_count']]).fit()
# summarizing the model
est_2.summary()
# p value of 0.000 (44.810) and 0.00(3.669)

''' Second Model with Entire home/apt as first feature and Manhattan'''
# building the model
est_2 = sm.OLS(y, X[['const','Entire home/apt','Manhattan']]).fit()
# summarizing the model
est_2.summary()
# p value of 0.000 (44.810) and 0.00(17.045)


###############################################################################

''' Third model with Entire home/apt as first feature, longitude as second feature and latitude'''
# building the model
est_3 = sm.OLS(y, X[['const','Entire home/apt','Manhattan','longitude']]).fit()
# summarizing the model
est_3.summary()
# p value of 0.000 (44.988) and 0.000(12.551) and 0.000(-9.261)

''' Third model with Entire home/apt as first feature, longitude as second feature and latitude'''
# building the model
est_3 = sm.OLS(y, X[['const','Entire home/apt','Manhattan','latitude']]).fit()
# summarizing the model
est_3.summary()
# p value of 0.000 (44.918) and 0.000(17.917) and 0.000(-7.114)

''' Third model with Entire home/apt as first feature, longitude as second feature and number_of_reviews'''
# building the model
est_3 = sm.OLS(y, X[['const','Entire home/apt','Manhattan','number_of_reviews']]).fit()
# summarizing the model
est_3.summary()
# p value of 0.000 (44.576) and 0.000(17.120) and 0.000(2.690)

''' Third model with Entire home/apt as first feature, longitude as second feature and calculated_host_listings_count'''
# building the model
est_3 = sm.OLS(y, X[['const','Entire home/apt','Manhattan','calculated_host_listings_count']]).fit()
# summarizing the model
est_3.summary()
# p value of 0.000 (44.360) and 0.000(16.724) and 0.000(1.904)

###############################################################################

''' Fourth model with Entire home/apt as first feature, longitude as second feature, latitude as third feature and number_of_reviews'''
# building the model
est_4 = sm.OLS(y, X[['const','Entire home/apt','Manhattan', 'latitude','longitude']]).fit()
# summarizing the model
est_4.summary()
# p value of 0.000 (44.837) and 0.000(11.216) and 0.000(-3.317) and 0.000(-6.760)

''' Fourth model with Entire home/apt as first feature, longitude as second feature, latitude as third feature and number_of_reviews'''
# building the model
est_4 = sm.OLS(y, X[['const','Entire home/apt','Manhattan', 'latitude','number_of_reviews']]).fit()
# summarizing the model
est_4.summary()
# p value of 0.000 (44.874) and 0.000(17.983) and 0.000(-7.124) and 0.000(2.718)

''' Fourth model with Entire home/apt as first feature, longitude as second feature, latitude as third feature and calculated_host_listings_count'''
# building the model
est_4 = sm.OLS(y, X[['const','Entire home/apt','longitude','latitude','calculated_host_listings_count']]).fit()
# summarizing the model
est_4.summary()
# p value of 0.000 (44.576) and 0.000(-15.188) and 0.000(6.374) and 0.000(2.788)

###############################################################################

''' Fifth model with Entire home/apt as first feature, longitude as second feature, latitude as third feature and number_of_reviews'''
# building the model
est_5 = sm.OLS(y, X[['const','Entire home/apt','Manhattan','latitude','longitude','number_of_reviews']]).fit()
# summarizing the model
est_5.summary()
# p value of 0.000 (44.576) and 0.000(11.195) and 0.000(-3.255) and 0.000(-6.912) and 0.000(3.074)

''' Fifth model with Entire home/apt as first feature, longitude as second feature, latitude as third feature and number_of_reviews'''
# building the model
est_5 = sm.OLS(y, X[['const','Entire home/apt','Manhattan','latitude','longitude','calculated_host_listings_count']]).fit()
# summarizing the model
est_5.summary()
# p value of 0.000 (44.653) and 0.000(10.977) and 0.000(-3.229) and 0.000(-6.781) and 0.000(1.647)

###############################################################################

''' Sixth model with Entire home/apt as first feature, longitude as second feature, latitude as third feature and number_of_reviews'''
# building the model
est_6 = sm.OLS(y, X[['const','Entire home/apt','Manhattan','latitude','longitude','number_of_reviews','calculated_host_listings_count']]).fit()
# summarizing the model
est_6.summary()
# p value of 0.000 (44.586) and 0.000(10.933) and 0.000(-3.155) and 0.000(-6.941) and 0.000(3.186) and 0.000(1.848)

# lets check the RMSE score
predicted_y = est_6.predict(X[['const','Entire home/apt','Manhattan','latitude','longitude','number_of_reviews','calculated_host_listings_count']])
rmse(predicted_y, y)

"""   
    R Sq value: 0.477
    Adj R Sq value: 0.476
    RMSE: 32.12 

"""

# checking the correlation
corr = X[['const','Entire home/apt','Manhattan','longitude','latitude','number_of_reviews','calculated_host_listings_count']].corr()
# no strong correlation is identified between different predictors


""" lets explore the linearity, independence, normal and constant error variance criteria for the 6th model """

# create a dataframe to store all the relevant data
ref = X[['const',
         'Entire home/apt',
         'Manhattan',
         'longitude',
         'latitude',
         'number_of_reviews',
         'calculated_host_listings_count']]
ref['residual'] = est_6.resid
ref['y'] = y
ref['y_pred'] = est_6.predict(X[['const',
                                 'Entire home/apt',
                                 'Manhattan',
                                 'longitude',
                                 'latitude',
                                 'number_of_reviews',
                                 'calculated_host_listings_count']])


""" check for linearity - residual plot with response """
plt.ylim(-150, 150)
plt.scatter(ref['y'], ref['residual'])
plt.axhline(y = 0.5, color='black', linestyle = '--')
plt.plot()

""" Since we can see the residuals are negative in for the datapoints at the 
beginning which later become positive We can see a increasing trend in the data """

# since the plot is not linear we have to transform the predictors and/or results 
X["longitude_2"] = X["longitude"]*X["longitude"]
X["latitude_2"] = X["latitude"]*X["latitude"]
X["number_of_reviews_2"] = X["number_of_reviews"]*X["number_of_reviews"]
X["calculated_host_listings_count_2"] = X["calculated_host_listings_count"]*X["calculated_host_listings_count"]

# taking squared root of the response
sqrt_y = np.sqrt(data_sample['price'])

# building the model
est_7 = sm.OLS(sqrt_y, X[['const',
                         'Entire home/apt',
                         'longitude',
                         'latitude',
                         'Manhattan',
                         'number_of_reviews',
                         'calculated_host_listings_count',
                         'longitude_2',
                         'latitude_2',
                         'number_of_reviews_2',
                         'calculated_host_listings_count_2']]).fit()

# summarizing the model
est_7.summary()

# lets check the RMSE score
predicted_y = est_7.predict(X[['const',
                         'Entire home/apt',
                         'longitude',
                         'latitude',
                         'Manhattan',
                         'number_of_reviews',
                         'calculated_host_listings_count',
                         'longitude_2',
                         'latitude_2',
                         'number_of_reviews_2',
                         'calculated_host_listings_count_2']])
rmse(predicted_y, sqrt_y)

"""   
    R Sq value: 0.512
    Adj R Sq value: 0.510
    RMSE: 1.57

"""

# checking the correlation
corr = X[['const',
          'Entire home/apt',
          'longitude',
          'latitude',
          'Manhattan',
          'number_of_reviews',
          'calculated_host_listings_count',
          'longitude_2',
          'latitude_2',
          'number_of_reviews_2',
          'calculated_host_listings_count_2']].corr()
# strong correlation is identified between predictors and their squared terms


""" lets explore the linearity, independence, normal and constant error variance criteria for the 6th model """

# create a dataframe to store all the relevant data
ref_2 = X[['const',
          'Entire home/apt',
          'longitude',
          'latitude',
          'Manhattan',
          'number_of_reviews',
          'calculated_host_listings_count',
          'longitude_2',
          'latitude_2',
          'number_of_reviews_2',
          'calculated_host_listings_count_2']]
ref_2['residual'] = est_7.resid
ref_2['y'] = sqrt_y
ref_2['y_pred'] = est_7.predict(X[['const',
                                  'Entire home/apt',
                                  'longitude',
                                  'latitude',
                                  'Manhattan',
                                  'number_of_reviews',
                                  'calculated_host_listings_count',
                                  'longitude_2',
                                  'latitude_2',
                                  'number_of_reviews_2',
                                  'calculated_host_listings_count_2']])

""" check for linearity - residual plot with response """
plt.ylim(-150, 150)
plt.scatter(ref_2['y'], ref_2['residual'])
plt.axhline(y = 0.5, color='black', linestyle = '--')
plt.plot()

""" There is still some upward trend remaining in the data but it had been reduced significantly """

""" Check the equal variance using Levene's test"""
# splitting the errors in two groups based on number of reviews
grp_1 = ref_2.query('number_of_reviews < 5')['residual']
grp_2 = ref_2.query('number_of_reviews >= 5')['residual']
levene(grp_1, grp_2, center='median')
# this results in non equal variance as the p value is 1.8e-105


# since the plot is not linear we have to transform the predictors and/or results 

X["longitude_3"] = X["longitude_2"]*X["longitude"]
X["latitude_3"] = X["latitude_2"]*X["latitude"]
X["calculated_host_listings_count_3"] = X["calculated_host_listings_count_2"]*X["calculated_host_listings_count"]
X["longitude_chlc"] = X["longitude"]*X["calculated_host_listings_count"]
X["latitude_number_of_reviews"] = X["number_of_reviews"]*X["latitude"]
X["latitude_chls"] = X["calculated_host_listings_count"]*X["latitude"]
X["number_of_reviews_chls"] = X["number_of_reviews"]*X['calculated_host_listings_count_3']
X["manhattan_entire_apt_num_reviews"] = X["Entire home/apt"]*X['Manhattan']*X['number_of_reviews']
X["manhattan_entire_apt_available"] = X["Entire home/apt"]*X['Manhattan']*X['availability_365']
X["manhattan_long_lat"] = X["longitude"]*X['Manhattan']*X['latitude']
X["entire_home_long_lat_manhattan"] = X["longitude"]*X['Entire home/apt']*X['latitude']*X['Manhattan']

# transforming the results 
y_1_4 = np.power(data_sample['price'],1/4)

# assinging weights for least squared regression
w_n = np.ones(3000)
w_n[0:2850] = 9
w_n[2850:] = 1/9

est_8 = sm.WLS(y_1_4, 
               X[['const',
                'Entire home/apt',
                'number_of_reviews',
                'calculated_host_listings_count',
                'longitude_2',
                'latitude_2',
                'number_of_reviews_2',
                'calculated_host_listings_count_2',
                'longitude_3',
                'latitude_3',
                'calculated_host_listings_count_3',
                'longitude_chlc',
                'latitude_number_of_reviews',
                'latitude_chls',
                'number_of_reviews_chls',
                'manhattan_entire_apt_num_reviews',
                'manhattan_entire_apt_available',
                'manhattan_long_lat',
                'entire_home_long_lat_manhattan',
                'long_2_lat_2_number_of_reviews']], weights=1/w_n**2).fit()

est_8.summary()

# lets check the RMSE score
predicted_y = est_8.predict(X[['const',
                            'Entire home/apt',
                            'number_of_reviews',
                            'calculated_host_listings_count',
                            'longitude_2',
                            'latitude_2',
                            'number_of_reviews_2',
                            'calculated_host_listings_count_2',
                            'longitude_3',
                            'latitude_3',
                            'calculated_host_listings_count_3',
                            'longitude_chlc',
                            'latitude_number_of_reviews',
                            'latitude_chls',
                            'number_of_reviews_chls',
                            'manhattan_entire_apt_num_reviews',
                            'manhattan_entire_apt_available',
                            'manhattan_long_lat',
                            'entire_home_long_lat_manhattan',
                            'long_2_lat_2_number_of_reviews']])

rmse(predicted_y, y_1_4)
    
"""   
    R Sq value: 0.646
    Adj R Sq value: 0.644
    RMSE: 0.355

"""






























# building the model
est_8 = sm.WLS(rt_4_y, X_test, weights=1/w_n**2).fit()

est_8 = sm.OLS(rt_4_y, X_test).fit()

from statsmodels.tools.eval_measures import rmse

ypred = est_8.predict(X_test)

rmse(rt_4_y, ypred)

# summarizing the model
est_8.summary() 

ref = X_test.copy()

# residual analusis
ref['residual_8'] = est_8.resid
ref['residual_8_2'] = np.power(est_8.resid,2)
ref['residual_8_abs'] = np.absolute(est_8.resid)
ref['rt_4_y'] = rt_4_y

# checking the residuals
ref_temp = ref.sample(50, random_state=12)
plt.ylim(-10, 10)
plt.scatter(ref_temp['rt_4_y'], ref_temp['residual_8'])
plt.axhline(y = 0.0, color='black', linestyle = '--')
plt.plot()


# statistical test to check variance using LEVENE TEST
from scipy.stats import levene
# splitting the errors in two groups based on number of reviews
grp_1 = ref.query('number_of_reviews < 5')['residual_8']
grp_2 = ref.query('number_of_reviews >= 5')['residual_8']
levene(grp_1, grp_2, center='median')


from scipy import stats as stats_sw
stats_sw.shapiro(ref['residual_8'])

import seaborn as sns
sns.distplot(ref['residual_8'])

# final done

###############################################################################
####################### lets remove the outliers ##############################
###############################################################################

# get the influence
influence = est_8.get_influence()

# cooks values
cooks_d = influence.cooks_distance[0]
studentized_residuals = influence.resid_studentized_external
studentized_residuals_i = influence.resid_studentized_internal
leverage = influence.hat_matrix_diag

X_test['cooks_distance'] = cooks_d
X_test['studentized_residuals'] = studentized_residuals
X_test['studentized_residuals_i'] = studentized_residuals_i
X_test['leverage'] = leverage

X_test_2 = X_test.query('studentized_residuals<3.0 and studentized_residuals>-3.0')
X_test_2 = X_test.query('leverage<0.034')

X_test_2_temp = pd.merge(X_test_2, rt_4_y, left_index=True, right_index=True)

y_test_2_temp = X_test_2_temp['price']

del X_test_2_temp['price']
del X_test_2_temp['cooks_distance']
del X_test_2_temp['studentized_residuals_i']
del X_test_2_temp['studentized_residuals']
del X_test_2_temp['leverage']

w_n = np.ones(2895)
w_n[0:2800] = 8
w_n[2800:] = 1/8

est_10 = sm.WLS(y_test_2_temp, X_test_2_temp, weights=1/w_n**2).fit()
est_10 = sm.OLS(y_test_2_temp, X_test_2_temp).fit()

est_10.summary()

ypred2 = est_10.predict(X_test_2_temp)

rmse(y_test_2_temp, ypred2)

# residuals
res_2 = X_test_2_temp.copy()
res_2['residual_10'] = est_10.resid
#ref['residual_8_2'] = np.power(est_8.resid,2)
#ref['residual_8_abs'] = np.absolute(est_8.resid)
#ref['rt_4_y'] = rt_4_y

# checking the residuals
ref_temp = ref.sample(50, random_state=12)
plt.ylim(-10, 10)
plt.scatter(y_test_2_temp, res_2['residual_10'])
plt.axhline(y = 0.0, color='black', linestyle = '--')
plt.plot()


grp_1 = res_2.query('number_of_reviews < 3')['residual_10']
grp_2 = res_2.query('number_of_reviews >= 3')['residual_10']
levene(grp_1, grp_2, center='median')

sns.distplot(res_2['residual_10'])
stats_sw.shapiro(res_2['residual_10'])




# adding the columns
ref['residual_6'] = est_8.resid
ref['rt_4_y'] = rt_4_y

# checking the residuals
ref_temp = ref.sample(50, random_state=12)
plt.ylim(-10, 10)
plt.scatter(ref_temp['rt_4_y'], ref_temp['residual_6'])
plt.axhline(y = 0.5, color='black', linestyle = '--')
plt.plot()

# check for linearity and variance - residual plot with predictor longitude
plt.ylim(-10, 10)
plt.scatter(ref_temp['longitude'], ref_temp['residual_5'])
plt.axhline(y = 0.5, color='black', linestyle = '--')
plt.plot()


from scipy.stats import levene
# splitting the errors in two groups based on number of reviews
grp_1 = ref.query('number_of_reviews < 3')['residual_6']
grp_2 = ref.query('number_of_reviews >= 3')['residual_6']
levene(grp_1, grp_2, center='median')

