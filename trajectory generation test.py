# -*- cding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

test_dataset = pd.read_csv(r'D:\Data store file\dataset-ais\test_dataset.csv',encoding = 'utf-8')
pd.set_option('display.max_columns', None)  # 读取的数据显示全部的列，不缺省显示
pd.set_option('display.max_rows',None)

# data = pd.DataFrame({'MMSI': [205517000, 209047000,205517000, 205517000, 209047000, 209047000],
#                      'Longitude': [118.168, 118.119, 118.088, 117.956, 117.955, 117.903],
#                      'Latitude': [38.889, 38.918, 38.926, 38.944, 38.944, 38.952]})
# print(data)
# print(data.dtypes)

# def difference_mmsi(data):
#     difference = data['MMSI']+1 - data['MMSI']
#     if difference ==0:
#         data1 = pd.DataFrame()
# data['token'] = data.groupby('MMSI')['MMSI'].apply(lambda i:i.diff(1))
# print(data)
# data['token'] = [data.iloc[i]['MMSI']-data.iloc[i-1]['MMSI'] for i in range(0,len(data))]
# for index in range(0,len(data)):
#      diff = data.iloc[index+1]['MMSI'] - data.iloc[index]['MMSI']
#      if diff == 0:
#          data['token'] = 1
#      else:
#          data['token'] = 0
# print(data)

# data1 = np.array(data)
# data1_list = data1.tolist()
# for item in data1_list:
#
# print(data1_list)
# # for index,row in data.iterrows():
# #     print(index,row)

# for index in range(0, len(data)):
#     if index == 0:
#         diff = data.ix[index]['MMSI']
#         d.append(data.loc[index,:])
#     elif index != 0:
#         diff = data.ix[index]['MMSI'] - data.ix[index - 1]['MMSI']
#         if diff == 0:
#             d.append(data.loc[index, :])
#             pd.DataFrame(d,columns=('MMSI','Longitude','Latitude'))
# print(d)

# list_mmsi = data['MMSI']
# for row in list_mmsi:
#     get_row = row
#     for index in range(0,len(data)):
#         list = []
#         get_index = data.iloc[index]['MMSI']
#         if get_index == get_row:
#             list.append(data.iloc[index,:])
#
#             #保存每一次的输出成csv文件即可，well done!
# print(list)

# for i in data['MMSI']:
#     for row in data.itertuples():
#         index = row.MMSI- i
#         print(index)

# 经过反复的计算和方法，发现为了得到同一个MMSI下的船舶，其实是一个堆栈的操作方法,以下测试：
# def divide_AIS(data):
#     mmsi_stack = []  # 创建栈
#     mmsi_stack.append((data[0][0]))#起点位置入栈
#     for index in range(len(data)):
#         if index == 0:
#             first_element = data.iloc[index]['MMSI']
#             mmsi_stack.append(first_element)  # 压入栈
#         elif index != 0:
#             compare_mmsi = data.iloc[index]['MMSI']
#             diff = compare_mmsi - first_element
#             if diff == 0:
#                 mmsi_stack.pop(compare_mmsi)  # 弹出栈
#             else:
#                 return False
#             print(compare_mmsi)



# for index in range(0,len(data)):
#     mmsi_first = int(data.iloc[index]['MMSI'])
#     mmsi_data_stack.append(mmsi_first)
#     for row in data['MMSI']:
#         mmsi_data_stack.append(row)
#         compare = row - mmsi_first
#         if compare != 0:
#             mmsi_data_stack.pop()
#
#     print(mmsi_data_stack) #打印栈顶的元素

# mmsi_data_stack = []
# already_check_value = []
# for index in range(0,len(data)):
#     first_mmsi = data.ix[index,'MMSI']
#     mmsi_data_stack.append(first_mmsi)
#     already_check_value.append(first_mmsi)
#     for row in data['MMSI']:
#         mmsi_data_stack.append(row)
#         if row in already_check_value:
#             compare = row - first_mmsi
#         if compare!=0:
#             mmsi_data_stack.pop()
#         else:
#             print(mmsi_data_stack[-1])
# mmsi_data_stack = []
# already_checked_value = []
# for index in range(0,len(data)):
#     if index == 0:
#         first_mmsi = int(data.ix[index,'MMSI'])
#         mmsi_data_stack.append(first_mmsi)
#         for row in data['MMSI']:
#             mmsi_data_stack.append(row)
#             compare = row - first_mmsi
#             if compare != 0:
#                 mmsi_data_stack.pop()
#             else:
#                 print(mmsi_data_stack[-1])
#     else:
#         first_mmsi = int(data.ix[index,'MMSI'])
#         mmsi_data_stack.append(first_mmsi)
#         already_checked_value.append(first_mmsi)
#         for row in data['MMSI']:
#             if row not in already_checked_value:
#                 mmsi_data_stack.append(row)
#                 compare = row - first_mmsi
#                 if compare != 0:
#                     mmsi_data_stack.pop()
#                 else:
#                     print(mmsi_data_stack[-1])


# mmsi_stack = []
# for index in range(0,len(test_dataset)):
#     mmsi_first = test_dataset.iloc[index]['MMSI']
#     mmsi_stack.append(mmsi_first)
#     for row in test_dataset['MMSI']:
#         mmsi_stack.append(row)    #将当前元素压入堆栈
#         compare = row - mmsi_first
#         if compare !=0:
#             mmsi_stack.pop()
#         else:
#         print(mmsi_stack[-1])#打印栈顶元素
#test_dataset.sort_values(by='MMSI') 排序


# finish_drop = test_dataset.drop(columns=['Direction','Heading','Speed'])
# list_mmsi = finish_drop['MMSI'].drop_duplicates()#将MMSI列表得到

test_dataset['day'] = pd.to_datetime(test_dataset['Record_Datetime']).dt.day
print(test_dataset)
# df1 = test_dataset.groupby(['MMSI'])
#
# for group in df1:
#        group[1].to_csv(str(group[0])+'.csv',index = False)


# after_filter_test_dataset = []
# for row in list_mmsi:
#        after_filter_test_dataset.append(finish_drop[finish_drop['MMSI']==row])#数据已经转换成list，按照list的顺序得到的就是已经过滤好的数据
# print(after_filter_test_dataset)
# 画图
# for index in range(0,len(after_filter_test_dataset)):
#        row1 = after_filter_test_dataset[index]['Longitude']
#        row2 = after_filter_test_dataset[index]['Latitude']
#        plt.axis([36,39,116,119])
#        plt.plot(row2, row1, color="r", linestyle="--", linewidth=1.0)
#        plt.xlabel("latitude")
#        plt.ylabel("Longitude")
#        savefilename = index
#        #plt.savefig("savefilename.png",dpi=120)
#        plt.show()
