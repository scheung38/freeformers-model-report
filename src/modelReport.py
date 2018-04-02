import pandas as pd
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
print(file_dir)
filepath = file_dir + "/modelreport.csv"


def modelReportFunction(user_id, area, attr):
    try:
        df = pd.read_csv(filepath, delimiter=',')
        return df[df.user_id == user_id][df[df.user_id == user_id].area == area][
            df[df.user_id == user_id][df[df.user_id == user_id].area == area].attr == attr].rolling(window=2).apply(
            lambda x: x[1] - x[0])
    except Exception as e:
        print(e)


Test_area = "tech"
Test_attr = "forward"

Test_user_id = [8, 9]

res1 = modelReportFunction(Test_user_id[0], Test_area, Test_attr)["grade"].iloc[-1]

res2 = modelReportFunction(Test_user_id[1], Test_area, Test_attr)["grade"].iloc[-1]

average = (res1 + res2)/2

print(average)
