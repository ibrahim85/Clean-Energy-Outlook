from ceo import missing_data as md
import ceo
import os
import os.path as op
import pandas as pd
import numpy as np
import inspect

data_path = op.join(ceo.__path__[0], 'Data')
data_path = op.join(data_path, 'Cleaned Data')
data = pd.read_csv(op.join(data_path, 'CA.csv'))

def test_future_df():
    """
    Function to test future_df
    Input:
          None
    Returns:
            None
    """
    data = pd.read_csv(op.join(data_path, 'CA.csv'))
    data1=md.future_df(data,[1,2,3,4,5])
    assert len(data1) == len(data) + 5, 'Rows not added'
    return

def test_gdp_pred():
    """
    Function to test gdp_pred
    Input:
          None
    Returns:
            None
    """
    data = pd.read_csv(op.join(data_path, 'WA.csv'))
    data1 = md.future_df(data,range(2017,2021))
    try:
        data1 = md.gdp_pred(data1,0)
        assert False, ('k not handled')
    except ValueError:
        pass
    return

def test_future_pred():
    """
    Function to test future_pred
    Input:
          None
    Returns:
            None
    """
    data = pd.read_csv(op.join(data_path, 'NY.csv'))
    try:
        data=md.future_pred(data,'EMFDB',0)
        assert False, ('k not handled')
    except ValueError:
        pass
    return

def test_predict():
    """
    Function to test predict
    Input:
          None
    Returns:
            None
    """
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_clean = op.join(path, 'Cleaned Data with Missing Predictors')
    path = op.join(path_clean,'CA.csv')
    data=pd.read_csv(path)
    pred = md.predict(data)
    assert all(pred['ENPRP'][-6:] != None), 'predict incorrect'
    assert all(pred['PAPRB'][-6:] >= 0), 'predict incorrect'
    assert all(pred['PCP'][-6:] != None), 'predict incorrect'
    assert all(pred['Inflation Adjusted Price'][-6:] >= 0), 'predict incorrect'

    return

def test_predict_all():
    """
    Function to test predict_all
    Input:
          None
    Returns:
            None
    """
    md.predict_all()
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_clean = op.join(path, 'Cleaned Data')
    statelist = os.listdir(path_clean)
    for state in statelist:
        path = op.join(path_clean,state)
        pred=pd.read_csv(path)
        assert all(pred['EMFDB'][-6:] != None), 'predict_all incorrect'
        assert all(pred['CLPRB'][-6:] >= 0), 'predict_all incorrect'
        assert all(pred['NGMPB'][-6:] != None), 'predict_all incorrect'
        assert all(pred['Nominal Price'][-6:] >= 0), 'predict_all incorrect'
    return
