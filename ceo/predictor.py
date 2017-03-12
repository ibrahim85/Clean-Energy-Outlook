#Importing libraries
import pandas as pd
from sklearn import linear_model
import numpy as np
import os

def future_df(data,year_list):
    """
    Appends a NaN future dataframe to the original dataframe
    Input:
          data (Pandas DataFrame) - Input DataFrame
          year_list (List) - list of years which has to be added to the dataframe
    Returns:
            data (Pandas DataFrame) - Contains original and NaN columns for all years
    """
    #Dataframe for future predictions
    future=pd.DataFrame(pd.np.empty((len(year_list),len(data.columns))) * pd.np.nan,columns=data.columns)
    future.Year = list(year_list)
    data = data.append(future,ignore_index=True)
    return data

def gdp_pred(data,k):
    """
    Predict missing values and future values of GDP
    Input:
          data (Pandas DataFrame) - Input DataFrame
          k (integer) - To be used for time-series data
    Returns:
            data (Pandas DataFrame) - Contains original and predicted values of GDP
    """
    ValueError
    from sklearn import linear_model

    #Linear regression
    regr=linear_model.LinearRegression(normalize=True)
    regr.fit(data.Year[3:8].values.reshape(-1,1),data.GDP[3:8])

    a=regr.predict(data.Year[0:3].values.reshape(-1,1))

    #Adding missing values to data
    for i in range(len(a)):
        data['GDP'][i] = a[i]

    column='GDP'

    k_variables=['k'+'%d' %i for i in range(1,k+1)]

    for i in k_variables:
        data[i]=0

    for i in range(0,50):
        if i >= k:
            for j in range(len(k_variables)):
                data[k_variables[j]][i]=data[column][i-j-1]

    if k == 1:
        regr.fit(data[['Year','k1']][0:55],data[column][0:55])
    elif k == 2:
        regr.fit(data[['Year','k1','k2']][0:55],data[column][0:55])
    elif k == 3:
        regr.fit(data[['Year','k1','k2','k3']][0:55],data[column][0:55])
    elif k == 4:
        regr.fit(data[['Year','k1','k2','k3','k4']][0:55],data[column][0:55])
    elif k == 5:
        regr.fit(data[['Year','k1','k2','k3','k4','k5']][0:55],data[column][0:55])
    else:
        raise ValueError('Incorrect value of k')
    #Future prediction of GDP
    for i in range(55,61):
        for j in range(len(k_variables)):
            data[k_variables[j]][i]=data[column][i-j-1]
        if k == 1:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i]])
        elif k == 2:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i]])
        elif k == 3:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i],data['k3'][i]])
        elif k == 4:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i],data['k3'][i],data['k4'][i]])
        elif k == 5:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i],data['k3'][i],data['k4'][i],data['k5'][i]])
        else:
            raise ValueError('Incorrect value of k')

    #Deleting unwanted columns
    for i in k_variables:
        del data[i]

    return data

def future_pred(data,column,k=1,a=50,b=61):
    """
        Predict missing values and future values of predictor
    Input:
          data (Pandas DataFrame) - Input DataFrame
          column (String) - Column name of predictor
          k (integer) - To be used for time-series data
          a (integer) - Last column index of actual data
          b (integer) - Last column of DataFrame
    Returns:
            data (Pandas DataFrame) - Contains original and predicted values of predictor
    """

    k_variables=['k'+'%d' %i for i in range(1,k+1)]

    for i in k_variables:
        data[i]=0

    for i in range(0,a):
        if i >= k:
            for j in range(len(k_variables)):
                data[k_variables[j]][i]=data[column][i-j-1]
    from sklearn import linear_model
    regr=linear_model.LinearRegression(normalize=True)

    if k == 1:
        regr.fit(data[['Year','k1']][0:a],data[column][0:a])
    elif k == 2:
        regr.fit(data[['Year','k1','k2']][0:a],data[column][0:a])
    elif k == 3:
        regr.fit(data[['Year','k1','k2','k3']][0:a],data[column][0:a])
    elif k == 4:
        regr.fit(data[['Year','k1','k2','k3','k4']][0:a],data[column][0:a])
    elif k == 5:
        regr.fit(data[['Year','k1','k2','k3','k4','k5']][0:a],data[column][0:a])
    else:
        raise ValueError('Incorrect value of k')

    #Future prediction
    for i in range(a,b):
        for j in range(len(k_variables)):
            data[k_variables[j]][i]=data[column][i-j-1]
        if k == 1:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i]])
        elif k == 2:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i]])
        elif k == 3:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i],data['k3'][i]])
        elif k == 4:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i],data['k3'][i],data['k4'][i]])
        elif k == 5:
            data[column][i] = regr.predict([data['Year'][i],data['k1'][i],data['k2'][i],data['k3'][i],data['k4'][i],data['k5'][i]])
        else:
            raise ValueError('Incorrect value of k')

    #Deleting unwanted columns
    for i in k_variables:
        del data[i]

    return data

def predict(data):
    """
    Predict missing values and future values of all predictors
    Input:
          data (Pandas DataFrame) - Input DataFrame
    Returns:
            data (Pandas DataFrame) - Contains original and predicted values of all predictors
    """
    data=future_df(data,range(2017,2021))
    data=gdp_pred(data,1)
    data=future_pred(data,'EMFDB',1)
    data=future_pred(data,'CLPRB',1)
    data=future_pred(data,'ENPRP',1)
    data=future_pred(data,'NGMPB',1)
    data=future_pred(data,'PAPRB',k=1)
    data=future_pred(data,'PCP',k=5,a=57)
    data=future_pred(data,'ZNDX',k=5,a=57)
    data=future_pred(data,'Nominal Price',k=1,a=56)
    data=future_pred(data,'Inflation Adjusted Price',k=1,a=56)
    return data

def predict_all():
    """
    Wrapping function
    Input:
          name (String) - Name of input CSV file
    Returns:
            Nan
    """
    #Removed CSVs of 3 CSV files due to insufficient data
    os.remove('Data/Cleaned Data/AK.csv')
    os.remove('Data/Cleaned Data/DC.csv')
    os.remove('Data/Cleaned Data/HI.csv')
    statelist = os.listdir('Data/Cleaned Data/')
    for state in statelist:
        data=pd.read_csv('Data/Cleaned Data/'+state)
        data=predict(data)
        data.to_csv('Data/Cleaned Data/'+state)
    return
