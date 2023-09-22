import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *

path = './name_ips/F20'
MAX_NUM = 1000000

if __name__ == '__main__' :
    for x, file in enumerate(path_and_name(path,'name_ips', 11,'csv')):
        if x==7:
            continue
        df = pd.read_csv(file, encoding='utf-8-sig')
        df_g = pd.read_csv(name_file('./F20/HW','HW',x+1,'csv'), encoding='utf-8-sig')
        full_names = []
        for i, row in df_g.iterrows():
            if i >= MAX_NUM:
                break
            if row['Surname'] == 'Overall average':
                full_names.append(row['Surname'])
                break
            fn = row['First name'] + ' ' + row['Surname']
            full_names.append(fn)
        df_g['User full name'] = full_names
        df_out = pd.merge(df, df_g[['User full name', 'ID number', 'Grade/20.00']], on = 'User full name')
        df_out.to_csv(name_file('./ips_grade/F20/','ips_grade',x+1,'csv'), mode = 'w', index = False, header = True, encoding='utf-8-sig')