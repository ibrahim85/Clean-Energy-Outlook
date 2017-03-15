import pandas as pd
import numpy as np
import xlrd
import ceo
from ceo import data_cleaning as dc
import os
import os.path as op
import inspect
#Location for Original Data
data_path = op.join(ceo.__path__[0], 'Data')
data_path = op.join(data_path, 'Original Data')
#Input data
df = pd.read_excel(op.join(data_path, 'State Energy Data System.xlsx'),sheetname=3)
gdp1=pd.read_csv(op.join(data_path, 'GDP.csv'),skiprows=4,index_col=1)
climate_data = pd.read_csv(op.join(data_path, 'climate_annual.txt'),sep = ' ',encoding = 'utf-8')
oil = pd.read_excel(op.join(data_path, 'Annual Average Crude Oil Price.xlsx'),skiprows=4)
clprb = xlrd.open_workbook(op.join(data_path, 'CLPRB.xlsx'))
emfdb=pd.read_excel(op.join(data_path, 'EMFDB.xlsx'))
enprp=pd.read_excel(op.join(data_path, 'ENPRP.xlsx'))
ngmpb=pd.read_excel(op.join(data_path, 'NGMPB.xlsx'))
paprb=pd.read_excel(op.join(data_path, 'PAPRB.xlsx'))
data = pd.DataFrame([['a','aa',1,2,3,4,5],['a','bb',6,7,8,9,10],['a','cc',11,12,13,14,15],['b','aa',1,2,3,4,5],['b','bb',6,7,8,9,10],['b','cc',11,12,13,14,15],['c','aa',1,2,3,4,5],['c','bb',6,7,8,9,10],['c','cc',11,12,13,14,15]],columns=['State','MSN',1960,1970,1980,1990,2000])
US_states_missing = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","VT","VA","WA","WV","WI"]

def test_data_extract():
    """
    Function to test data_extract
    Input:
          None
    Returns:
            None
    """
    data = pd.DataFrame([['a','aa',1,2,3,4,5],['a','bb',6,7,8,9,10],['a','cc',11,12,13,14,15],['b','aa',1,2,3,4,5],['b','bb',6,7,8,9,10],['b','cc',11,12,13,14,15],['c','aa',1,2,3,4,5],['c','bb',6,7,8,9,10],['c','cc',11,12,13,14,15]],columns=['State','MSN',1960,1970,1980,1990,2000])
    result1 = pd.DataFrame([[1960,1,6],[1970,2,7],[1980,3,8],[1990,4,9],[2000,5,10]],columns=['Year','aa','bb'])
    df1 = dc.data_extract(data,'a',['aa','bb'])
    assert all(df1 == result1), 'Data extraction incorrect!'
    try:
        dc.data_extract([[1,2,3]],1,['aa','bb'])
        assert False, 'Error not raised'
    except TypeError:
        pass
    try:
        dc.data_extract(data,1,['aa','bb'])
        assert False, 'Error not raised'
    except TypeError:
        pass
    try:
        dc.data_extract(data,'state','aa')
        assert False, 'Error not raised'
    except TypeError:
        pass
    return

def test_data_extract_all():
    """
    Function to test data_extract_all
    Input:
          None
    Returns:
            None
    """
    #Location of Test Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_test = op.join(path, 'Test Data')
    if not os.path.exists(path_test):
        os.makedirs(path_test)
    try:
        dc.data_extract_all(data,['a',2],['aa','bb'],path_test)
        assert False, 'Error not raised'
    except TypeError:
        pass
    try:
        dc.data_extract_all(data,['a','b'],[['a'],'bb'],path_test)
        assert False, 'Error not raised'
    except TypeError:
        pass
    names = os.listdir(path_test)
    #Removing creating csv files
    for i in names:
        os.remove(path_test+'\\%s'%i)
    return

def test_add_clprb():
    """
    Function to test add_clprb
    Input:
          None
    Returns:
            None
    """
    #Location of Test Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_test = op.join(path, 'Test Data')
    if not os.path.exists(path_test):
        os.makedirs(path_test)
    dc.data_extract_all(df,US_states_missing,['HYTCP'],path_test)
    try:
        dc.add_clprb(clprb,US_states_missing,path_test)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    names = os.listdir(path_test)
    #Removing creating csv files
    for i in names:
        os.remove(path_test+'\\%s'%i)
    return

