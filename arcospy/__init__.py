
def pharm_latlon(county='', state='', key=''):
        
        if len(key)<1:
            
            print("Please supply a valid API key.")
            
        elif len(state)<1 or len(state)>2:
            
            print("Please supply the U.S. state (abbreviated) of interest.")
        
        else: 
            
            url = "https://arcos-api.ext.nile.works/v1/pharmacy_latlon"
            
            import requests
            import pandas as pd
            
            params = {"state": state,
                      "county": county, 
                      "key": key}
            
            requestdata = requests.get(url, params = params)
            
            requestdata = requestdata.json()
            
            return pd.DataFrame.from_records(requestdata)

# Function 2: Get the core-based statistical area GEOID for each pharmacy based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

def pharm_cbsa(geoid='', county='', state='', key=''):
    
        if len(key)<1:
            
            print("Please supply a valid API key.")
            
        elif len(state)<1 or len(state)>2:
            
            print("Please supply the U.S. state (abbreviated) of interest.")
        
        else: 
            
            url =  "https://arcos-api.ext.nile.works/v1/pharmacy_cbsa"
            
            import requests
            import pandas as pd
            
            params = {"geoid": geoid, 
                      "state": state,
                      "county": county, 
                      "key": key}
            
            requestdata = requests.get(url, params = params)
            
            requestdata = requestdata.json()
            
            return pd.DataFrame.from_records(requestdata)
            
# Function 3: Get census tract GEOID for each pharmacy based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

def pharm_tracts(county='', state='', key=''):
        
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url =  "https://arcos-api.ext.nile.works/v1/pharmacy_tracts"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
        
# Function 4: Get county GEOID for each pharmacy based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)
        
def pharm_counties(county='', state='', key=''):
  
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url =  "https://arcos-api.ext.nile.works/v1/pharmacy_counties"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
        
# Function 5: Get DEA designated addresses for each pharmacy based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)
        
def buyer_addresses(county='', state='', key=''):
       
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url =  "https://arcos-api.ext.nile.works/v1/buyer_details"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
        
# Function 6: Get DEA designated addresses for each Reporter based on REPORTER_DEA_NO (Includes Manufacturers and Distributors)
        
def reporter_addresses(county='', state='', key=''):
           
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url =  "https://arcos-api.ext.nile.works/v1/reporter_details"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
        
# Function 7: Get annual population for counties between 2006 and 2012
        
def county_population(county='', state='', key=''):
          
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
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)

# Function 8: Get annual popuilation for states between 2006 and 2012

def state_population(state='', key=''):
        
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/state_population"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
        
# Function 9: Get list of misidentified pharmacies by BUYER_DEA_NOs
        
def not_pharmacies(key=''):
        
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/not_pharmacies"
        
        import requests
        import pandas as pd
        
        params = {"key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
        
# Function 10: Get annual summarized pill totals by county

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
    
# Function 11: Get buyer details for each county
        
def buyer_details(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/buyer_details"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)

# Function 12: Get total pills for each pharmacy in a county

def total_pharmacies_county(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/total_pharmacies_county"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 13: Get total pills for each manufacturer in a county
        

def total_manufacturers_county(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/total_manufacturers_county"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 14: Get total pills for each distributor in a county
        
def total_distributors_county(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/total_distributors_county"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 15: Get total pills for each pharmacy in a state

def total_pharmacies_state(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/total_pharmacies_state"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 16: Get total pills for each manufacturer in a state

def total_manufacturers_state(county='', state='', key=''):
        
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/total_manufacturers_state"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 17: Get total pills for each distributor in a state

def total_distributors_state(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/total_distributors_state"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 18: Get annual total pills for each buyer (pharmacy, etc) in a county
        
def combined_buyer_annual(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/combined_buyer_annual"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
        
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)

# Function 19: Get annual total pills for each buyer (pharmacy, etc) in a county
        
def combined_buyer_monthly(county='', state='', year='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/combined_buyer_monthly"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "year": year,
                  "key": key}
            
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 20: Get monthly summarized pill totals by county
        
def summarized_county_monthly(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/combined_county_monthly"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
            
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 21: raw data command: Download raw prescription data for specified county (by state and county names)
        
def county_raw(county='', state='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
        
    elif len(state)<1 or len(state)>2:
        
        print("Please supply the U.S. state (abbreviated) of interest.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/county_data"
        
        import requests
        import pandas as pd
        
        params = {"state": state,
                  "county": county, 
                  "key": key}
            
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)

# Function 22: raw data command: Download raw prescription data for specified county (by county FIPS code)
        
def county_raw_fips(fips='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
    
    elif len(fips)<1 or len(fips)>6:
        
        print("No valid FIPS code detected.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/county_fips_data"
        
        import requests
        import pandas as pd
        
        params = {"fips": fips,
                  "key": key}
            
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 23: raw data command: Download raw prescription data for specified pharmacy (by BUYER_DEA_NO)
        
def pharmacy_raw(buyer_dea_no='', key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
    
    elif len(buyer_dea_no)<1 or len(buyer_dea_no)>9:
        
        print("No valid buyer DEA number detected.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/pharmacy_data"
        
        import requests
        import pandas as pd
        
        params = {"buyer_dea_no": buyer_dea_no,
                  "key": key}
            
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)
    
# Function 24: raw data command: Download raw ARCOS data (Warning 130+ GB file)
        
def raw_data(key=''):
    
    if len(key)<1:
        
        print("Please supply a valid API key.")
    
    else: 
        
        url = "https://arcos-api.ext.nile.works/v1/all_the_data"
        
        import requests
        import pandas as pd
        
        params = {"key": key}
            
        requestdata = requests.get(url, params = params)
        
        requestdata = requestdata.json()
        
        return pd.DataFrame.from_records(requestdata)