import pandas as pd
import numpy as np
import xlrd
import os
import os.path as op
import inspect
pd.options.mode.chained_assignment = None
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def data_extract(df,state,param_list):
    """
    Extracts data of the input state with the input parameters
    Input:
          df (Pandas DataFrame) - Input DataFrame
          state (str) - Initials of the state (like CA, WA, TX)
          param_list (List of str) - Column names to extract
    Returns:
            datalist[0] (Pandas DataFrame) - Extracted DataFrame
    """
    if type(df) == pd.DataFrame and type(state) == str and type(param_list) == list:
        pass
    else:
        raise TypeError
    datalist=[]
    dftemp=df[df['MSN'].isin(["Year"] + param_list) & (df.State==state)]
    if any(df.columns == 'Data_Status'):
        del dftemp['Data_Status']
    if any(df.columns == 'State'):
        del dftemp['State']
    if any(df.columns == 'MSN'):
        del dftemp['MSN']
    dftemp=dftemp.T
    dftemp.columns=param_list
    dftemp.reset_index(inplace=True)
    dftemp.rename(columns={'index':'Year'},inplace=True)
    datalist.append(dftemp)
    return datalist[0]

def data_extract_all(df,state_list,param_list,path_miss):
    """
    Extracts data of all the input states with the input parameters
    Input:
          df (Pandas DataFrame) - Input DataFrame
          state_list (List of str) - List of initials of the state (like CA, WA, TX)
          param_list (List of str) - Column names to extract
    Returns:
            None
    """
    if type(df) == pd.DataFrame and type(state_list) == list and type(param_list) == list and all(isinstance(x, str) for x in param_list):
        pass
    else:
        raise TypeError
    for state in state_list:
        data=data_extract(df,state,param_list)
        data.to_csv(path_miss+'\\%s.csv'%state, encoding='utf-8', index=False)
    return

def add_clprb(data,state_list,path_miss):
    """
    Extracts data from the CLPRB data set and adds it the CSV files of all the input states
    Input:
          data (Pandas DataFrame) - Input CLPRB DataFrame
          state_list (List of str) - List of initials of the state (like CA, WA, TX)
    Returns:
            None
    """
    for j in state_list:
        dftemp = pd.read_csv(path_miss+'\\%s.csv' %j)
        dftemp.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        dftemp['CLPRB']=None
        table = data.sheet_by_name(j) # open sheet j
        nrows = table.nrows # get how many lines
        for i in range(1,nrows): #cycle in the table
            dftemp['CLPRB'][i-1] = table.row_values(i)[3] # columns 4
        dftemp.to_csv(path_miss+'\\%s.csv'%j, encoding='utf-8', index=False)
    names = os.listdir(path_miss)
    assert len(names) == len(state_list), 'Add CLPRB Error'
    return

def add_msn(data,state_list,parameter,path_miss):
    """
    Extracts data from the input data set and adds it the CSV files of all the input states
    Input:
          data (Pandas DataFrame) - Input DataFrame
          state_list (List of str) - List of initials of the state (like CA, WA, TX)
          parameter (List of str) - Column name to extract
    Returns:
            None
    """
    for i in state_list:
        tempdf=data[data.StateCode=='%s'%i]
        del tempdf['MSN']
        del tempdf['StateCode']
        df = pd.read_csv(path_miss+'\\%s.csv' %i)
        df.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        df_r=pd.merge(df, tempdf,on='Year',how='outer')
        df_r.rename(columns={'Data':parameter}, inplace = True)
        df_r.to_csv(path_miss+'\\%s.csv' %i, encoding='utf-8', index=False)
    return

def climate(data,param,statelist,path_miss):
    """
    Extracts climate data from the data set and adds it the CSV files of all the input states
    Input:
          data (Pandas DataFrame) - Input DataFrame
          state_list (List of str) - List of initials of the state (like CA, WA, TX)
          param (str) - Column name
    Returns:
            None
    """
    statesdic = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
    for i in statelist:
        dforigin = pd.read_csv(path_miss+'\\%s.csv' %i)
        dfstate=data[data.State==statesdic[i]]
        dftoadd=dfstate[['Year',param]]
        dfnew=pd.merge(dforigin, dftoadd,on='Year',how='outer')
        dfnew.to_csv(path_miss+'\\%s.csv'%i, encoding='utf-8', index=False)
    return

