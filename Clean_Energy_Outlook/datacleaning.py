import pandas as pd
import numpy as np
import xlrd

def data_extract(df,state,param_list):
    datalist=[]
    dftemp=df[df['MSN'].isin(["Year"] + param_list) & (df.State==state)]
    del dftemp['Data_Status']
    del dftemp['State']
    del dftemp['MSN']
    dftemp=dftemp.T
    dftemp.columns=param_list
    datalist.append(dftemp)
    #datalist.to_csv('Data/Data_States/%s.csv'% (statelist[i]), encoding='utf-8', index=True)
    return datalist

def data_extract_all(df,state_list,param_list):
    for i in state_list:
        data=data_extract(df,i,param_list)
        data[0].to_csv('Data/Data_States/%s.csv'%i, encoding='utf-8', index=True)
    return

def add_clprb(state_list):
    data = xlrd.open_workbook('Data/Original Data/more MSN/CLPRB.xlsx') # open xlsx file
    for j in state_list:
        dftemp = pd.read_csv('Data/Data_States/%s.csv' %j)
        dftemp.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        dftemp['CLPRB']=None
        table = data.sheet_by_name(j) # open sheet j
        nrows = table.nrows # get how many lines
        for i in range(1,nrows): #cycle in the table
            dftemp['CLPRB'][i-1] = table.row_values(i)[3] # columns 4
        dftemp.to_csv('Data/Data_States/%s.csv'%j, encoding='utf-8', index=False)
    return

def add_msn(state_list,parameter):
    data=pd.read_excel("Data/Original Data/more MSN/%s.xlsx" %parameter)
    for i in state_list:
        tempdf=data[data.StateCode=='%s'%i]
        del tempdf['MSN']
        del tempdf['StateCode']
        df = pd.read_csv('Data/Data_States/%s.csv' %i)
        df.rename(columns={'Unnamed: 0':'Year','Unnamed: 5':'GDP'}, inplace = True)
        df_r=pd.merge(df, tempdf,on='Year',how='outer')
        df_r.rename(columns={'Data':parameter}, inplace = True)
        df_r.to_csv('Data/Data_States/%s.csv' %i, encoding='utf-8', index=False)
    return

def climate(data,param,statelist):
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
        dforigin = pd.read_csv('Data/Data_States/%s.csv' %i)
        dfstate=data[data.State==statesdic[i]]
        dftoadd=dfstate[['Year',param]]
        dfnew=pd.merge(dforigin, dftoadd,on='Year',how='outer')
        dfnew.to_csv('Data/Data_States/%s.csv'%i, encoding='utf-8', index=False)
    return

def oil_price(oil_data,statelist):
    oiltoadd=oil_data[14:-1]
    for i in statelist:
        dforigin = pd.read_csv('Data/Data_States/%s.csv' %i)
        dfnew=pd.merge(dforigin, oiltoadd,on='Year',how='outer')
        dfnew.to_csv('Data/Data_States/%s.csv'%i, encoding='utf-8', index=False)
    return

def add_gdp(gdp,statelist):
    del gdp['Fips']
    gdp=gdp[0:52].T
    del gdp['United States']
    for c in range(len(gdp.columns)):
        gdp.rename(columns={gdp.columns[c]:statelist[c]},inplace=True)
    gdp.reset_index(inplace=True)
    gdp.rename(columns={'index':'Year'},inplace=True)
    gdp.Year = gdp.Year.astype(float)
    for i in statelist:
        df = pd.read_csv('Data/Data_States/%s.csv' %i)
        df.rename(columns={'Unnamed: 0':'Year'},inplace=True)
        df_r=pd.merge(df, gdp[['Year',i]],on='Year',how='outer')
        df_r.rename(columns={i:'GDP'},inplace=True)
        df_r.to_csv('Data/Data_States/%s.csv'%i, encoding='utf-8', index=False)
    return
