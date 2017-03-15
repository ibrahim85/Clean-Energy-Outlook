import sklearn
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.svm import SVR
import pandas as pd
import os
import os.path as op
import inspect
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def read_data(file_name):
    """
    Function to read a csv file
    Input:
          file_name: Name of the CSV file
    Returns:
           Pandas DataFrame
    """

    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_clean = op.join(path, 'Cleaned Data')
    path = op.join(path_clean, 'file_name')
    names = os.listdir(path_clean)
    if all(file_name != i for i in names):
        raise ValueError
    return pd.read_csv(path)

def preprocess(data):
    """
    Function for preprocessing columns
    Input:
          data (Pandas DataFrame)
    Returns:
            data (Pandas DataFrame) : Contains scaled columns of predictors
    """
    # Data Preprocessing
    data['GDP_scaled']=preprocessing.scale(data['GDP'])
    data['CLPRB_scaled']=preprocessing.scale(data['CLPRB'])
    data['EMFDB_scaled']=preprocessing.scale(data['EMFDB'])
    data['ENPRP_scaled']=preprocessing.scale(data['ENPRP'])
    data['NGMPB_scaled']=preprocessing.scale(data['NGMPB'])
    data['PAPRB_scaled']=preprocessing.scale(data['PAPRB'])
    data['PCP_scaled']=preprocessing.scale(data['PCP'])
    data['ZNDX_scaled']=preprocessing.scale(data['ZNDX'])
    data['OP_scaled']=preprocessing.scale(data['Nominal Price'])
    data['OP2_scaled']=preprocessing.scale(data['Inflation Adjusted Price'])

    return data

def split_data(data,param):
    """
    Function to split data for training and testing
    Input:
          data (Pandas DataFrame)
    Returns:
            X_train (list): Training set of predictors
            X_test (list): Training set of predictors
            y_train (list): Training set of energy
            y_test (list): Testing set of energy
    """
    all_x = data[['GDP_scaled','CLPRB_scaled','EMFDB_scaled','ENPRP_scaled','NGMPB_scaled','PAPRB_scaled','PCP_scaled','ZNDX_scaled','OP_scaled', 'OP2_scaled']][:55]
    all_y = data[[param]][:55]
    return cross_validation.train_test_split(all_x, all_y, test_size=0.2, random_state=0)

def SVR_predict(data, X_train, X_test, y_train, y_test, param):
    """
    Function to predict future values of parameter
    Input:
          data (Pandas DataFrame): original data
          X_train (list): Training set of predictors
          X_test (list): Training set of predictors
          y_train (list): Training set of energy
          y_test (list): Testing set of energy

    Returns:
            data (Pandas DataFrame): original data + future values
    """
    if param == 'NUETP' or param == 'SOEGP':
        kernel_name = 'sigmoid'
        c_value = 90.0
    elif param == 'HYTCP' or param == 'WYTCP':
        kernel_name = 'linear'
        c_value = 1000
    else:
        raise ValueError('Incorrect parameter name')
    clf = SVR(kernel=kernel_name, C=c_value, epsilon=0.3).fit(X_train, y_train)
    future_x = data[['GDP_scaled','CLPRB_scaled','EMFDB_scaled','ENPRP_scaled','NGMPB_scaled','PAPRB_scaled','PCP_scaled','ZNDX_scaled','OP_scaled','OP2_scaled']][-6:]
    pred = pd.DataFrame(clf.predict(future_x))
    for i in range(6):
        if pred[0][i] < 0:
            pred[0][i] = 0
    data[param][-6:] = pred[0]
    return data

def SVR_predict_all():
    """
    Wrapping function for SVR
    Inputs:
           None
    Returns:
            None
    """
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    path_clean = op.join(path, 'Cleaned Data')
    path_predict = op.join(path, 'Predicted Data')
    path_predict = op.join(path_predict, 'SVR')
    statelist = os.listdir(path_clean)
    if not os.path.exists(path_predict):
        os.makedirs(path_predict)
    for state in statelist:
        data = read_data(state)
        data = preprocess(data)
        X_train, X_test, y_train, y_test = split_data(data,'NUETP')
        data = SVR_predict(data,X_train, X_test, y_train, y_test,'NUETP')
        X_train, X_test, y_train, y_test = split_data(data,'SOEGP')
        data = SVR_predict(data,X_train, X_test, y_train, y_test,'SOEGP')
        X_train, X_test, y_train, y_test = split_data(data,'HYTCP')
        data = SVR_predict(data,X_train, X_test, y_train, y_test,'HYTCP')
        X_train, X_test, y_train, y_test = split_data(data,'WYTCP')
        data = SVR_predict(data,X_train, X_test, y_train, y_test,'WYTCP')
        data.drop(['GDP_scaled','CLPRB_scaled','EMFDB_scaled','ENPRP_scaled','NGMPB_scaled','PAPRB_scaled','PCP_scaled','ZNDX_scaled','OP_scaled','OP2_scaled'],inplace=True,axis=1)
        data.to_csv(path_predict+'\\%s'%state, encoding='utf-8', index=False)
    return
