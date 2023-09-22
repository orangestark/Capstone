import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json

path = './Logs'
MAX_NUM = 10000

#return a list of path and name
def path_and_name(path, name, num, tp):
    l = []
    for i in range(1, num+1):
        fname = path.rstrip('/')+ '/' + name + '{:02}'.format(i) + "." + tp
        l.append(fname)
    return l
        
if __name__ == '__main__':
    ip_dict = {}
    for file in path_and_name(path,'HW', 11,'csv'):
        print(file)
        df = pd.read_csv(file, encoding='utf-8-sig')
        num = 0
        js_exist = False
        # print(df.head())
        try:
            df_ig = pd.read_csv('ip_geolocation.csv')
            ip_list = df_ig['IPv4'].tolist()
            # print(ip_list)
            js_exist = True
            print('READ SUCCESS')
        except:
            ip_list = []
        for ip in df['IP address']:
            ip = str(ip).strip()
            try:
                if (num < MAX_NUM) and (ip not in ip_dict.keys()) and (ip not in ip_list):
                    num += 1
                    js = ip_to_geo(ip)
                    ip_dict[ip] = js
                    print(num)
                    df_js = pd.DataFrame(js, index=[0])
                    if js_exist:
                        df_js.to_csv('ip_geolocation.csv', mode = 'a', index = False, header = False, encoding='utf-8-sig')
                    else:
                        df_js.to_csv('ip_geolocation.csv', mode = 'a', index = False, encoding='utf-8-sig')
                        js_exist = True
            except:
                print(ip)
        print('\nfinished\n')