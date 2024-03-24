import pandas as pd
import csv
df = pd.read_csv('public-covid-19-cases-canada.csv', sep=',')

Number_of_Rows = df.shape[0]
Number_of_Columns = df.shape[1]
Number_of_Province = df.groupby('province')['province'].count()
Range_of_Age = df.groupby('age')['age'].count()
Gender_Demographic = df.groupby('sex')['sex'].count()
# To Make Coloumn Search Non Case Sensitive
df['locally_acquired'] = df['locally_acquired'].str.lower()
Most_Frequent_Sources = df.groupby('locally_acquired')['locally_acquired'].count()
print ("Number of Entries: {0} Number of Columns: {1} \n".format(Number_of_Rows,Number_of_Columns))

print("Column Names are Listed below: ")
print(df.columns.values)

print('\nNumber of Cases in Each {0} '.format(Number_of_Province))
print('\nRange of agegroup sorted by {0}: '.format(Range_of_Age))
print('\nGender Demographics sorted by {0}: '.format(Gender_Demographic))
print('\nNumber of Cases {0}: '.format(Most_Frequent_Sources))

drop_AGE_df = df[~df['age'].isin(['Not Reported'])]
drop_SEX_df = drop_AGE_df[~drop_AGE_df['sex'].isin(['Not Reported'])]
drop_LOCALLYACQUIRED_df = drop_SEX_df[drop_SEX_df['locally_acquired'].notna()]
drop_TRAVELHISTORY_df = drop_LOCALLYACQUIRED_df[drop_LOCALLYACQUIRED_df['has_travel_history'].notna()]
drop_TRAVELHISTORY_df['age'].replace(['<18','<10','<1','10-19','<20'],['0-19','0-19','0-19','0-19','20-29'],inplace=True)
Reformated_Range_of_Age = drop_TRAVELHISTORY_df.groupby('age')['age'].count()
print('\nRange of agegroup sorted by {0}: '.format(Reformated_Range_of_Age))

drop_TRAVELHISTORY_df.to_csv('file_name.csv', sep=',',index=False)