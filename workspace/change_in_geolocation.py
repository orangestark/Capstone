import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *


path = './F20_Logs_new'
MAX_NUM = 10000000000
MAX_MISS = 5


if __name__ == '__main__' :
    d = {}
    num = 0
    df = pd.read_csv('name_regions_F20_new.csv', encoding='utf-8-sig')
    for i, row in df.iterrows():
        if num >= MAX_NUM:
            break
        num += 1
        name = row['User full name']
        miss = 0
        l = [0, 0, 0]
        previous = []
        for i in range(1, 12):
            try:
                location = row[str(i)].split(',')
            except:
                miss += 1
                continue
                
            if len(previous) == 0 :
                if len(location) > 1:
                    l[(i-1)//4] += len(location) - 1
            else:
                if len(location) > 1:
                    l[(i-1)//4] += len(location) - 1
                    if len(previous) > 1:
                        for check in location:
                            if check not in previous:
                                l[(i-1)//4] += 1
                    else:
                        if previous[0] not in location:
                            l[(i-1)//4] += 1
                else:
                    if len(previous) > 1:
                        if location[0] not in previous:
                            l[(i-1)//4] += 1
                    else:
                        if previous[0] != location[0]:
                            l[(i-1)//4] += 1
            previous = location
        if miss <= MAX_MISS:
            d[name] = l
    op = []
    for k, v in d.items():
        op.append({'User full name': k, 'Assignment 1-4': v[0], 'Assignment 5-8': v[1], 'Assignment 9-11': v[2]})
    df_out = pd.DataFrame(op)
    df_out.to_csv('./change_in_geolocation_F20.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
                    
                
                
    