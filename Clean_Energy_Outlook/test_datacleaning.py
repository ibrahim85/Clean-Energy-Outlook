import pandas as pd
import numpy as np
import xlrd
import datacleaning as dc

def test_data_extract():
    data = pd.DataFrame([['a','aa',1,2,3,4,5],['a','bb',6,7,8,9,10],['a','cc',11,12,13,14,15],['b','aa',1,2,3,4,5],['b','bb',6,7,8,9,10],['b','cc',11,12,13,14,15],['c','aa',1,2,3,4,5],['c','bb',6,7,8,9,10],['c','cc',11,12,13,14,15]],columns=['State','MSN',1960,1970,1980,1990,2000])
    result1 = pd.DataFrame([[1,6],[2,7],[3,8],[4,9],[5,10]],[1960,1970,1980,1990,2000],['aa','bb'])
    df = dc.data_extract(data,'a',['aa','bb'])
    #result2 =
    assert all(df == result1), 'Data extraction incorrect!'
    return

def test_data_extract_all():
    return

def test_add_clprb():
    return

def test_add_msn():
    return

def test_climate():
    return

def test_oil_price():
    return

def test_add_gdp():
    return

def test_clean_all_data():
    return
