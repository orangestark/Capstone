import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *

path = './F20/HW'
MAX_NUM = 10000000

if __name__ == '__main__' :
    d = {}
    for x, file in enumerate(path_and_name(path,'HW', 11,'csv')):
        if x==7:
            continue
        df = pd.read_csv(file, encoding='utf-8-sig')
        num = 0
        for i, row in df.iterrows():
            if i >= MAX_NUM:
                break
            num += 1
            if row['Surname'] == 'Overall average':
                break
            fn = row['First name'] + ' ' + row['Surname']
            idn = row['ID number']
            if idn not in d.keys():
                d[idn] = fn
    
    op = []
    for k, v in d.items():
        op.append({'User full name':v, 'ID number':str(k)})
    df_out = pd.DataFrame(op)
    df_out.to_csv('./name_id.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
        