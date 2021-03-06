import pandas as pd
from numpy import nanmean, nanmedian, nanmax, nanmin

pd.options.display.max_rows = 9999 # expand the number of rows displayed for certain print outs

dataframe = pd.read_csv('Restaurant_Scores_-_LIVES_Standard.csv')
# dataframe contains 53973 rows x 22 columns
# can be treated like a 2D array, where [x][y] = ['column title'][row #]

inspection_scores = dataframe['inspection_score'] # section of the dataframe that stores all of the inspection scores - essentially an array of inspection scores
violation_description = dataframe['violation_description'] # 'array' of violation descriptions

# statistic variables found with numpy functions
min_score = nanmin(inspection_scores)
max_score = nanmax(inspection_scores)
mean_score = nanmean(inspection_scores)
median_score = nanmedian(inspection_scores)

# print out the dataset statistics w/ some small formatting
print('\nReastaurant Inspection Score Statistics: ')
print('MIN:    ', min_score)
print('MAX:    ', max_score)
print('MEAN:   ', mean_score)
print('MEDIAN: ', median_score)
print('\n')

# calling .value_counts() on the array of violation descriptions will return a new set of the values, with the count of that value in the original array
violation_value_counts = violation_description.value_counts()
print('Restaurant Violation Counts:')
print(violation_value_counts)