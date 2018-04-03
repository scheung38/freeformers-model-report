import pandas as pd
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
print(file_dir)
filepath = file_dir + "/modelreport.csv"

# Read the CSV into a pandas data frame (df)
# With a df you can do many things
# most important: visualize data with Seaborn

# df = pd.read_csv('/Users/zaharamiriam/PycharmProjects/freeformers-model-report/src/modelreport.csv', delimiter=',')

# Write a function that given area and attribute, outputs average improvement say UserA = 4, UserB = 0 => 2
# area:     attribute:      average_improvement:
# tech,     forward,        2

print("")
print("original df")
df = pd.read_csv(filepath, delimiter=',')
print(df)
print("")
print("beginning of df8")
df8 = df[df.user_id == 8]
print(df8)
print("beginning of df8_tech")
df8_tech = df8[df8.area == 'tech']
print(df8_tech)
print("beginning of df8_tech_forward")
df8_tech_forward = df8_tech[df8_tech.attr == 'forward']
print(df8_tech_forward)
print("beginning of df8_tech_forward_rolling")
print(df8_tech_forward.rolling(window=2).apply(lambda x: x[1] - x[0]))
print("")
df2 = df[df.user_id == 9]
print("beginning of df2")
print(df2)
print("")
print(df.pivot_table(index='user_id', columns=['area', 'attr'], values='grade',
                     aggfunc='last'))
print("")

df2 = pd.DataFrame({'Age': [35, 37, 40, 29, 31, 26, 28],
                    'City': ['B', 'Ch', 'LA', 'Ch', 'B', 'B', 'Ch'],
                    'Position': ['M', 'M', 'M', 'P', 'P', 'M', 'M']})
print("")
print(df2)
print("")
print(df2.pivot_table(index='Position', columns='City', values='Age', aggfunc='last'))
