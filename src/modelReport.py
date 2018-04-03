import pandas as pd
import os
import sys
import numpy as np

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
print(file_dir)
filepath = file_dir + "/modelreport.csv"


def singleUserImprovement(user_id, area, attr):
    try:
        df = pd.read_csv(filepath, delimiter=',')
        return df[df.user_id == user_id][df[df.user_id == user_id].area == area][
            df[df.user_id == user_id][df[df.user_id == user_id].area == area].attr == attr].rolling(window=2).apply(
            lambda x: x[1] - x[0])
    except (IndexError, Exception) as e:
        print(e)


def averageUsersImprovement(user_id, area, attr):
    acc = []
    for x in user_id:
        acc.append(singleUserImprovement(x, area, attr)["grade"].iloc[-1])
    print(acc)
    return np.average(acc)


# res1 = singleUserImprovement(Test_user_id[0], Test_area, Test_attr)["grade"].iloc[-1]
# res2 = singleUserImprovement(Test_user_id[1], Test_area, Test_attr)["grade"].iloc[-1]
# average = (res1 + res2)/len(Test_user_id)
# print(average)

# print([acc.append(singleUserImprovement(x, Test_area, Test_attr)["grade"].iloc[-1]) for x in Test_user_id])

if __name__ == '__main__':
    Test_area = "tech"
    Test_attr = "forward"
    Test_user_id = [8, 9]

    print(averageUsersImprovement(Test_user_id, Test_area, Test_attr))
