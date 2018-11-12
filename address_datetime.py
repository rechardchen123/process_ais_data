#!/usr/bin/env python3 
# -*- coding: utf-8 -*
import os, sys
import glob
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#pd.set_option('display.max_columns', None)  # 读取的数据显示全部的列，不缺省显示
#pd.set_option('display.max_rows', None)

#read files in the directory
file_names = glob.glob("/home/ucesxc0/Scratch/output/ais_data_process/groupby-ais-file/*.csv")
#save_path = "D:/AIS-trajectory/ "
#创建文件夹用于存储轨迹数据
# for file in file_names:
#     basename1=os.path.basename(file)
#     basename2 = os.path.splitext(basename1)[0]
#     folder_name = save_path + str(basename2)
#     os.makedirs(folder_name)
# loop for the files
for f in file_names:
    read_file = pd.read_csv(f)

    # 读取datetime的天数
    read_file['Day'] = pd.to_datetime(read_file['Record_Datetime']).dt.day

    # 根据天数这一行将轨迹分成三个部分
    groups = read_file.groupby(read_file['Day'])

    #produce the everyday trajectory for the same MMSI
	
    for name, group in groups:
        select_group = groups.get_group(name) #use the get_group to select the single part of the groupby parts
        row = select_group['Latitude']
        column = select_group['Longitude']
        name_mmsi=select_group.iloc[0]['MMSI']
        plt.plot(row, column, linewidth=1.0)
        plt.xlabel("latitude")
        plt.ylabel("Longitude")
        plt.savefig("/home/ucesxc0/Scratch/output/ais_data_process/result/%d-%d.png"%(name_mmsi,name), dpi=60)  # 批量保存图片,按照MMSI-DAY的情况 不然有的会被合并，dpi不要调整太大        plt.show()
        plt.cla() #每次记得清空当前画布，不然轨迹都是在一个画布上完成的，轨迹就全部重叠在一起了。
		#plt.show()






