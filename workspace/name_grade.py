import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *

path = './F20/HW/'
MAX_NUM = 10

if __name__ == '__main__' :
    d = {}
    df_total = pd.read_csv(path + 'hw_grades_20.csv', encoding='utf-8-sig')
    df_name = pd.read_csv('./name_id.csv', encoding='utf-8-sig')
    df_name['ID number'] = df_name['ID number'].astype(str)
    df = pd.merge(df_name, df_total, on = 'ID number')
    num = 0
    ls = df['0'] 
    for i in df['ID number']:
        if num > MAX_NUM:
            break
        num += 1
        print(i)