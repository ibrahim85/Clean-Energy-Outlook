from ceo import predictor as pr
import ceo
import os
import os.path as op
import pandas as pd
import numpy as np

data_path = op.join(ceo.__path__[0], 'Data')
data_path = op.join(data_path, 'Cleaned Data')
data = pd.read_csv(op.join(data_path, 'CA.csv'))

def test_future_df():
    data = pd.read_csv(op.join(data_path, 'CA.csv'))
    data1=pr.future_df(data,[1,2,3,4,5])
    assert len(data1) == len(data) + 5, 'Rows not added'
    return

def test_gdp_pred():
    #data1=gdp_pred(data,1)
    data = pd.read_csv(op.join(data_path, 'WA.csv'))
    data1 = pr.future_df(data,range(2017,2021))
    try:
        data1 = pr.gdp_pred(data1,0)
        assert False, ('k not handled')
    except ValueError:
        pass
    return

def test_future_pred():
    data = pd.read_csv(op.join(data_path, 'NY.csv'))
    try:
        data=pr.future_pred(data,'EMFDB',0)
        assert False, ('k not handled')
    except ValueError:
        pass
    return
