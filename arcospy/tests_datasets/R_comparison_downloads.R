# Download tests datasets using original ARCOS package
#install.packages("arcos")
library(arcos)

# Flow of script is to download each dataset and then save as a .csv
# which can be imported into Python for comparison

input_county = 'Hennepin'
input_state = 'MN'
input_key = 'WaPo'

# Test function 1: pharm_latlon
func1_output <- pharm_latlon(input_county, input_state, input_key)
write.csv(func1_output, file = '/Users/jefferysauer/Dropbox/Maryland/PhD_Courses/GEOG788P/jeffsauer_MnM4SDS_project/arcospy/arcospy/tests_datasets/func1_output.csv')

# Test function 3: pharm_tracts
func3_output <- pharm_tracts(input_county, input_state, input_key)
write.csv(func3_output, file = '/Users/jefferysauer/Dropbox/Maryland/PhD_Courses/GEOG788P/jeffsauer_MnM4SDS_project/arcospy/arcospy/tests_datasets/func3_output.csv')

# Test function 5: buyer_addresses
func5_output <- buyer_addresses(input_county, input_state, input_key)
write.csv(func5_output, file = '/Users/jefferysauer/Dropbox/Maryland/PhD_Courses/GEOG788P/jeffsauer_MnM4SDS_project/arcospy/arcospy/tests_datasets/func5_output.csv')

# Test function 7: county_population
func7_output <- county_population(input_county, input_state, input_key)
write.csv(func7_output, file = '/Users/jefferysauer/Dropbox/Maryland/PhD_Courses/GEOG788P/jeffsauer_MnM4SDS_project/arcospy/arcospy/tests_datasets/func7_output.csv')

# Test function 9: not_pharmacies
func9_output <- not_pharmacies("WaPo")
write.csv(func9_output, file = '/Users/jefferysauer/Dropbox/Maryland/PhD_Courses/GEOG788P/jeffsauer_MnM4SDS_project/arcospy/arcospy/tests_datasets/func9_output.csv')

# Test function 11: buyer_details
func11_output <- buyer_details(input_county, input_state, input_key)
write.csv(func11_output, file = '/Users/jefferysauer/Dropbox/Maryland/PhD_Courses/GEOG788P/jeffsauer_MnM4SDS_project/arcospy/arcospy/tests_datasets/func11_output.csv')

# Test function 13: total_manufacturers_county
func13_output <- total_manufacturers_county(input_county, input_state, input_key)
write.csv(func13_output, file = '/Users/jefferysauer/Dropbox/Maryland/PhD_Courses/GEOG788P/jeffsauer_MnM4SDS_project/arcospy/arcospy/tests_datasets/func13_output.csv')

# Test function 13: 