def oil_price(oil_data,statelist,path_miss):
    """
    Extracts data from the oil data set and adds it the CSV files of all the input states
    Input:
          oil_data (Pandas DataFrame) - Input DataFrame
          statelist (List of str) - List of initials of the state (like CA, WA, TX)
    Returns:
            None
    """
    oiltoadd=oil_data[14:-1]
    for i in statelist:
        dforigin = pd.read_csv(path_miss+'\\%s.csv' %i)
        dfnew=pd.merge(dforigin, oiltoadd,on='Year',how='outer')
        dfnew.to_csv(path_miss+'\\%s.csv'%i, encoding='utf-8', index=False)
    return

def add_gdp(gdp,statelist,path_miss):
    """
    Extracts data from the GDP data set and adds it the CSV files of all the input states
    Input:
          gdp (Pandas DataFrame) - Input DataFrame
          statelist (List of str) - List of initials of the state (like CA, WA, TX)
    Returns:
            None
    """
    if any('Fips' == gdp.columns):
        del gdp['Fips']
    gdp=gdp[0:52].T
    del gdp['United States']
    for c in range(len(statelist)):
        gdp.rename(columns={gdp.columns[c]:statelist[c]},inplace=True)
    gdp.reset_index(inplace=True)
    gdp.rename(columns={'index':'Year'},inplace=True)
    gdp.Year = gdp.Year.astype(float)
    for i in statelist:
        df = pd.read_csv(path_miss+'\\%s.csv' %i)
        df.rename(columns={'Unnamed: 0':'Year'},inplace=True)
        df_r=pd.merge(df, gdp[['Year',i]],on='Year',how='outer')
        df_r.rename(columns={i:'GDP'},inplace=True)
        df_r.to_csv(path_miss+'\\%s.csv'%i, encoding='utf-8', index=False)
    return

def clean_all_data():
    """
    Wrapping function to clean the data and add it the CSV files of all the input states
    Input:
          None
    Returns:
            None
    """
    path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'Data')
    data_path = op.join(path, 'Original Data')
    path_miss = op.join(path, 'Cleaned Data with Missing Predictors')
    if not os.path.exists(path_miss):
        os.makedirs(path_miss)
    df = pd.read_excel(op.join(data_path, 'State Energy Data System.xlsx'),sheetname=3)
    gdp=pd.read_csv(op.join(data_path, 'GDP.csv'),skiprows=4,index_col=1)
    climate_data = pd.read_csv(op.join(data_path, 'climate_annual.txt'),sep = ' ',encoding = 'utf-8')
    oil = pd.read_excel(op.join(data_path, 'Annual Average Crude Oil Price.xlsx'),skiprows=4)
    clprb = xlrd.open_workbook(op.join(data_path, 'CLPRB.xlsx'))
    emfdb=pd.read_excel(op.join(data_path, 'EMFDB.xlsx'))
    enprp=pd.read_excel(op.join(data_path, 'ENPRP.xlsx'))
    ngmpb=pd.read_excel(op.join(data_path, 'NGMPB.xlsx'))
    paprb=pd.read_excel(op.join(data_path, 'PAPRB.xlsx'))
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"], path_miss)
    add_gdp(gdp,statelist,path_miss)
    add_clprb(clprb,statelist,path_miss)
    add_msn(emfdb,statelist,'EMFDB',path_miss)
    add_msn(enprp,statelist,'ENPRP',path_miss)
    add_msn(ngmpb,statelist,'NGMPB',path_miss)
    add_msn(paprb,statelist,'PAPRB',path_miss)
    climate(climate_data,'PCP',statelist,path_miss)
    climate(climate_data,'ZNDX',statelist,path_miss)
    oil_price(oil,statelist,path_miss)
    names = os.listdir(path_miss)
    assert len(names) == len(statelist), 'Add clean_all_data Error'
    return
