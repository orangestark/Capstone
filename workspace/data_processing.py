import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df_rg = pd.read_csv('./name_regions_F20.csv', encoding='utf-8-sig')
    X = [(i+1) for i in range(11)]
    Y = [0 for i in range(11)]
    Z = [0 for i in range(11)]
    for i, row in df_rg.iterrows():
        if row['User full name'] == 'Promethee Spathis':
            continue
        for j in range(len(Y)):
            try:
                ls = row[str(j+1)].split(',')
                if len(ls) > 1:
                    Y[j] += 1
            except:
                Z[j] += 1
    # print(X)
    print(['{:.0%}'.format(Y[j]/253) for j in range(11)])
    print(['{:.0%}'.format(Z[j]/253) for j in range(11)])
    
    # Y1 = [Y[j]/253 for j in range(11)]
    # Z1 = [Z[j]/253 for j in range(11)]
    
    
    # plt.plot(X, Y1, label = 'Students who change location during each assignment')
    # plt.plot(X, Z1, label = 'Students who do not finish the assignment')
    # # plt.title("Number of Students in Paris throughout 11 Assignments")
    # plt.xlabel("Assignment")
    # plt.ylabel("Percentage of Students")
    # plt.legend()
    # plt.xticks(X)
    # # plt.yticks([0.05*j for j in range(1, 11)])
    
    # plt.show()