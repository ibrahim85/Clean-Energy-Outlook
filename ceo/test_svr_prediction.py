from ceo import svr_prediction as sp
import ceo
import os
import os.path as op
import pandas as pd
import inspect

data_path = op.join(ceo.__path__[0], 'Data')
data_path = op.join(data_path, 'Cleaned Data')

def test_read_data():
    """
    Function to test read_data
    Input:
          None
    Returns:
            None
    """
    state = 'abc.csv'
    try:
        data = sp.read_data(state)
        assert False, 'Error'
    except ValueError:
        pass
    return

def test_preprocess():
    """
    Function to test preprocess
    Input:
          None
    Returns:
            None
    """
    data = pd.read_csv(op.join(data_path, 'CA.csv'))
    pred = sp.preprocess(data)
    #Checking column names for specific strings
    assert any('GDP_scaled' == i for i in pred.columns), 'Error'
    assert any('OP2_scaled' == i for i in pred.columns), 'Error'
    assert any('ZNDX_scaled' == i for i in pred.columns), 'Error'
    assert any('PAPRB_scaled' == i for i in pred.columns), 'Error'
    assert any('EMFDB_scaled' == i for i in pred.columns), 'Error'
    return

def test_SVR_predict():
    """
    Function to test SVR_predict
    Input:
          None
    Returns:
            None
    """
    data = pd.read_csv(op.join(data_path, 'CA.csv'))
    data = sp.preprocess(data)
    X_train, X_test, y_train, y_test = sp.split_data(data,'NUETP')
    data = sp.SVR_predict(data,X_train, X_test, y_train, y_test,'NUETP')
    #Checking last 6 items of NUETP is None
    assert all(data['NUETP'][-6:] != None), 'Error'
    return

def test_SVR_predict_all():
    """
    Function to test SVR_predict_all
    Input:
          None
    Returns:
            None
    """
    sp.SVR_predict_all()
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_predict = op.join(path, 'Predicted Data')
    path_predict = op.join(path_predict, 'SVR')
    #Path of SVR results
    statelist = os.listdir(path_predict)
    for state in statelist:
        path = op.join(path_predict,state)
        data = pd.read_csv(path)
        #Checking last 6 items is None
        assert all(data['NUETP'][-6:] != None), 'Error'
        assert all(data['NUETP'][-6:] != None), 'Error'
        assert all(data['NUETP'][-6:] != None), 'Error'
        assert all(data['NUETP'][-6:] != None), 'Error'
    return
