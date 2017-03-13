import pandas as pd
import numpy as np
import xlrd
import ceo
from ceo import data_cleaning as dc
import os
import os.path as op

data_path = op.join(ceo.__path__[0], 'Data')
data_path = op.join(data_path, 'Original Data')

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

def test_clean_all_data():
    """

    """
    return

def test_data_extract():
    """

    """
    data = pd.DataFrame([['a','aa',1,2,3,4,5],['a','bb',6,7,8,9,10],['a','cc',11,12,13,14,15],['b','aa',1,2,3,4,5],['b','bb',6,7,8,9,10],['b','cc',11,12,13,14,15],['c','aa',1,2,3,4,5],['c','bb',6,7,8,9,10],['c','cc',11,12,13,14,15]],columns=['State','MSN',1960,1970,1980,1990,2000])
    result1 = pd.DataFrame([[1960,1,6],[1970,2,7],[1980,3,8],[1990,4,9],[2000,5,10]],columns=['Year','aa','bb'])
    df1 = dc.data_extract(data,'a',['aa','bb'])
    assert all(df1 == result1), 'Data extraction incorrect!'
    try:
        dc.data_extract([[1,2,3]],1,['aa','bb'])
        assert False, 'Error not raised'
    except AssertionError:
        pass
    try:
        dc.data_extract(data,1,['aa','bb'])
        assert False, 'Error not raised'
    except AssertionError:
        pass
    try:
        dc.data_extract(data,'state','aa')
        assert False, 'Error not raised'
    except AssertionError:
        pass
    return

def test_data_extract_all():
    """

    """
    try:
        dc.data_extract_all(data,['a',2],['aa','bb'])
        assert False, 'Error not raised'
    except AssertionError:
        pass
    try:
        dc.data_extract_all(data,['a','b'],[['a'],'bb'])
        assert False, 'Error not raised'
    except AssertionError:
        pass
    os.remove('Data/Cleaned Data with Missing Predictors/a.csv')
    return

def test_add_clprb():
    """

    """
    dc.data_extract_all(df,US_states_missing,['HYTCP'])
    try:
        dc.add_clprb(clprb,US_states_missing)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    return

def test_add_msn():
    """

    """
    try:
        dc.add_msn(ngmpb,US_states_missing,'NGMPB')
        assert False, 'Error not raised'
    except ValueError:
        pass
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"])
    dc.add_msn(paprb,statelist,'PAPRB')
    names = os.listdir('Data/Cleaned Data with Missing Predictors')
    for i in names:
        d = pd.read_csv('Data/Cleaned Data with Missing Predictors/%s' %i)
        assert any('PAPRB' == c for c in d.columns),'Data Cleaning Incorrect'
    return

def test_climate():
    """

    """
    try:
        dc.climate(climate_data,'PCP',US_states_missing)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"])
    dc.add_gdp(gdp1,statelist)
    dc.climate(climate_data,'PCP',statelist)
    names = os.listdir('Data/Cleaned Data/')
    for i in names:
        d = pd.read_csv('Data/Cleaned Data/%s' %i)
        assert any('PCP' == c for c in d.columns),'Data Cleaning Incorrect'
    return

def test_oil_price():
    """

    """
    try:
        dc.oil_price(oil,US_states_missing)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"])
    dc.add_gdp(gdp1,statelist)
    dc.oil_price(oil,statelist)
    names = os.listdir('Data/Cleaned Data/')
    for i in names:
        d = pd.read_csv('Data/Cleaned Data/%s' %i)
        assert any('Inflation Adjusted Price' == c for c in d.columns),'Data Cleaning Incorrect'
    return

def test_add_gdp():
    """

    """
    try:
        dc.add_gdp(gdp1,US_states_missing)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"])
    dc.add_gdp(gdp1,statelist)
    names = os.listdir('Data/Cleaned Data/')
    for i in names:
        d = pd.read_csv('Data/Cleaned Data/%s' %i)
        assert any('GDP' == c for c in d.columns),'Data Cleaning Incorrect'
    return
