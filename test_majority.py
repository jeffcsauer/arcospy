# Import arcospy commands
from arcospy import pharm_latlon, pharm_tracts, buyer_addresses, county_population, not_pharmacies, buyer_details, total_manufacturers_county
import pandas as pd
import os

#Get filepath from travisci
#dirpath = os.getcwd()
#print("current directory is : " + dirpath)

# Create the series of test objects from commands
input_county = 'Hennepin'
input_state = 'MN'
input_key = 'WaPo'

## Test function 1: pharm_latlon
func1_output = pharm_latlon(input_county, input_state, input_key)
func1_output_R = pd.read_csv('/home/travis/build/jeffcsauer/arcospy/tests_datasets/func1_output.csv') 

# Drop first index column as artifact of importing csv
func1_output_R = func1_output_R.drop(func1_output_R.columns[0], axis=1)

# Test function 3: pharm_tracts
func3_output = pharm_tracts(input_county, input_state, input_key)
func3_output_R = pd.read_csv('/home/travis/build/jeffcsauer/arcospy/tests_datasets/func3_output.csv') 

# Drop first index column as artifact of importing csv
func3_output_R = func3_output_R.drop(func3_output_R.columns[0], axis=1)

# Test function 5: buyer_addresses
func5_output = buyer_addresses(input_county, input_state, input_key)
func5_output_R = pd.read_csv('/home/travis/build/jeffcsauer/arcospy/tests_datasets/func5_output.csv') 

# Drop first index column as artifact of importing csv
func5_output_R = func5_output_R.drop(func5_output_R.columns[0], axis=1)

# Test function 7: county_population
func7_output = county_population(input_county, input_state, input_key)
func7_output_R = pd.read_csv('/home/travis/build/jeffcsauer/arcospy/tests_datasets/func7_output.csv') 

# Drop first index column as artifact of importing csv
func7_output_R = func7_output_R.drop(func7_output_R.columns[0], axis=1)

# Test function 9: not_pharmacies
func9_output = not_pharmacies(input_key)
func9_output_R = pd.read_csv('/home/travis/build/jeffcsauer/arcospy/tests_datasets/func9_output.csv') 

# Drop first index column as artifact of importing csv
func9_output_R = func9_output_R.drop(func9_output_R.columns[0], axis=1)

# Test function 11: buyer_details
func11_output = buyer_details(input_county, input_state, input_key)
func11_output_R = pd.read_csv('/home/travis/build/jeffcsauer/arcospy/tests_datasets/func11_output.csv') 

# Drop first index column as artifact of importing csv
func11_output_R = func11_output_R.drop(func11_output_R.columns[0], axis=1)

# Test function 13: total_manufacturers_county
func13_output = total_manufacturers_county(input_county, input_state, input_key)
func13_output_R = pd.read_csv('/home/travis/build/jeffcsauer/arcospy/tests_datasets/func13_output.csv') 

# Drop first index column as artifact of importing csv
func13_output_R = func13_output_R.drop(func13_output_R.columns[0], axis=1)

# Run tests
assert func1_output.shape == func1_output_R.shape
assert func3_output.shape == func3_output_R.shape
assert func5_output.shape == func5_output_R.shape
assert func7_output.shape == func7_output_R.shape
assert func9_output.shape == func9_output_R.shape
assert func11_output.shape == func11_output_R.shape
assert func13_output.shape == func13_output_R.shape