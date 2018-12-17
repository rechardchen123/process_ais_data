# -*- cding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import pymysql
import datetime
import glob

'''
程序说明：
1.实现能从Mysql数据库读取AIS数据到本地，保存到pandas的dataframe中；
2.实现从本地读取CSV文件，以便于数据处理；
3.利用datetime函数将数据库保存的时间戳转换成具体的时间函数，以便于读取；
4.将轨迹数据进行清洗，并对轨迹数据进行重构，输出符合要求的轨迹数据；
5.形成最终的MMSI唯一性代表的轨迹运动特性的数据，以便于后期深度学习的时候使用。
'''

# 链接数据库的句子
# dbconn = pymysql.connect(host = '127.0.0.1',user = 'root', passwd='369848252',db= 'ais_dynamic',charset = 'utf8')

# sql查询语句
# sqlcmd = "select * from ais_dynamic.ais_dynamic limit 100"

# 从CSV文件中读取数据进行处理
# ais_file= pd.read_csv(r'C:\Users\cege-user\Desktop\dataset-ais\1-1000000-ais.csv',header = 0,sep = ' ',names = list('Record_Datetime','MMSI','Longitude','Latitude','Direction',
#                                                        'Heading','Speed','Status','ROT','Position_Accuracy','UTC_Hour',
#                                                        'UTC_Minute','UTC_Second','Message_ID','Rec_Datetime','Source_ID'))

ais_file1 = pd.read_csv(r'D:\Data store file\dataset-ais\1-1000000-ais.csv')
ais_file2 = pd.read_csv(r'D:\Data store file\dataset-ais\1000001-2000000-ais.csv')
ais_file3 = pd.read_csv(r'D:\Data store file\dataset-ais\2000001-3000000.csv')
ais_file4 = pd.read_csv(r'D:\Data store file\dataset-ais\3000001-4000000.csv')
ais_file5 = pd.read_csv(r'D:\Data store file\dataset-ais\4000001-5000000.csv')
ais_file6 = pd.read_csv(r'D:\Data store file\dataset-ais\5000001-6000000.csv')
ais_file7 = pd.read_csv(r'D:\Data store file\dataset-ais\6000001-669370.csv')

pd.set_option('display.max_columns', None)  # 读取的数据显示全部的列，不缺省显示
# 读取多个csv文件
# ais_file = dict()
# file_names = glob.glob(r"C:\Users\cege-user\Desktop\dataset-ais\*.csv")
# for file_name in file_names:
#     ais_file[file_name] = pd.read_csv(file_name)

# 利用pandas导入mysql数据
# test = pd.read_sql(sqlcmd,dbconn)
# 将数据表中的第一行数据的时间戳转换成时间格式的数据
# 添加时区的转换方法
# test.Record_Datetime = (pd.to_datetime(test.Record_Datetime.values, unit="s").tz_localize('UTC').tz_convert('Asia/Shanghai'))

# 不添加时区的转换方法（因为元数据是当地的时间戳，可以不需要加上时区去转换数据）
# test.Record_Datetime = (pd.to_datetime(test.Record_Datetime.values, unit="s"))
# Convert_aisfile_record_Datetime1 = pd.to_datetime(ais_file1.record_Datetime.values, unit='s')
# Convert_aisfile_record_Datetime2 = pd.to_datetime(ais_file2.record_Datetime.values, unit='s')
# Convert_aisfile_record_Datetime3 = pd.to_datetime(ais_file3.record_Datetime.values, unit='s')
# Convert_aisfile_record_Datetime4 = pd.to_datetime(ais_file4.record_Datetime.values, unit='s')
# Convert_aisfile_record_Datetime5 = pd.to_datetime(ais_file5.record_Datetime.values, unit='s')
# Convert_aisfile_record_Datetime6 = pd.to_datetime(ais_file6.record_Datetime.values, unit='s')
# Convert_aisfile_record_Datetime7 = pd.to_datetime(ais_file7.record_Datetime.values, unit='s')

