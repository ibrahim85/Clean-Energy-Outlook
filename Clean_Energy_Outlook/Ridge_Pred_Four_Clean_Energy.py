import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# define year and state lists


def pred_nuclear(data, statelist):
""" predict the nuclear data for all 50 states"""
year1 = data[['Year']][:44]
year2 = data[['Year']][-11:]
year3 = data[['Year']][-6:]
# set 5 years in future for prediction
year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
future = year3
  for i in range(49):
    data = pd.read_csv('%s.csv' % (statelist[i]))

    year1 = data[['Year']][:44]
    #print(year1.shape)
    year2 = data[['Year']][-11:]
    # Split data for train and test
    #print(i)
    all_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['NUETP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    # predict NUETP for future
    #year3 = data[['Year']][-6:]
    #year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
    #print(year3)
    future_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    pred = pd.DataFrame(regr2.predict(future_x))
    pred.columns = [statelist[i]]
    #print(pred)
    future = pd.concat([future, pred], axis=1)
    #print(future)
  print(future)

  # output to csv
  future.to_csv('NuclearPreds.csv', encoding='utf-8', index=False)


def pred_solar(data, statelist):
""" predict the solar energy data for all states"""
year1 = data[['Year']][:44]
year2 = data[['Year']][-11:]
year3 = data[['Year']][-6:]
# set 5 years in future for prediction
year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
future = year3
  for i in range(49):
    data = pd.read_csv('%s.csv' % (statelist[i]))

    year1 = data[['Year']][:44]
    #print(year1.shape)
    year2 = data[['Year']][-11:]
    # Split data for train and test
    #print(i)
    all_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['SOEGP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    # predict SOEGP for future
    #year3 = data[['Year']][-6:]
    #year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
    #print(year3)
    future_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    pred = pd.DataFrame(regr2.predict(future_x))
    pred.columns = [statelist[i]]
    #print(pred)
    future = pd.concat([future, pred], axis=1)
    #print(future)
  print(future)

  # output to csv
  future.to_csv('SolarPreds.csv', encoding='utf-8', index=False)


  def pred_wind(data, statelist):
  """ predict the wind energy data for all states"""
  year1 = data[['Year']][:44]
  year2 = data[['Year']][-11:]
  year3 = data[['Year']][-6:]
  # set 5 years in future for prediction
  year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
  future = year3
    for i in range(49):
    data = pd.read_csv('%s.csv' % (statelist[i]))

    year1 = data[['Year']][:44]
    #print(year1.shape)
    year2 = data[['Year']][-11:]
    # Split data for train and test
    #print(i)
    all_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['WYTCP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    # predict WYTCP for future
    #year3 = data[['Year']][-6:]
    #year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
    #print(year3)
    future_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    pred = pd.DataFrame(regr2.predict(future_x))
    pred.columns = [statelist[i]]
    #print(pred)
    future = pd.concat([future, pred], axis=1)
    #print(future)
  print(future)

  # output to csv
  future.to_csv('WindPreds.csv', encoding='utf-8', index=False)


  def pred_wind(data, statelist):
  """ predict the wind energy data for all states"""
  year1 = data[['Year']][:44]
  year2 = data[['Year']][-11:]
  year3 = data[['Year']][-6:]
  # set 5 years in future for prediction
  year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
  future = year3
    for i in range(49):
    data = pd.read_csv('%s.csv' % (statelist[i]))

    year1 = data[['Year']][:44]
    #print(year1.shape)
    year2 = data[['Year']][-11:]
    # Split data for train and test
    #print(i)
    all_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][0:55]
    all_y = data[['HYTCP']][0:55]
    train_x, test_x, train_y, test_y = train_test_split(all_x, all_y, test_size=0.2)
    regr2 = linear_model.Ridge(alpha = 0.75)
    regr2.fit(train_x, train_y)
    # predict Hydro for future
    #year3 = data[['Year']][-6:]
    #year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])
    #print(year3)
    future_x = data[['GDP','CLPRB','EMFDB','ENPRP','NGMPB','PAPRB','PCP','ZNDX','Nominal Price', 'Inflation Adjusted Price']][-6:]
    pred = pd.DataFrame(regr2.predict(future_x))
    pred.columns = [statelist[i]]
    #print(pred)
    future = pd.concat([future, pred], axis=1)
    #print(future)
  print(future)

  # output to csv
  future.to_csv('HydroPreds.csv', encoding='utf-8', index=False)
