# -*- cding: utf-8 -*-
import os
import pandas as pd
import numpy as np
from datetime import datetime,date
import matplotlib.pyplot as plt


'''
经过 read and process data 得到了经过筛选的轨迹数据，将不符合要求的轨迹数据删除，
再此基础上，将相关轨迹按照MMSI的唯一性进行重绘，构成新的轨迹点。
主要步骤如下：
1.统计drop_decimals_finish_drop.csv文件中MMSI的个数，得到处理后的数据中轨迹数据的总条目；
2.再根据时间，将同一天MMSI相同的轨迹数据输出，形成单个MMSI，在指定的时间所形成的轨迹数据；
3.利用经度为横坐标，纬度为纵坐标画图，按照时间先后顺序输出轨迹；
4.得到轨迹的完整图像
'''
# 读取CSV文件
trajectory_process = pd.read_csv(r'D:\Data store file\dataset-ais\drop_decimals_finish_drop.csv')
pd.set_option('display.max_columns', None)  # 读取的数据显示全部的列，不缺省显示
pd.set_option('display.max_rows',None)


count_MMSI = 0
for i in trajectory_process['MMSI'].duplicated():
    if i == False:
        count_MMSI = count_MMSI + 1
print('total MMSI number is: ', count_MMSI)  # count_MMSI = 1746 表明有1746搜船舶的MMSI数据，形成1746个轨迹点的数据



# 转换日期格式
trajectory_process['Record_Datetime'] = pd.to_datetime(trajectory_process['Record_Datetime'])

#得到MMSI列表，去除重复的MMSI数据
finish_drop = trajectory_process.drop(columns=['Direction','Heading','Speed'])
#
# list_mmsi = finish_drop['MMSI'].drop_duplicates()
df1 = finish_drop.groupby(['MMSI'])
for group in df1:
    group[1].to_csv(str(group[0]) + '.csv', index=False)

# after_filter_trajectory_process = [] #创建一个列表用来存储分组后的MMSI数据
#
#
# for row in list_mmsi:
#     after_filter_trajectory_process.append(finish_drop[finish_drop['MMSI']==row])#将相同MMSI的数据从原数据列中筛选出来，压入堆栈


# file = open('ais_data.txt','w')
# for i in after_filter_trajectory_process:
#     file.write(str(i))
#     file.write('\n')
# file.close()
#
# 画图,需要特殊处理一下,内存大小限制
# for index in range(0,len(after_filter_trajectory_process)):
#     #根据数据的经纬度绘制轨迹图
#     row = after_filter_trajectory_process[index]['Latitude']
#     column = after_filter_trajectory_process[index]['Longitude']
#     plt.axis([36,39,116,119])
#     plt.plot(row,column,linewidth = 1.0)
#     plt.xlabel("latitude")
#     plt.ylabel("Longitude")
#     #plt.savefig(index.png,dpi=120)
#     plt.show()
