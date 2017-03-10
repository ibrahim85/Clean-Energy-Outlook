# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# define a function that write separate prediction results to original data files
def add_pred(hydrofile, nuclearfile, windfile, solarfile)
  statelist=["AK","AL","AR","AZ","CA","CO","CT","DE","FL","GA","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]
  print(len(statelist))
  # Read prediction data
  hydro = pd.read_csv(hydrofile)
  nuclear = pd.read_csv(nuclearfile)
  wind = pd.read_csv(windfile)
  solar = pd.read_csv(solarfile)
  #ca = pd.read_csv("CA.csv")
  #print(hydro)
  #print(ca)
  for i in range(49):
      #i=1
      data = pd.read_csv('%s.csv' % (statelist[i]))
      #print(data)
      data['HYTCP'][55:61] = hydro[statelist[i]]
      data['NUETP'][55:61] = nuclear[statelist[i]]
      data['WYTCP'][55:61] = wind[statelist[i]]
      data['SOEGP'][55:61] = solar[statelist[i]]
      #print(data)
      data.to_csv('%s.csv'% (statelist[i]), encoding='utf-8', index=False)
