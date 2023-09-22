import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *

# path = './name_ips/F20'
# path = './name_ips/F21'
# path = './name_ips/F20_new'
path = './name_ips/F21_new'
MAX_NUM = 10

def get_Paris_centric_location(df, ip):
    if df_ip[df_ip['ip_address'] == ip]['continent'].tolist()[0] == 'Europe' :
        if df_ip[df_ip['ip_address'] == ip]['country'].tolist()[0] == 'France':
            if df_ip[df_ip['ip_address'] == ip]['city'].tolist()[0] == 'Paris' :
                return 'Paris'
            else:
                return 'France'
        else:
            return 'Europe'
    else:
        return 'out of Europe'
    
def get_Paris_centric_location_2(df, ip):
    if df_ip[df_ip['ip_address'] == ip]['continent'].tolist()[0] == 'Europe' :
        if df_ip[df_ip['ip_address'] == ip]['country'].tolist()[0] == 'France':
            if df_ip[df_ip['ip_address'] == ip]['region_geoname_id'].tolist()[0] == 3012874 :
                if df_ip[df_ip['ip_address'] == ip]['city'].tolist()[0] == 'Paris' :
                    return 'Paris'
                else:
                    return'IdF'
            else:
                return 'France'
        else:
            return 'Europe'
    else:
        return 'out of Europe'
    
def arr_to_str(arr):
    result = ''
    if 'Paris' in arr:
        result += 'Paris,'
    if 'France' in arr:
        result += 'France,'
    if 'Europe' in arr:
        result += 'Europe,'
    if 'out of Europe' in arr:
        result += 'out of Europe'
    return result.rstrip(',')

def arr_to_str_2(arr):
    result = ''
    if 'Paris' in arr:
        result += 'Paris,'
    if 'IdF' in arr:
        result += 'IdF,'
    if 'France' in arr:
        result += 'France,'
    if 'Europe' in arr:
        result += 'Europe,'
    if 'out of Europe' in arr:
        result += 'out of Europe'
    return result.rstrip(',')

if __name__ == '__main__' :
    d = {}
    df_ip = pd.read_csv('ip_info.csv', encoding='utf-8-sig')
    for x, file in enumerate(path_and_name(path,'name_ips', 11,'.csv')):
        df = pd.read_csv(file, encoding='utf-8-sig')
        num = 0
        for i, row in df.iterrows():
            # if num >= MAX_NUM:
            #     break
            # num += 1
            name = row['User full name']
            try:
                IP = row['IP address'].split(',')
            except:
                print(name, row['IP address'])
                continue
            for ip in IP:
                # l = get_Paris_centric_location(df_ip, ip)
                l = get_Paris_centric_location_2(df_ip, ip)
                if name in d.keys():
                    if l not in d[name][x]:
                        d[name][x].append(l)
                else:
                    d[name] = [[] for k in range(11)]
                    d[name][x].append(l)
        # print(d)
        # if x==1:
        #     break
    op = []
    for k, v in d.items():
        total = []
        op.append({'User full name':k})
        for i, arr in enumerate(v):
            total.extend(arr)
            # op[-1][str(i+1)] = arr_to_str(arr)
            op[-1][str(i+1)] = arr_to_str_2(arr)
        # op[-1]['total'] = arr_to_str(total)
        op[-1]['total'] = arr_to_str_2(total)
    df_out = pd.DataFrame(op)
    # df_out.to_csv('./name_regions_F20(1).csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
    # df_out.to_csv('./name_regions_F21.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
    # df_out.to_csv('./name_regions_F20_new.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
    df_out.to_csv('./name_regions_F21_new.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
            