def test_add_msn():
    """
    Function to test add_msn
    Input:
          None
    Returns:
            None
    """
    #Location of Test Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_test = op.join(path, 'Test Data')
    if not os.path.exists(path_test):
        os.makedirs(path_test)
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    #Extracting data, adding MSN
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"],path_test)
    dc.add_msn(paprb,statelist,'PAPRB',path_test)
    names = os.listdir(path_test)
    for i in names:
        d = pd.read_csv(path_test+'\\%s' %i)
        assert any('PAPRB' == c for c in d.columns),'Data Cleaning Incorrect'
    names = os.listdir(path_test)
    #Removing creating csv files
    for i in names:
        os.remove(path_test+'\\%s'%i)
    return

def test_climate():
    """
    Function to test climate
    Input:
          None
    Returns:
            None
    """
    #Location of Test Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_test = op.join(path, 'Test Data')
    if not os.path.exists(path_test):
        os.makedirs(path_test)
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    #Extracting data, adding GDP and Climate data
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"],path_test)
    dc.add_gdp(gdp1,statelist,path_test)
    dc.climate(climate_data,'PCP',statelist,path_test)
    names = os.listdir(path_test)
    for i in names:
        d = pd.read_csv(path_test+'\\%s' %i)
        assert any('PCP' == c for c in d.columns),'Data Cleaning Incorrect'
    names = os.listdir(path_test)
    #Removing creating csv files
    for i in names:
        os.remove(path_test+'\\%s'%i)
    return

def test_oil_price():
    """
    Function to test oil_price
    Input:
          None
    Returns:
            None
    """
    #Location of Test Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_test = op.join(path, 'Test Data')
    if not os.path.exists(path_test):
        os.makedirs(path_test)
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    #Extracting data, adding GDP and Oil Price
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"],path_test)
    dc.add_gdp(gdp1,statelist,path_test)
    dc.oil_price(oil,statelist,path_test)
    names = os.listdir(path_test)
    for i in names:
        d = pd.read_csv(path_test+'\\%s' %i)
        #Checking column 'Inflation Adjusted Price' present in CSV
        assert any('Inflation Adjusted Price' == c for c in d.columns),'Data Cleaning Incorrect'
    names = os.listdir(path_test)
    #Removing creating csv files
    for i in names:
        os.remove(path_test+'\\%s'%i)
    return

def test_add_gdp():
    """
    Function to test add_gdp
    Input:
          None
    Returns:
            None
    """
    #Location of Test Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_test = op.join(path, 'Test Data')
    if not os.path.exists(path_test):
        os.makedirs(path_test)
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    #Extracting data, adding GDP
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"],path_test)
    dc.add_gdp(gdp1,statelist,path_test)
    names = os.listdir(path_test)
    for i in names:
        d = pd.read_csv(path_test+'\\%s' %i)
        #Checking column 'GDP' present in CSV
        assert any('GDP' == c for c in d.columns),'Data Cleaning Incorrect'
    names = os.listdir(path_test)
    #Removing creating csv files
    for i in names:
        os.remove(path_test+'\\%s'%i)
    return

def test_clean_all_data():
    """
    Function to test clean_all_data
    Input:
          None
    Returns:
            None
    """
    dc.clean_all_data()
    #Location of Missing Data
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_clean = op.join(path, 'Cleaned Data with Missing Predictors')
    states = os.listdir(path_clean)
    for i in states:
        path_csv = op.join(path_clean,i)
        pred = pd.read_csv(path_csv)
        #Checking column name in CSV
        assert any('EMFDB' == pred.columns), 'predict_all incorrect'
        assert any('HYTCP' == pred.columns), 'predict_all incorrect'
        assert any('NGMPB' == pred.columns), 'predict_all incorrect'
        assert any('PCP' == pred.columns), 'predict_all incorrect'
    return
