# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:56:55 2022

@author: Nikhil
"""

""" Importing libraries and loading datasets """

# importing the libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

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


""" REGRESSION ANALYSIS """



data_sample = data.sample(n=3000)

""" 1st Model """

# predictors - removed latitude, longitude
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

# dependent variable 
y = data_sample['price']

# adding constant in the data          
X = sm.add_constant(X)

# building the model
est_1 = sm.OLS(y, X).fit()

# summarizing the model
est_1.summary()


"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.117
Model:                            OLS   Adj. R-squared:                  0.113
Method:                 Least Squares   F-statistic:                     30.31
Date:                Sun, 05 Jun 2022   Prob (F-statistic):           3.17e-71
Time:                        20:01:19   Log-Likelihood:                -20251.
No. Observations:                3000   AIC:                         4.053e+04
Df Residuals:                    2986   BIC:                         4.061e+04
Df Model:                          13                                         
Covariance Type:            nonrobust                                         
==================================================================================================
                                     coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------------
const                          -2.188e+04   1.18e+04     -1.854      0.064    -4.5e+04    1258.036
latitude                        -129.5968    115.793     -1.119      0.263    -356.638      97.445
longitude                       -366.2494    132.955     -2.755      0.006    -626.942    -105.557
minimum_nights                     0.1960      0.220      0.890      0.374      -0.236       0.628
number_of_reviews                 -0.1990      0.107     -1.852      0.064      -0.410       0.012
reviews_per_month                 -4.1052      3.128     -1.312      0.189     -10.238       2.028
calculated_host_listings_count    -0.1612      0.118     -1.369      0.171      -0.392       0.070
availability_365                   0.2660      0.031      8.654      0.000       0.206       0.326
Bronx                             82.9870     61.631      1.347      0.178     -37.856     203.830
Brooklyn                          84.4134     48.687      1.734      0.083     -11.051     179.878
Manhattan                        136.8082     49.498      2.764      0.006      39.755     233.861
Queens                           102.4810     54.495      1.881      0.060      -4.371     209.333
Entire home/apt                  143.5016     24.556      5.844      0.000      95.353     191.650
Private room                      38.4940     24.651      1.562      0.118      -9.840      86.828
==============================================================================
Omnibus:                     5633.727   Durbin-Watson:                   1.983
Prob(Omnibus):                  0.000   Jarque-Bera (JB):         10355432.017
Skew:                          13.989   Prob(JB):                         0.00
Kurtosis:                     289.462   Cond. No.                     5.83e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.83e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

# prediction
X_copy = X.copy()
X_copy['y_pred_1'] = est_1.predict(X)
X_copy['y_pred'] = est_1.predict(X)
y_copy = pd.DataFrame({'y_actual':y, 'y_pred':est_1.predict(X)})
y_copy['residuals'] = y_copy['y_pred'] - y_copy['y_actual']
X_copy['residuals'] = X_copy['y_pred'] - y_copy['y_actual']

# Checking the linearity

# residual vs y 
plt.scatter(y_copy['y_actual'], y_copy['residuals'])
plt.plot()

# plot residual vs predictors
def plot_residual_vs_predictor(predictor):
    plt.ylim(-5700, 5700)
    plt.scatter(X_copy[predictor], X_copy['residuals'])
    plt.axhline(y = 0.5, color='black', linestyle = '--')
    plt.plot()

# plot between predictors and results
def plot_results_vs_predictor(predictor, results):
    plt.scatter(X_copy[predictor], X_copy[results])
    plt.plot()

# residual vs latitude
plot_residual_vs_predictor('latitude')

# residual vs longitude
plot_residual_vs_predictor('longitude')

# residual vs minimum_nights
plot_residual_vs_predictor('minimum_nights')

# residual vs num_of_reviews
plot_residual_vs_predictor('number_of_reviews')

# residual vs reviews_per_month
plot_residual_vs_predictor('reviews_per_month')

# residual vs calculated_host_listings_count
plot_residual_vs_predictor('calculated_host_listings_count')

# residual vs availability_365
plot_residual_vs_predictor('availability_365')


""" 2nd Model """

# check the correlation between the variables
corr = X.corr()


# we dropped longitude and latitude as we are taking neighborhodd_groups, which serves the same purpose
# number of review and reviews per month are also very correlated so we are dropping reviews per month

X = data_sample[[
          'number_of_reviews',
          'availability_365', 
          'Entire home/apt', 
          ]]

# dependent variable 
y = data_sample['price']

# adding constant in the data          
X = sm.add_constant(X)

# building the model
est_1 = sm.OLS(y, X).fit()

# summarizing the model
est_1.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.095
Model:                            OLS   Adj. R-squared:                  0.094
Method:                 Least Squares   F-statistic:                     104.6
Date:                Mon, 06 Jun 2022   Prob (F-statistic):           2.01e-64
Time:                        02:12:03   Log-Likelihood:                -20288.
No. Observations:                3000   AIC:                         4.058e+04
Df Residuals:                    2996   BIC:                         4.061e+04
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                69.8091      6.658     10.485      0.000      56.755      82.864
number_of_reviews    -0.3095      0.087     -3.577      0.000      -0.479      -0.140
availability_365      0.2436      0.029      8.350      0.000       0.186       0.301
Entire home/apt     117.9624      7.658     15.404      0.000     102.947     132.978
==============================================================================
Omnibus:                     5588.431   Durbin-Watson:                   1.987
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          9858949.670
Skew:                          13.752   Prob(JB):                         0.00
Kurtosis:                     282.491   Cond. No.                         422.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""

# prediction
X_copy = X.copy()
X_copy['y_pred'] = est_1.predict(X)
X_copy['y'] = y
y_copy = pd.DataFrame({'y_actual':y, 'y_pred':est_1.predict(X)})
y_copy['residuals'] = y_copy['y_pred'] - y_copy['y_actual']
X_copy['residuals'] = X_copy['y_pred'] - y_copy['y_actual']

# residual vs number_of_reviews
plot_residual_vs_predictor('number_of_reviews')

# residual vs availability_365
plot_residual_vs_predictor('availability_365')

# residual vs Entire home/apt
plot_residual_vs_predictor('Entire home/apt')

# check linearity - number of reviews vs results
plot_results_vs_predictor('number_of_reviews', 'y')

# check linearity - availability vs results
plot_results_vs_predictor('availability_365', 'y')


""" Remove the y-values which are more than 500 to check whether these points were influntial are not """

data_sample_2 = data_sample.query('price<=1000')

X = data_sample_2[['number_of_reviews',
                  'availability_365', 
                  'Entire home/apt', 
                 ]]

# dependent variable 
y = data_sample_2['price']

# adding constant in the data          
X = sm.add_constant(X)

# building the model
est_1 = sm.OLS(y, X).fit()

# summarizing the model
est_1.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.263
Model:                            OLS   Adj. R-squared:                  0.263
Method:                 Least Squares   F-statistic:                     355.1
Date:                Mon, 06 Jun 2022   Prob (F-statistic):          3.94e-197
Time:                        02:31:30   Log-Likelihood:                -17931.
No. Observations:                2982   AIC:                         3.587e+04
Df Residuals:                    2978   BIC:                         3.589e+04
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                72.5648      3.134     23.151      0.000      66.419      78.711
number_of_reviews    -0.1925      0.042     -4.579      0.000      -0.275      -0.110
availability_365      0.1150      0.014      8.236      0.000       0.088       0.142
Entire home/apt     114.5281      3.626     31.582      0.000     107.418     121.639
==============================================================================
Omnibus:                     2080.917   Durbin-Watson:                   1.976
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            36448.237
Skew:                           3.128   Prob(JB):                         0.00
Kurtosis:                      18.944   Cond. No.                         416.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""

# prediction
X_copy = X.copy()
X_copy['y_pred'] = est_1.predict(X)
X_copy['y'] = y
y_copy = pd.DataFrame({'y_actual':y, 'y_pred':est_1.predict(X)})
y_copy['residuals'] = y_copy['y_pred'] - y_copy['y_actual']
X_copy['residuals'] = X_copy['y_pred'] - y_copy['y_actual']

# check linearity - number of reviews vs results
plot_results_vs_predictor('number_of_reviews', 'y')

# check linearity - availability vs results
plot_results_vs_predictor('availability_365', 'y')

# residual vs number_of_reviews
plot_residual_vs_predictor('number_of_reviews')

# residual vs availability_365
plot_residual_vs_predictor('availability_365')

# lets add Manhattan in as the feature
X = data_sample_2[[
          'number_of_reviews',
          'availability_365', 
          'Entire home/apt',
          'Manhattan',
          'minimum_nights'
          ]]

# dependent variable 
y = data_sample_2['price']

# adding constant in the data          
X = sm.add_constant(X)

# building the model
est_1 = sm.OLS(y, X).fit()

# summarizing the model
est_1.summary()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.316
Model:                            OLS   Adj. R-squared:                  0.315
Method:                 Least Squares   F-statistic:                     343.1
Date:                Mon, 06 Jun 2022   Prob (F-statistic):          3.74e-243
Time:                        02:48:47   Log-Likelihood:                -17822.
No. Observations:                2982   AIC:                         3.565e+04
Df Residuals:                    2977   BIC:                         3.568e+04
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                52.7858      3.295     16.018      0.000      46.324      59.247
number_of_reviews    -0.1740      0.041     -4.290      0.000      -0.253      -0.094
availability_365      0.1163      0.013      8.633      0.000       0.090       0.143
Entire home/apt     106.0736      3.541     29.954      0.000      99.130     113.017
Manhattan            53.7363      3.570     15.051      0.000      46.736      60.737
==============================================================================
Omnibus:                     2116.311   Durbin-Watson:                   1.989
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            39110.430
Skew:                           3.184   Prob(JB):                         0.00
Kurtosis:                      19.560   Cond. No.                         426.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""

corr = X.corr()


""" Important !!!!!!!!!!!!!!!!!!! 
After adding minimum nights the r squared value increased 

