"""
Welcome to arcospy, the python version of the R arcos package maintained by
The Washington Post. arcospy is the result of a R-to-python translation
project carried out at the University of Maryland in the Fall of 2019.
The project was motivated by The Washington Post’s data-driven story
on a large pain pill database recently made publicly available.

The arcospy module was built to offer the exact same functionality as arcos,
with the only difference being the ability to run the API calls in python!
All of the commands in arcospy inherit the names from the original commands
in arcos. Both arcos and arcospy act as wrappers for the DEA ARCOS dataset.

arcospy github: https://github.com/jeffcsauer/arcospy
arcos github: https://github.com/wpinvestigative/arcos
"""

# Function 1: Get latitude and longitude data for each pharmacy based on
# BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

def pharm_latlon(county='', state='', key=''):
    """Get latitude and longitude data for each pharmacy based on
    BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/pharmacy_latlon"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 2: Get the core-based statistical area GEOID for each pharmacy
# based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

def pharm_cbsa(geoid='', county='', state='', key=''):
    """Get the core-based statistical area GEOID for each
    pharmacy based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

    Args:
        geoid: Filter the data to only this cbsa GEOD (e.g. '26580')
        county: If geoid not included, filter the data to only this county (e.g. 'Mingo')
        state: If geoid not included, filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/pharmacy_cbsa"

    import requests
    import pandas as pd

    params = {"geoid": geoid,
              "state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 3: Get census tract GEOID for each pharmacy
# based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

def pharm_tracts(county='', state='', key=''):
    """Get census tract GEOID for each pharmacy based on
    BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/pharmacy_tracts"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 4: Get county GEOID for each pharmacy
# based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

def pharm_counties(county='', state='', key=''):
    """Get county GEOID for each pharmacy based on
    BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/pharmacy_counties"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 5: Get DEA designated addresses for each pharmacy
# based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

def buyer_addresses(county='', state='', key=''):
    """Get DEA designated addresses for each pharmacy
    based on BUYER_DEA_NO (Only includes retail and chain pharmacy designations)

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/buyer_details"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 6: Get DEA designated addresses for each Reporter
# based on REPORTER_DEA_NO (Includes Manufacturers and Distributors)

def reporter_addresses(county='', state='', key=''):
    """Get DEA designated addresses for each Reporter based
    on REPORTER_DEA_NO (Includes Manufacturers and Distributors)

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/reporter_details"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 7: Get annual population for counties between 2006 and 2012

def county_population(county='', state='', key=''):
    """Get annual population for counties between 2006 and 2012

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/county_population"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 8: Get annual popuilation for states between 2006 and 2012

def state_population(state='', key=''):
    """Get annual population for states between 2006 and 2012

    Args:
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/state_population"

    import requests
    import pandas as pd

    params = {"state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 9: Get list of misidentified pharmacies by BUYER_DEA_NOs

def not_pharmacies(key=''):
    """Get list of misidentified pharmacies by BUYER_DEA_NOs

    Args:
        key
        Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    url = "https://arcos-api.ext.nile.works/v1/not_pharmacies"

    import requests
    import pandas as pd

    params = {"key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 10: Get annual summarized pill totals by county

def summarized_county_annual(county='', state='', key=''):
    """Get annual summarized pill totals by county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/combined_county_annual"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 11: Get buyer details for each county

def buyer_details(county='', state='', key=''):
    """Get monthly summarized pill totals by county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/buyer_details"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 12: Get total pills for each pharmacy in a county

def total_pharmacies_county(county='', state='', key=''):
    """Get total pills for each pharmacy in a county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/total_pharmacies_county"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 13: Get total pills for each manufacturer in a county
def total_manufacturers_county(county='', state='', key=''):
    """Get total pills for each manufacturer in a county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/total_manufacturers_county"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 14: Get total pills for each distributor in a county

def total_distributors_county(county='', state='', key=''):
    """Get total pills for each distributor in a county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/total_distributors_county"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 15: Get total pills for each pharmacy in a state

def total_pharmacies_state(county='', state='', key=''):
    """Get total pills for each pharmacy in a state

    Args:
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/total_pharmacies_state"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 16: Get total pills for each manufacturer in a state

def total_manufacturers_state(county='', state='', key=''):
    """Get total pills for each manufacturer in a state

    Args:
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/total_manufacturers_state"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 17: Get total pills for each distributor in a state

def total_distributors_state(county='', state='', key=''):
    """Get total pills for each distributor in a state

    Args:
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/total_distributors_state"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 18: Get annual total pills for each buyer (pharmacy, etc) in a county

def combined_buyer_annual(county='', state='', key=''):
    """Get annual total pills for each buyer (pharmacy, etc) in a county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/combined_buyer_annual"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 19: Get annual total pills for each buyer (pharmacy, etc) in a county

def combined_buyer_monthly(county='', state='', year='', key=''):
    """Get annual total pills for each buyer (pharmacy, etc) in a county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        year: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/combined_buyer_monthly"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "year": year,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 20: Get monthly summarized pill totals by county

def summarized_county_monthly(county='', state='', key=''):
    """Get monthly summarized pill totals by county

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/combined_county_monthly"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 21: raw data command: Download raw prescription data
# for specified county (by state and county names)

def county_raw(county='', state='', key=''):
    """Data from from non-contiguous states not yet processed and available.

    Args:
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(state) == 2:

        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/county_data"

    import requests
    import pandas as pd

    params = {"state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 22: raw data command: Download raw prescription
# data for specified county (by county FIPS code)

def county_raw_fips(fips='', key=''):
    """Data from from non-contiguous states not yet processed and available.

    Args:
        fips: Filter the data to only this county (e.g. ‘01001’ for Autauga, Alabama)
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(fips) > 1 or len(fips) > 6:

        print("No valid FIPS code detected.")

    url = "https://arcos-api.ext.nile.works/v1/county_fips_data"

    import requests
    import pandas as pd

    params = {"fips": fips,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 23: raw data command: Download raw prescription
# data for specified pharmacy (by BUYER_DEA_NO)

def pharmacy_raw(buyer_dea_no='', key=''):
    """Data from from non-contiguous states not yet processed and available.

    Args:
        buyer_dea_no: Filter the data to only this pharmacy (e.g. ‘AB0454176’)
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    elif not len(buyer_dea_no) > 1 or len(buyer_dea_no) > 9:

        print("No valid buyer DEA number detected.")

    url = "https://arcos-api.ext.nile.works/v1/pharmacy_data"

    import requests
    import pandas as pd

    params = {"buyer_dea_no": buyer_dea_no,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Function 24: raw data command: Download raw ARCOS data (Warning 130+ GB file)

def raw_data(key=''):
    """Download raw ARCOS data (Warning 130+ GB file)

    Args:
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    url = "https://arcos-api.ext.nile.works/v1/all_the_data"

    import requests
    import pandas as pd

    params = {"key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)
