# arcospy.py
"""Welcome to arcospy, the python version of the R arcos package maintained by
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

import pandas as pd
import requests
import io

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

def buyer_list(key=''):
    """Get list of drugs available in the ARCOS database

    Args:
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:
        print("Please supply a valid API key.")

    url = "https://arcos-api.ext.nile.works/v1/buyer_list"

    params = {"key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)


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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "year": year,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

def county_list(key=''):
    """Get dataframe of counties, states, and fips codes that are represented in the ARCOS data

    Args:
        key: Key needed to make query successful (NOTE: only necessary arg)

    Returns:
        pandas data frame
    """

    if not key:
        print("Please supply a valid API key.")

    url = "https://arcos-api.ext.nile.works/v1/county_list"

    params = {"key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

def county_population(county='', state='', key=''):
    """Get annual population for counties between 2006 and 2014

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    # Deprecated due to changes in payload
    #requestdata = requestdata.json()

    # New transformation of delivery
    return pd.read_csv(io.StringIO(requestdata.text), sep='\t')

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

    params = {"fips": fips,
              "key": key}

    requestdata = requests.get(url, params=params)

    # Deprecated due to changes in payload
    #requestdata = requestdata.json()

    # New transformation of delivery
    return pd.read_csv(io.StringIO(requestdata.text), sep='\t')

def drug_list(key=''):
    """Get list of drugs available in the ARCOS database

    Args:
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:

        print("Please supply a valid API key.")

    url = "https://arcos-api.ext.nile.works/v1/drug_list"

    params = {"key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"geoid": geoid,
              "county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"buyer_dea_no": buyer_dea_no,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

def state_population(state='', key=''):
    """Get annual population for states between 2006 and 2014

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

    params = {"state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

def total_distributors_state(state='', key=''):
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

    params = {"state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

def total_manufacturers_state(state='', key=''):
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

    params = {"state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

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

    params = {"county": county,
              "state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

def total_pharmacies_state(state='', key=''):
    """Get total pills for each pharmacy in a state

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

    url = "https://arcos-api.ext.nile.works/v1/total_pharmacies_state"

    params = {"state": state,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# New functions (Week of 3/12/2020)

def drug_county_biz(buyer_bus_act='', drug='', county='', state='', key=''):
    """Returns all data by county (Will be large and could take extra time to load)

    Args:
        buyer_bus_act: If included, filters the data to only this
        buyer type (e.g. ‘HOSP/CLINIC’ or ‘RETAIL PHARMACY’)
        drug: Filter the data to only this drug (e.g. ‘FENTANYL’)
        county: Filter the data to only this county (e.g. 'Mingo')
        state: Filter the data to county within this state (e.g. 'WV')
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:
        print("Please supply a valid API key.")
    elif not drug:
        print("Please specify which drug you are interested in (e.g. 'FENTANYL').")
    elif not len(state) == 2:
        print("Please supply the U.S. state (in abbreviated form) of interest.")

    url = "https://arcos-api.ext.nile.works/v1/county_data_drug"

    params = {"buyer_bus_act": buyer_bus_act,
              "drug": drug,
              "state": state,
              "county": county,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)

# Drug county raw may be deprecated - suggest to use drug_county_biz instead

def drug_county_raw(buyer_bus_act='', drug='', fips='', key=''):
    """Returns all data by county (Will be large and could take extra time to load)

    Args:
        buyer_bus_act: If included, filters the data to only this
        buyer type (e.g. ‘HOSP/CLINIC’ or ‘RETAIL PHARMACY’)
        drug: Filter the data to only this drug (e.g. ‘FENTANYL’)
        fips: Filter the data to only this county (e.g. ‘01001’ for Autauga, Alabama)
        key: Key needed to make query successful

    Returns:
        pandas data frame
    """

    if not key:
        print("Please supply a valid API key.")
    elif not drug:
        print("Please specify which drug you are interested in (e.g. 'FENTANYL').")
    elif not len(fips) == 5:
        print("Please supply a zip code in 5 digit format \
              (e.g. ‘09003’ for Hartford, Connecticut).")

    url = "https://arcos-api.ext.nile.works/v1/county_data_drug"

    params = {"buyer_bus_act": buyer_bus_act,
              "drug": drug,
              "fips": fips,
              "key": key}

    requestdata = requests.get(url, params=params)

    requestdata = requestdata.json()

    return pd.DataFrame.from_records(requestdata)
