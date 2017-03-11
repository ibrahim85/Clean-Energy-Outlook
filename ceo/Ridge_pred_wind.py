# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# define the function to predict wind data in the future
def pred_wind(samplefile, filelist):
  # read data
  data = pd.read_csv(samplefile)
  year1 = data[['Year']][:44]
  #print(year1.shape)
  year2 = data[['Year']][-11:]

  # predict wind energy for future
  year3 = year2 = data[['Year']][-6:]
  year3 = year3.set_index([[0, 1, 2, 3, 4, 5]])

  #statelist=["AK","AL","AR","AZ","CA","CO","CT","DE","FL","GA","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]
  #print(len(statelist))

  future = year3
  # do ridge regression on train data

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
