#!/usr/bin/env python3 
# -*- coding: utf-8 -*
import os, sys
import glob
import pandas as pd
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

#pd.set_option('display.max_columns', None)  # 读取的数据显示全部的列，不缺省显示
#pd.set_option('display.max_rows', None)

#read files in the directory
file_names = glob.glob(r"C:\Users\LPT-ucesxc0\AIS-Data\data-after-split-MMSI/*.csv")

# loop for the files
for f in file_names:
    read_file = pd.read_csv(f)
    #分别读取天，时，分，秒并且将时分转换成秒以便计算
    read_file['Day'] = pd.to_datetime(read_file['Record_Datetime']).dt.day
    read_file['Hour'] = (pd.to_datetime(read_file['Record_Datetime']).dt.hour).apply(lambda x:x*3600)
    read_file['Minute'] = (pd.to_datetime(read_file['Record_Datetime']).dt.minute).apply(lambda x:x*60)
    read_file['Seconds'] = pd.to_datetime(read_file['Record_Datetime']).dt.second
    read_file['time_to_seconds'] = read_file['Hour'] + read_file['Minute'] + read_file['Seconds']
    #删除以上的时分秒数据:
    after_process_read_file = read_file.drop(columns=['Record_Datetime','Hour','Minute','Seconds'])
    # 根据天数将同一个MMSI文件按照天数分开，按照MMSI-Day的格式生成文件
    group_by_day = after_process_read_file.groupby(after_process_read_file['Day'])
    name = int(after_process_read_file.iloc[0]['MMSI'])
    for group in group_by_day:
        group[1].to_csv(str(name)+'-'+str(group[0])+'.csv', index=False)




    #produce the everyday trajectory for the same MMSI

    # for name, group in groups:
    #     select_group = groups.get_group(name) #use the get_group to select the single part of the groupby parts
    #     row = select_group['Latitude']
    #     column = select_group['Longitude']
    #     name_mmsi=select_group.iloc[0]['MMSI']
    #     plt.plot(row, column, linewidth=1.0)
    #     plt.xlabel("latitude")
    #     plt.ylabel("Longitude")
    #     plt.savefig("/home/ucesxc0/Scratch/output/ais_data_process/result/%d-%d.png"%(name_mmsi,name), dpi=60)  # 批量保存图片,按照MMSI-DAY的情况 不然有的会被合并，dpi不要调整太大        plt.show()
    #     plt.cla() #每次记得清空当前画布，不然轨迹都是在一个画布上完成的，轨迹就全部重叠在一起了。
	# 	#plt.show()






