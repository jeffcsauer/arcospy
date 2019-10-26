# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:55:44 2019

@author: USER
"""
import pandas as pd

# define states
states = ["AL", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# create empty DF for population
popdata = pd.DataFrame([])

# copy over the county pop function
def county_population(state='', county='', key=''):
          
        if len(key)<1:
            
            print("Please supply a valid API key.")
            
        elif len(state)<1 or len(state)>2:
            
            print("Please supply the U.S. state (abbreviated) of interest.")
        
        else: 
            
            url = "https://arcos-api.ext.nile.works/v1/county_population"
            
            import requests
            import pandas as pd
            
            params = {"state": state,
                      "county": county, 
                      "key": key}
            
            requestdata = requests.get(url, params = params)
            
            tempdata = requestdata.json()
            
            return pd.DataFrame.from_records(tempdata)

# download for all states     
for i in states:
   
    popdata = popdata.append(county_population(state = i, key = "WaPo"))

# create empty DF for pill data
pilldata = pd.DataFrame([])

# copy over the pill data
def summarized_county_annual(county='', state='', key=''):

    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/combined_county_annual"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)

# download the pill data
for i in states:
   
    pilldata = pilldata.append(summarized_county_annual(state = i, key = "WaPo"))

# merge the two df
pillpop = pd.merge(popdata, pilldata, how='left', on=['countyfips', 'year'])