"""

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.324
Model:                            OLS   Adj. R-squared:                  0.322
Method:                 Least Squares   F-statistic:                     284.7
Date:                Mon, 06 Jun 2022   Prob (F-statistic):          2.06e-249
Time:                        02:51:47   Log-Likelihood:                -17804.
No. Observations:                2982   AIC:                         3.562e+04
Df Residuals:                    2976   BIC:                         3.566e+04
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                54.8942      3.296     16.655      0.000      48.431      61.357
number_of_reviews    -0.2079      0.041     -5.105      0.000      -0.288      -0.128
availability_365      0.1331      0.014      9.721      0.000       0.106       0.160
Entire home/apt     107.9790      3.536     30.539      0.000     101.046     114.912
Manhattan            54.9716      3.556     15.459      0.000      47.999      61.944
minimum_nights       -0.7345      0.124     -5.922      0.000      -0.978      -0.491
==============================================================================
Omnibus:                     2111.725   Durbin-Watson:                   1.992
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            38853.411
Skew:                           3.175   Prob(JB):                         0.00
Kurtosis:                      19.504   Cond. No.                         427.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""

# prediction
X_copy = X.copy()
X_copy['y_pred'] = est_1.predict(X)
X_copy['y'] = y
y_copy = pd.DataFrame({'y_actual':y, 'y_pred':est_1.predict(X)})
y_copy['residuals'] = y_copy['y_pred'] - y_copy['y_actual']
X_copy['residuals'] = X_copy['y_pred'] - y_copy['y_actual']

# check linearity - number of reviews vs results
plot_results_vs_predictor('number_of_reviews', 'y')

# check linearity - availability vs results
plot_results_vs_predictor('availability_365', 'y')

# check linearity - minimum_nights vs results
plot_results_vs_predictor('minimum_nights', 'y')

# check linearity - minimum_nights vs results
plot_results_vs_predictor('Manhattan', 'y')

# check linearity - minimum_nights vs results
plot_results_vs_predictor('Entire home/apt', 'y')


# residual vs number_of_reviews
plot_residual_vs_predictor('number_of_reviews')

# residual vs availability_365
plot_residual_vs_predictor('availability_365')

# residual vs availability_365
plot_residual_vs_predictor('minimum_nights')

""" Model 3 """