# 合并这7个dataframe成为一个dataframe,便于后续的数据处理
merge_aisfile_1_2 = ais_file1.append(ais_file2, ignore_index=True)
merge_aisfile_3_1 = merge_aisfile_1_2.append(ais_file3, ignore_index=True)
merge_aisfile_4_2 = merge_aisfile_3_1.append(ais_file4, ignore_index=True)
merge_aisfile_5_3 = merge_aisfile_4_2.append(ais_file5, ignore_index=True)
merge_aisfile_6_4 = merge_aisfile_5_3.append(ais_file6, ignore_index=True)
merge_aisfile_last = merge_aisfile_6_4.append(ais_file7, ignore_index=True)

# 合并成一张dataframe后，将时间戳转换成时间格式并将转换后的新时间格式写如DataFrame
merge_aisfile_last.Record_Datetime = pd.to_datetime(merge_aisfile_last.Record_Datetime.values, unit='s')

# 转换经度和维度成日常习惯表达（数据库中的经纬度数据除以600000转换成正常的经纬度的度单位表示，精度范围在-180到180，超出为非法。纬度范围在-90到90，超出为非法）
merge_aisfile_last.Longitude = merge_aisfile_last.Longitude / 600000

merge_aisfile_last.Latitude = merge_aisfile_last.Latitude / 600000

# 船航向转换（范围是0-3600，以1/10°为单位，3600为不可用值，数据清晰中应该将数据抛出）
merge_aisfile_last.Direction = merge_aisfile_last.Direction / 10

# 船首向不需要转换（数据库记录的默认范围是0-359，以及511，超出为非法，511代号表示船首向不可用，在清洗数据中应该将其数据抛出）

# 船速（船速/10为正常的船舶运行速度,范围是0-1023，超出为非法）
merge_aisfile_last.Speed = merge_aisfile_last.Speed / 10

'''
数据处理部分，详细实现有以下三个方面：
1.将经纬度，航向，航速，船首向明显不符合的特征的数据剔除
2.将MMSI相同的数据按照时间先后顺序进行排序
3.对一天24h以内的，同一个MMSI的数据进行输出
'''
# 筛选明显不符合特征的数据
merge_aisfile_last.describe()  # 获取统计上的指标,对于一般的数据可以大致清楚其分布的范围与大小

# 筛选heading不等于511的所有的数据，Direction中不等于360的所有数据，Speed在0-40之间的数据,
# Longitude和latitude分别在(116-119)和(36-39)之间的数据

Longitude_Latitude_Heading_Direction_Speed_filter = merge_aisfile_last[(merge_aisfile_last['Heading'] != 511)
                                                                       & (merge_aisfile_last['Direction'] != 360)
                                                                       & ((merge_aisfile_last['Speed'] > 0) & (
        merge_aisfile_last['Speed'] < 40))
                                                                       & ((merge_aisfile_last['Longitude'] > 116) & (
        merge_aisfile_last['Longitude'] < 119))
                                                                       & ((merge_aisfile_last['Latitude'] > 36) & (
        merge_aisfile_last['Latitude'] < 39))
                                                                       ]
# 删除不需要的列的数据
finish_drop = Longitude_Latitude_Heading_Direction_Speed_filter.drop(
    columns=['Status', 'ROT', 'Position_Accuracy', 'UTC_Hour', 'UTC_Minute',
             'UTC_Second', 'Message_ID', 'Rev_Datetime', 'Source_ID'])
# 行索引重新排序，形成新的DataFrame
finish_drop.reset_index(drop=True, inplace=True)
drop_decimals_finish_drop = finish_drop.round({'Longitude': 3, 'Latitude': 3})  # 输出位数的小数部分保留2位

# 保存CSV文件
merge_aisfile_last.to_csv(r'D:\Data store file\dataset-ais-tianjin\merged_data.csv')
Longitude_Latitude_Heading_Direction_Speed_filter.to_csv(
    r'C:\Users\cege-user\Desktop\dataset-ais-tianjin\Longitude_Latitude_Heading_Direction_Speed_filter.csv')
drop_decimals_finish_drop.to_csv(r'D:\Data store file\dataset-ais-tianjin\drop_decimals_finish_drop.csv',index=False)
