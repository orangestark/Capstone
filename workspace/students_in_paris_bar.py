import pandas as pd
from ip_to_geo_1 import ip_to_geo
import json
from util import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df_rg = pd.read_csv('./name_regions_F20(1).csv', encoding='utf-8-sig')
    X = [(i+1) for i in range(11)]
    Y = [0 for i in range(11)]
    Y_ofe = [0 for i in range(11)]
    Y_f = [0 for i in range(11)]
    Y_np = [0 for i in range(11)]
    Y_idf = [0 for i in range(11)]
    for i, row in df_rg.iterrows():
        if row['User full name'] == 'Promethee Spathis':
            continue
        for j in range(len(Y)):
            try:
                ls = row[str(j+1)].split(',')
                if 'Paris' in ls:
                    Y[j] += 1
                if 'out of Europe' in ls:
                    Y_ofe[j] += 1
                if 'France' in ls and 'Paris' not in ls:
                    Y_f[j] += 1
                if 'Paris' not in ls and 'IdF' not in ls:
                    Y_np[j] += 1
                if 'IdF' in ls or 'Paris' in ls:
                    Y_idf[j] += 1
            except:
                continue
    print(X)
    print(Y)
    print(Y_ofe)
    print(Y_f)
    print(Y_np)
    print(Y_idf)
    
    '''plot students in paris (bar)'''
    # plt.bar(X, Y)
    # plt.title("Number of Students in Paris throughout 11 Assignments")
    # plt.xlabel("Assignment")
    # plt.ylabel("Number of Students")
    
    # plt.show()
    # # plt.savefig('students_in_paris_bar.png')
    
    '''plot students in paris (line)'''
    # plt.plot(X, Y, linewidth = 3)
    # plt.title("Number of Students in Paris throughout 11 Assignments")
    # plt.xlabel("Assignment")
    # plt.ylabel("Number of Students")
    # plt.xticks(X)
    # plt.annotate('lock down #1', xy = (2.5, 95), xytext = (2.5, 157), arrowprops=dict(facecolor='red'))
    # plt.annotate('lock down #2', xy = (6.5, 95), xytext = (6.5, 157), arrowprops=dict(facecolor='red'))
    
    '''another version'''
    # plt.annotate('lock down #1', xy = (2.5, 152), xytext = (5, 148), arrowprops=dict(facecolor='red'))
    # plt.annotate('lock down #2', xy = (6.5, 115), xytext = (8.5, 130), arrowprops=dict(facecolor='red'))
    
    plt.show()
    # plt.savefig('students_in_paris_bar.png')
    
    
    '''plot students not in paris'''
    # plt.bar(X, Y_np)
    # plt.title("Number of Students not in Paris throughout 11 Assignments")
    # plt.xlabel("Assignment")
    # plt.ylabel("Number of Students")
    
    # plt.show()
    # # plt.savefig('students_in_paris_bar.png')
    
    '''plot bar and line'''
    # df = pd.DataFrame({
    #     'Students outside Paris'})
    # plt.bar(X, Y)
    # plt.title("Number of Students in Paris throughout 11 Assignments")
    # plt.xlabel("Assignment")
    # plt.ylabel("Number of Students")
    
    # plt.show()
    # # plt.savefig('students_in_paris_bar.png')