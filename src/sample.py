import pandas as pd
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
print(file_dir)
filepath = file_dir + "/modelreport.csv"

df = pd.read_csv(filepath, delimiter=',')

df8 = df[df.user_id == 8]
df8_tech = df8[df8.area == 'tech']
df8_tech_forward = df8_tech[df8_tech.attr == 'forward']

print("")
print("original df")
print("")
print(df)
print("")
print("df8")
print("")
print(df8)
print("")

print("df8_tech")
print("")
print(df8_tech)
print("")

print("df8_tech_forward")
print("")
print(df8_tech_forward)
print("")

