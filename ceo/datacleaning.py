import pandas as pd
import numpy as np
import xlrd
import os
import ceo
import sys
import os.path as op
data_path = op.join(ceo.__path__[0], 'Data')
data_path = op.join(data_path, 'Original Data')
US_states = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

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
    assert type(df) == pd.DataFrame and type(state) == str and type(param_list) == list, 'TypeError'
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
    datalist.append(dftemp)
    return datalist[0]

def data_extract_all(df,state_list,param_list):
    """
    Extracts data of all the input states with the input parameters
    Input:
          df (Pandas DataFrame) - Input DataFrame
          state_list (List of str) - List of initials of the state (like CA, WA, TX)
          param_list (List of str) - Column names to extract
    Returns:
            None
    """
    assert type(df) == pd.DataFrame and type(state_list) == list and type(param_list) == list and all(isinstance(x, str) for x in state_list) and all(isinstance(x, str) for x in param_list), 'TypeError'
    for i in state_list:
        data=data_extract(df,i,param_list)
        data.to_csv('Data/Cleaned Data/%s.csv'%i, index=True)
    return

def add_clprb(data,state_list):
    """
    Extracts data from the CLPRB data set and adds it the CSV files of all the input states
    Input:
          data (Pandas DataFrame) - Input CLPRB DataFrame
          state_list (List of str) - List of initials of the state (like CA, WA, TX)
    Returns:
            None
    """
    for j in state_list:

        dftemp = pd.read_csv('Data/Cleaned Data/%s.csv' %j)
        dftemp.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        dftemp['CLPRB']=None
        table = data.sheet_by_name(j) # open sheet j
        nrows = table.nrows # get how many lines
        for i in range(1,nrows): #cycle in the table
            dftemp['CLPRB'][i-1] = table.row_values(i)[3] # columns 4
        dftemp.to_csv('Data/Cleaned Data/%s.csv'%j, encoding='utf-8', index=False)
    names = os.listdir('Data/Cleaned Data/')
    assert len(names) == len(US_states), 'Add CLPRB Error'
    return

def add_msn(data,state_list,parameter):
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
        df = pd.read_csv('Data/Cleaned Data/%s.csv' %i)
        df.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        df_r=pd.merge(df, tempdf,on='Year',how='outer')
        df_r.rename(columns={'Data':parameter}, inplace = True)
        df_r.to_csv('Data/Cleaned Data/%s.csv' %i, encoding='utf-8', index=False)
    names = os.listdir('Data/Cleaned Data/')
    assert len(names) == len(US_states), 'Add MSN Error'
    return

def climate(data,param,statelist):
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
        'WY': 'Wyoming'
}
    for i in statelist:
        dforigin = pd.read_csv('Data/Cleaned Data/%s.csv' %i)
        dfstate=data[data.State==statesdic[i]]
        dftoadd=dfstate[['Year',param]]
        dfnew=pd.merge(dforigin, dftoadd,on='Year',how='outer')
        dfnew.to_csv('Data/Cleaned Data/%s.csv'%i, encoding='utf-8', index=False)
    names = os.listdir('Data/Cleaned Data/')
    assert len(names) == len(US_states), 'Add Climate Error'
    return

def oil_price(oil_data,statelist):
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
        dforigin = pd.read_csv('Data/Cleaned Data/%s.csv' %i)
        dfnew=pd.merge(dforigin, oiltoadd,on='Year',how='outer')
        dfnew.to_csv('Data/Cleaned Data/%s.csv'%i, encoding='utf-8', index=False)
    names = os.listdir('Data/Cleaned Data/')
    assert len(names) == len(US_states), 'Add oil_price Error'
    return

def add_gdp(gdp,statelist):
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
    assert len(statelist) == len(US_states), 'statelist Error'
    for c in range(len(gdp.columns)):
        gdp.rename(columns={gdp.columns[c]:statelist[c]},inplace=True)
    gdp.reset_index(inplace=True)
    gdp.rename(columns={'index':'Year'},inplace=True)
    gdp.Year = gdp.Year.astype(float)
    for i in statelist:
        df = pd.read_csv('Data/Cleaned Data/%s.csv' %i)
        df.rename(columns={'Unnamed: 0':'Year'},inplace=True)
        df_r=pd.merge(df, gdp[['Year',i]],on='Year',how='outer')
        df_r.rename(columns={i:'GDP'},inplace=True)
        df_r.to_csv('Data/Cleaned Data/%s.csv'%i, encoding='utf-8', index=False)
    names = os.listdir('Data/Cleaned Data/')
    assert len(names) == len(US_states), 'Add GDP Error'
    return

def clean_all_data(df,gdp,clprb,climate_data,oil,emfdb,enprp,ngmpb,paprb):
    """
    Wrapping function to clean the data and add it the CSV files of all the input states
    Input:
          df (Pandas DataFrame) - Input DataFrame
          gdp (Pandas DataFrame) - Input DataFrame
          clprb (Pandas DataFrame) - Input DataFrame
          climate_data (Pandas DataFrame) - Input DataFrame
          oil (Pandas DataFrame) - Input DataFrame
          emfdb (Pandas DataFrame) - Input DataFrame
          enprp (Pandas DataFrame) - Input DataFrame
          ngmpb (Pandas DataFrame) - Input DataFrame
          paprb (Pandas DataFrame) - Input DataFrame
    Returns:
            None
    """
    statelist=["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
    data_extract_all(df,statelist,["HYTCP","WYTCP","SOEGP","NUETP"])
    add_gdp(gdp,statelist)
    add_clprb(clprb,statelist)
    add_msn(emfdb,statelist,'EMFDB')
    add_msn(enprp,statelist,'ENPRP')
    add_msn(ngmpb,statelist,'NGMPB')
    add_msn(paprb,statelist,'PAPRB')
    climate(climate_data,'PCP',statelist)
    climate(climate_data,'ZNDX',statelist)
    oil_price(oil,statelist)
    names = os.listdir('Data/Cleaned Data/')
    assert len(names) == len(US_states), 'Add clean_all_data Error'
    return
