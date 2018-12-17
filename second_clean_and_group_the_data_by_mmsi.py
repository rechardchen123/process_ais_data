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
trajectory_process = pd.read_csv(r'C:\Users\LPT-ucesxc0\Documents\AIS-Data\drop_decimals_finish_drop.csv')
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
finish_drop = trajectory_process.drop(columns=['Heading'])

#按照MMSI输出数据
df1 = finish_drop.groupby(['MMSI'])
for group in df1:
    group[1].to_csv(str(group[0]) + '.csv', index=False)



