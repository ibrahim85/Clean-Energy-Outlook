import pandas as pd
import numpy as np
import xlrd
import datacleaning as dc
import os

data = pd.DataFrame([['a','aa',1,2,3,4,5],['a','bb',6,7,8,9,10],['a','cc',11,12,13,14,15],['b','aa',1,2,3,4,5],['b','bb',6,7,8,9,10],['b','cc',11,12,13,14,15],['c','aa',1,2,3,4,5],['c','bb',6,7,8,9,10],['c','cc',11,12,13,14,15]],columns=['State','MSN',1960,1970,1980,1990,2000])
df = pd.read_excel("Data/Original Data/State Energy Data System.xlsx",sheetname=3)
gdp1=pd.read_csv('Data/Original Data/GDP.csv',skiprows=4,index_col=1)
oil = pd.read_excel("Data/Original Data/Annual Average Crude Oil Price.xlsx",skiprows=4)
climate_data =  pd.read_csv('Data/Original Data/climate_annual.txt',sep = ' ',encoding = 'utf-8')
US_states = ["AL","AK","AZ","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","VT","VA","WA","WV","WI"]

def test_clean_all_data():
    """

    """
    dc.clean_all_data()
    names = os.listdir('Data/Cleaned Data/')
    for i in names:
        df = pd.read_csv('Data/Cleaned Data/%s' %i)
        assert all([any('HYTCP' == c for c in df.columns), any('WYTCP' == c for c in df.columns)]),'Data Cleaning Incorrect'
        assert any('GDP' == c for c in df.columns),'Data Cleaning Incorrect'
        assert all([any('EMFDB' == c for c in df.columns), any('NGMPB' == c for c in df.columns)]),'Data Cleaning Incorrect'
        assert any('ZNDX' == c for c in df.columns),'Data Cleaning Incorrect'
        assert any('Nominal Price' == c for c in df.columns),'Data Cleaning Incorrect'
    return

def test_data_extract():
    """

    """
    result1 = pd.DataFrame([[1,6],[2,7],[3,8],[4,9],[5,10]],[1960,1970,1980,1990,2000],['aa','bb'])
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
    try:
        dc.data_extract_all(df,US_states,["HYTCP","WYTCP","SOEGP","NUETP"])
        assert False, 'Error not raised'
    except AssertionError:
        pass
    return

def test_add_clprb():
    """

    """
    try:
        dc.add_clprb(US_states)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    return

def test_add_msn():
    """

    """
    try:
        dc.add_msn(US_states,'NGMPB')
        assert False, 'Error not raised'
    except AssertionError:
        pass
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    dc.data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"])
    dc.add_msn(statelist,'PAPRB')
    names = os.listdir('Data/Cleaned Data/')
    for i in names:
        d = pd.read_csv('Data/Cleaned Data/%s' %i)
        assert any('PAPRB' == c for c in d.columns),'Data Cleaning Incorrect'
    return

def test_climate():
    """

    """
    try:
        climate_data = pd.read_csv('Data/Original Data/climate_annual.txt',sep = ' ',encoding = 'utf-8')
        dc.climate(climate_data,'PCP',US_states)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    climate_data = pd.read_csv('Data/Original Data/climate_annual.txt',sep = ' ',encoding = 'utf-8')
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
        dc.oil_price(oil,US_states)
        assert False, 'Error not raised'
    except AssertionError:
        pass
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    climate_data = pd.read_csv('Data/Original Data/climate_annual.txt',sep = ' ',encoding = 'utf-8')
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
        dc.add_gdp(gdp1,US_states)
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
