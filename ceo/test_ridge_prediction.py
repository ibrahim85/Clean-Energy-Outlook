from ceo import ridge_prediction as rp
import ceo
import os
import os.path as op
import pandas as pd
import inspect

data_path = op.join(ceo.__path__[0], 'Data')
data_path = op.join(data_path, 'Cleaned Data')

def test_pred_nuclear():
    data = pd.read_csv(op.join(data_path, 'CA.csv'))
    pred = rp.pred_nuclear(data)
    assert all(pred['NUETP'][-6:] != None), 'pred_nuclear incorrect'
    data = pd.read_csv(op.join(data_path, 'WA.csv'))
    pred = rp.pred_nuclear(data)
    assert all(pred['NUETP'][-6:] >= 0), 'pred_nuclear incorrect'
    return

def test_pred_solar():
    data = pd.read_csv(op.join(data_path, 'CA.csv'))
    pred = rp.pred_solar(data)
    assert all(pred['SOEGP'][-6:] != None), 'pred_solar incorrect'
    data = pd.read_csv(op.join(data_path, 'AZ.csv'))
    pred = rp.pred_solar(data)
    assert all(pred['SOEGP'][-6:] >= 0), 'pred_solar incorrect'
    return

def test_pred_wind():
    data = pd.read_csv(op.join(data_path, 'NY.csv'))
    pred = rp.pred_wind(data)
    assert all(pred['WYTCP'][-6:] != None), 'pred_wind incorrect'
    data = pd.read_csv(op.join(data_path, 'TX.csv'))
    pred = rp.pred_wind(data)
    assert all(pred['WYTCP'][-6:] >= 0), 'pred_wind incorrect'
    return

def test_pred_hydro():
    data = pd.read_csv(op.join(data_path, 'OR.csv'))
    pred = rp.pred_hydro(data)
    assert all(pred['HYTCP'][-6:] != None), 'pred_hydro incorrect'
    data = pd.read_csv(op.join(data_path, 'IL.csv'))
    pred = rp.pred_hydro(data)
    assert all(pred['HYTCP'][-6:] >= 0), 'pred_hydro incorrect'
    return

def test_ridge_predict_all():
    rp.ridge_predict_all()
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_predict = op.join(path, 'Predicted Data')
    path_predict = op.join(path_predict, 'Ridge Regression')
    statelist = os.listdir(path_predict)
    for i in statelist:
        pred = pd.read_csv(path_predict+'\\%s' %i)
        assert all(pred['NUETP'][-6:] != None), 'pred_nuclear incorrect'
        assert all(pred['NUETP'][-6:] >= 0), 'pred_nuclear incorrect'
        assert all(pred['SOEGP'][-6:] != None), 'pred_solar incorrect'
        assert all(pred['SOEGP'][-6:] >= 0), 'pred_solar incorrect'
        assert all(pred['WYTCP'][-6:] != None), 'pred_wind incorrect'
        assert all(pred['WYTCP'][-6:] >= 0), 'pred_wind incorrect'
        assert all(pred['HYTCP'][-6:] != None), 'pred_hydro incorrect'
        assert all(pred['HYTCP'][-6:] >= 0), 'pred_hydro incorrect'
    return
