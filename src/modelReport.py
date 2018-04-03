import pandas as pd
import os
import sys
import numpy as np


def getCsv():
    try:
        file_dir = os.path.dirname(__file__)
        sys.path.append(file_dir)
        filepath = file_dir + "/modelreport.csv"
        return pd.read_csv(filepath, delimiter=',')

    except (FileNotFoundError, TypeError, Exception) as e:
        print(e)


def singleUserImprovement(user_id, area, attr):
    try:
        df = getCsv()
        df8 = df[df.user_id == user_id]
        df8_tech = df8[df8.area == area]
        df8_tech_forward = df8_tech[df8_tech.attr == attr]
        res = df8_tech_forward.rolling(window=2).apply(lambda x: x[1] - x[0])
        return res

    except (IndexError, Exception) as e:
        print(e)


def averageUsersImprovement(user_id, area, attr):
    acc = []
    for x in user_id:
        acc.append(singleUserImprovement(x, area, attr)["grade"].iloc[-1])
    print(acc)
    return np.average(acc)


if __name__ == '__main__':
    Test_area = "tech"
    Test_attr = "forward"
    Test_user_id = [8, 9, 10]

    print(averageUsersImprovement(Test_user_id, Test_area, Test_attr))
