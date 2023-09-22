import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *

# path = './F20/Logs'
# path = './F21/Logs'
# path = './F20_Logs_new'
path = './F21_Logs_new'
MAX_NUM = 1000000

if __name__ == '__main__' :
    # d = {}
    for x, file in enumerate(path_and_name(path,'HW', 11,'_new.csv')):
        d = {}
        df = pd.read_csv(file, encoding='utf-8-sig')
        # df_ig = pd.read_csv('ip_geolocation.csv')
        num = 0
        for i, row in df.iterrows():
            if num >= MAX_NUM:
                break
            num += 1
            name = row['User full name']
            IP = row['IP address']
            if name in d.keys():
                if IP not in d[name]:
                    d[name].append(IP)
            else:
                d[name] = [IP]
        op = []
        for k, v in d.items():
            op.append({'User full name':k, 'num':len(v), 'IP address':','.join(map(str, v))})
        df_out = pd.DataFrame(op)
        # df_out.columns = ['User full name','num','IP address']
        # df_out.to_csv('./name_ips/F20/name_ips'+'{:02}'.format(x+1)+'.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
        # df_out.to_csv('./name_ips/F21/name_ips'+'{:02}'.format(x+1)+'.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
        # df_out.to_csv('./name_ips/F20_new/name_ips'+'{:02}'.format(x+1)+'.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
        df_out.to_csv('./name_ips/F21_new/name_ips'+'{:02}'.format(x+1)+'.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
        