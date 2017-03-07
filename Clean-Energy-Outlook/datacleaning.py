import pandas as pd
import numpy as np
import xlrd

def data_extract(df,state,param_list):
    datalist=[]
    dftemp=df[df['MSN'].isin(["Year"] + param_list) & (df.State==state)]
    del dftemp['Data_Status']
    del dftemp['State']
    del dftemp['MSN']
    dftemp=dftemp.T
    dftemp.columns=param_list
    datalist.append(dftemp)
    #datalist.to_csv('Data/Data_States/%s.csv'% (statelist[i]), encoding='utf-8', index=True)
    return datalist

def data_extract_all(df,state_list,param_list):
    for i in state_list:
        data=data_extract(df,'CA',param_list)
        data[0].to_csv('Data/Data_States/%s.csv'%i, encoding='utf-8', index=True)
    return

def add_clprb(state_list):
    for j in range(52):
        dftemp = pd.read_csv('Data/Data_States/%s.csv' % (state_list[j]))
        dftemp.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        dftemp['CLPRB']=None
        if j==44:  #for state US, missing data of GDP
            continue
        #else: dftemp.drop(dftemp.index[55],inplace=True) #delete last line of GDP
        data = xlrd.open_workbook('Data/Original Data/more MSN/CLPRB.xlsx') # open xlsx file
        table = data.sheets()[j] # open sheet j
        nrows = table.nrows # get how many lines
        for i in range(1,nrows): #cycle in the table
            dftemp['CLPRB'][i-1] = table.row_values(i)[3] # columns 4
        dftemp.to_csv('Data/Data_States/%s.csv'% (state_list[j]), encoding='utf-8', index=False)
    return

def add_msn(state_list,parameter):
    data=pd.read_excel("Data/Original Data/more MSN/%s.xlsx" %parameter)
    for i in state_list:
        tempdf=data[data.StateCode=='%s'%i]
        del tempdf['MSN']
        del tempdf['StateCode']
        df = pd.read_csv('Data/Data_States/%s.csv' %i)
        df.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        df_r=pd.merge(df, tempdf,on='Year',how='outer')
        df_r.rename(columns={'Data':parameter}, inplace = True)
        df_r.to_csv('Data/Data_States/%s.csv' %i, encoding='utf-8', index=False)
    return
