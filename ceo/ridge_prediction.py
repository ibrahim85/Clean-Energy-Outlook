import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import os
import os.path as op
import inspect
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# function for nuclear energy data
def pred_nuclear(data):
    """
    Function to predict future values of NUETP
    Inputs:
           data (Pandas DataFrame): original data
    Returns:
            data (Pandas DataFrame): original + predicted values
    """
    data['k1']=0
    for i in range(0,55):
        if i >= 1:
            data['k1'][i]=data['NUETP'][i-1]

    # Split data for train and test
    all_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['NUETP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    for i in range(55,61):
        data['k1'][i]=data['NUETP'][i-1]
        future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][i:i+1]
        pred = regr2.predict(future_x)
        #Replacing negative values with 0
        if pred < 0:
            pred = 0
        data['NUETP'][i] = pred
    del data['k1']

    return data

# function for solar energy data
def pred_solar(data):
    """
    Function to predict future values of SOEGP
    Inputs:
           data (Pandas DataFrame): original data
    Returns:
            data (Pandas DataFrame): original + predicted values
    """
    data['k1']=0
    for i in range(0,55):
        if i >= 1:
            data['k1'][i]=data['SOEGP'][i-1]

    # Split data for train and test
    all_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['SOEGP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    for i in range(55,61):
        data['k1'][i]=data['SOEGP'][i-1]
        future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][i:i+1]
        pred = regr2.predict(future_x)
        #Replacing negative values with 0
        if pred < 0:
            pred = 0
        data['SOEGP'][i] = pred
    del data['k1']
    return data

# function for wind energy data
def pred_wind(data):
    """
    Function to predict future values of WYTCP
    Inputs:
           data (Pandas DataFrame): original data
    Returns:
            data (Pandas DataFrame): original + predicted values
    """
    data['k1']=0
    for i in range(0,55):
        if i >= 1:
            data['k1'][i]=data['WYTCP'][i-1]
    all_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['WYTCP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    for i in range(55,61):
        data['k1'][i]=data['WYTCP'][i-1]
        future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][i:i+1]
        pred = regr2.predict(future_x)
        #Replacing negative values with 0
        if pred < 0:
            pred = 0
        data['WYTCP'][i] = pred
    del data['k1']
    return data

# function for hydro energy data
def pred_hydro(data):
    """
    Function to predict future values of HYTCP
    Inputs:
           data (Pandas DataFrame): original data
    Returns:
            data (Pandas DataFrame): original + predicted values
    """
    data['k1']=0
    for i in range(0,55):
        if i >= 1:
            data['k1'][i]=data['HYTCP'][i-1]
    all_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['HYTCP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    for i in range(55,61):
        data['k1'][i]=data['HYTCP'][i-1]
        future_x = data[['k1','GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][i:i+1]
        pred = regr2.predict(future_x)
    #Replacing negative values with 0
        if pred < 0:
            pred = 0
        data['HYTCP'][i] = pred
    del data['k1']
    return data

def ridge_predict_all():
    """
    Wrapping function for Ridge
    Inputs:
           None
    Returns:
            None
    """
    #Path of Cleaned and Predicted Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_clean = op.join(path, 'Cleaned Data')
    path_predict = op.join(path, 'Predicted Data')
    path_predict = op.join(path_predict, 'Ridge Regression')
    statelist = os.listdir(path_clean)
    if not os.path.exists(path_predict):
        os.makedirs(path_predict)
    for i in statelist:
        path = op.join(path_predict, i)
        data = pd.read_csv(path)
        #Predicting nuclear, wind. hydro and solar
        data = pred_nuclear(data)
        data = pred_hydro(data)
        data = pred_wind(data)
        data = pred_solar(data)
        data.rename(columns={'Unnamed: 0':'State'}, inplace=True)
        data['State'] = i[0:2]
        data.to_csv(path_predict+'\\%s'%i, encoding='utf-8', index=False)
    return
