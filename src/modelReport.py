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
        df_user = df[df.user_id == user_id]
        df_user_area = df_user[df_user.area == area]
        df_user_area_attr = df_user_area[df_user_area.attr == attr]
        res = df_user_area_attr.rolling(window=2).apply(lambda x: x[1] - x[0])
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
