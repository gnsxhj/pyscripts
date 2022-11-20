import os

import time

import pandas as pd
import numpy as np
import re
import glob
import fnmatch
import datetime as dt
import shutil

from tempfile import TemporaryFile
import zipfile
from pathlib import Path

# pandas操作excel
os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp')
# path = './test.xlsx'
# data = pd.DataFrame({'id':[1,2,3], 'name':['abc','def','ghi']})
# data = data.set_index('id') # 将id设置为索引
# data.to_excel(path) #将数据写入excel文件
# print('test.xlsx')

# path = './read_file.txt'
# # read_data = pd.read_csv(path, sep=',', header=None)
# # read_data = pd.read_csv(path, sep=',', header=None, names=['性别','姓名','手机','地址','入职时间'])
# # read_data = pd.read_csv(path, sep=',', header=None, names=['性别','姓名','手机','地址','入职时间'], index_col=1)
# read_data = pd.read_csv(path, sep=',', header=None, nrows=3)
# '''
# sep: 分隔符或正则表达式 sep ='\s+'
# header: 默认第一行，没有就是None
# names: 和header配合使用
# index_col: 索引的列号或列名，可以是名称或数字
# '''
# print(read_data)
# # print(read_data.head(3))
# # print(read_data.shape)
# # print(read_data.columns)

# data = pd.read_csv(path, encoding='utf-8')
# data.to_csv('./read_file.csv', encoding='utf-8')
# print(data)

# path = './read_file.xlsx'
# data = pd.read_excel(path, header=None, names=['id', 'name', 'age', 'number', 'address', 'date'])
# data = data.set_index('id')
# print(data)
# # data.to_excel('./temp.xlsx')

# data = pd.Series(['XHJ','Male',20,'1981-10-09'], index=['a','b','c','d'])
# print(data.index)
# print(data.values)

# dict = {'huawei':520, 'xiaomi':320, 'apple':600, 'sumsung':550}
# data = pd.Series(dict)
# print(data)
# print(data.index) #查询索引
# print(data['huawei']) #根据k值查询, 里面只接受一个k
# print(data[['huawei', 'xiaomi']])
#
# list_1 = ['names','age','address']
# list_2 = ['XHJ','40','ANTING']
# data = pd.Series(list_2, index=list_1)
# print(data)

# path = './data_structure.xlsx'
# data = pd.read_excel(path, header=None, names=['id', 'name', 'age', 'number', 'address', 'date'], index_col='id')
# # print(data.sort_index)
# # print(data.sort_values('address'))
# # print(data.isnull())
# # print(data.notnull())
# # print(data.fillna(0))
# # print(data.fillna(1))
# # print(data.replace('明教','日月神教'))
# print(data.reset_index(drop=True)) #索引列被直接删除
# print(data.reset_index(drop=False)) #索引列被还原为普通列

# path = './data_structure.xlsx'
# data = pd.read_excel(path, header=None, names=['id', 'name', 'age', 'number', 'address', 'date'], index_col='id', nrows=7)
# print(data)

# data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
# print(data['a'][1]) # a列0行
# print(data.loc[0]['a']) # 根据标签来拿数值, 先行后列
# print(data.iloc[0][0]) # 根据标签的数字位置来确定
# print(data[['a', 'b']]) # 查询多个列，一定要用[]

# # 如何用字典来创建DataFrame
# dict = {
#     'name':['abc', 'def', 'ghi'], # 要用,隔开的
#     'age':['20', '35', '20'],
#     'action':['football', 'basketball', 'swimming']
# }
#
# data = pd.DataFrame(dict)
# print(data)
# print(data['name'])
# print(data.loc[1])
# print(data.loc[1]['name']) # 指定某行某列
# print(data.loc[1][['name','age']]) # 查询单行上面多列
# print(data.loc[0:1]) # 查询多行

# data_1 = pd.Series(['Jack', 'Tom', 'Mike'], index = [1,2,3], name = 'name')
# data_2 = pd.Series(['male', 'male', 'male'], index = [1,2,3], name = 'gender')
# data_3 = pd.Series([50, 40, 20], index = [1,2,3], name = 'age')
# table_1 = pd.DataFrame({data_1.name:data_1, data_2.name:data_2, data_3.name:data_3})
# print(table_1)
# print(table_1.head(2))
# print(table_1.tail(2))
# print(table_1.values)
# print(table_1.shape)
# print(table_1.fillna(0))
# print(table_1.replace(1, -1))
# print(table_1.isnull())
# print(table_1.notnull())
# print(table_1.columns)
# print(table_1.index)
# print(table_1.sort_index)
# print(table_1.sort_values)
# # table_2 = pd.DataFrame([data_1, data_2, data_3])
# # print(table_2)

# # Merge
# 数据1 = pd.DataFrame({'姓名':['叶问','李小龙','孙兴华','李小龙','叶问','叶问'],'出手次数1':np.arange(6)})
# 数据2 = pd.DataFrame({'姓名':['黄飞鸿','孙兴华','李小龙'],'出手次数2':[1,2,3]})
# 数据3 = pd.merge(数据1, 数据2, on='姓名', how='inner') # 内连接
# # 数据3 = pd.merge(数据1, 数据2, on='姓名', how='left') # 左连接
# # 数据3 = pd.merge(数据1, 数据2, on='姓名', how='right') # 右连接
# # 数据3 = pd.merge(数据1, 数据2, on='姓名', how='outer') # 左连接
# print(数据1)
# print('*'*30)
# print(数据2)
# print('='*30)
# print(数据3)

# # MultipleKey Merge
# 数据1 = pd.DataFrame({'姓名': ['张三', '张三', '王五'],'班级': ['1班', '2班', '1班'],'分数': [10,20,30]})
# 数据2 = pd.DataFrame({'姓名': ['张三', '张三', '王五','王五'],'班级': ['1班', '1班', '1班','2班'],'分数': [40,50,60,70]})
# 数据3= pd.merge(数据1,数据2,on=['姓名','班级']) # 内连接的结果
# 数据4= pd.merge(数据1,数据2,on=['姓名','班级'], how='outer') # 外连接的结果
# 数据5= pd.merge(数据1,数据2,on=['姓名'], how='inner') # 内连接的结果
# 数据5= pd.merge(数据1,数据2,on=['姓名'], suffixes=['_l', '_r'], how='inner') # 内连接的结果, 用suffixes指定后缀区分同样的key
# 数据6= pd.merge(数据1,数据2,on=['姓名'], how='outer') # 外连接的结果
# print(数据1)
# print('*'*30)
# print(数据2)
# print('='*30)
# print(数据3)
# print('*'*30)
# print(数据4)
# print('='*30)
# print(数据5)
# print('*'*30)
# print(数据6)

# # Merge on Index (基于 Index 上的Merge)
# 数据1 = pd.DataFrame({'姓名': ['张三','李四','王五','张三','李四'],'次数':range(5)})
# 数据2 = pd.DataFrame({'数据': [10, 20]}, index=['张三','李四'])
# 数据3 = pd.merge(数据1, 数据2, left_on='姓名', right_index=True)
# print(数据1)
# print('*'*30)
# print(数据2)
# print('='*30)
# print(数据3)

# # join
# left_dict = {'姓名_l':['张三','李四','王五'], '年龄_l':[20, 10, 30]}
# right_dict = {'姓名_r':['Alice','Jack','Bob'], '年龄_r':[15, 32, 26]}
# left_tabel = pd.DataFrame(left_dict)
# right_tabel = pd.DataFrame(right_dict)
# print(left_tabel.join(right_tabel)) # key值要不一样
#

# # concat
# arr = np.arange(9).reshape(3,3)
# print(arr)
# arr_1 = np.concatenate([arr, arr], axis = 1 ) # axis=1表示按照列来合并
# print(arr_1)
# arr_2 = np.concatenate([arr, arr], axis = 0 ) # axis=0表示按照行来合并
# print(arr_2)

# data_1 = pd.Series([0, 1, 2], index=['A', 'B', 'C'])
# print(data_1)
# data_2 = pd.Series([3, 4], index=['D', 'E'])
# # data_2 = pd.Series([3, 4], index=['A', 'B'])
# print(data_2)
# data_3 = pd.concat([data_1, data_2], axis = 0) # 默认是按照行来合并
# print(data_3)
# data_4 = pd.concat([data_1, data_2], axis = 1, sort = True) # 按照列来合并，又可以理解为行对齐
# print(data_4)

# df1 = pd.DataFrame([['A0', 'B0', 'C0', 'D0'],['A1', 'B1', 'C1', 'D1'],['A2', 'B2', 'C2', 'D2'],['A3', 'B3', 'C3', 'D3']],columns=['A','B','C','D'])
# df2 = pd.DataFrame([['A4', 'B4', 'C4', 'D4'],\
#                     ['A5', 'B5', 'C5', 'D5'],\
#                     ['A6', 'B6', 'C6', 'D6'],\
#                     ['A7', 'B7', 'C7', 'D7']],\
#                    columns=['A','B','C','D'],\
#                    index=[4, 5, 6, 7])
# dict3 = {
#     'A':['A8', 'A9', 'A10', 'A11'],
#     'B':['B8', 'B9', 'B10', 'B11'],
#     'C':['C8', 'C9', 'C10', 'C11'],
#     'D':['D8', 'D9', 'D10', 'D11'],
# }
# df3 = pd.DataFrame(dict3, index=[8, 9, 10 ,11])
# dict4 = {
#     'B':['B2', 'B3', 'B6', 'B7'],
#     'D':['D2', 'D3', 'D6', 'D7'],
#     'F':['F2', 'F3', 'F6', 'F7'],
# }
# df4 = pd.DataFrame(dict4, index=[2, 3, 6 ,7])
# print(df1)
# print('*'*30)
# print(df2)
# print('='*30)
# print(df3)
# print('*'*30)
# print(df4)
# print('='*30)
# # frames = [df1, df2, df3]
# # result = pd.concat(frames)
# # result = pd.concat(frames, keys=['t1', 't2', 't3'])
# # print(result)
# # result = pd.concat([df1, df4], axis=1) # 对齐行
# # result = pd.concat([df1, df4], axis=1, join='inner') # inner表示求交集
# result = pd.concat([df1, df4], axis=0, ignore_index=True) # 整理出一个新的index
# # # append的用法
# # result = df1.append(df2) #改功能也将被删除，用concat取代
# print(result)
# s2 = pd.Series(['X0','X1','X2','X3'], index=['A','B','C','D'])
# result = df1.append(s2, ignore_index=True)
# print(result)

# # 各种数据自动填充
# # in_path = './autofill.xlsx'
# in_path = './autofill.csv'
# out_path = './autofill_out.csv'
# # read_data = pd.read_excel(in_path, skiprows=8, usecols='F:I', dtype={'序号':str,'性别':str,'日期':str})
# read_data = pd.read_csv(in_path, dtype={'序号':str,'性别':str,'日期':str}) # 读取csv文件
# start_date = dt.date(2022,4,13)
#
# # 累积月份的计算方法
# def add_month(init_date, delta_month):
#     '''
#     :param init_date: 输入起始日期
#     :param delta_month: 输入月份的差值
#     :return:
#     '''
#     y = delta_month // 12
#     m = init_date.month + delta_month % 12
#     # if m != 12: # 可以用不等于
#     if m > 12:    # 也可以用大于，因为等于12，计算取余就是0，会报错
#         y = y + m // 12
#         m = m % 12
#     return dt.date(init_date.year+y, m, init_date.day )
#
# print(start_date)
# for i in read_data.index:
#     read_data['序号'].at[i] = i+1
#     # read_data['序号'].at[i] = str(i+1)
#     read_data['性别'].at[i] = '男' if i % 2 == 0 else '女'
#     # read_data['日期'].at[i] = start_date + dt.timedelta(days=i)
#     # read_data['日期'].at[i] = dt.date(start_date.year+i, start_date.month, start_date.day)
#     read_data['日期'].at[i] = add_month(start_date, i)
# read_data.set_index('序号', inplace=True) # 去除系统生成的索引列, 打印出来的时候就不需要设置:index=False
# print(read_data)
# read_data.to_csv(out_path)
# # read_data.to_csv(out_path, index=False)

# # 计算列
# # in_path = './column_cal.xlsx'
# in_path = './column_cal.csv'
# # read_data = pd.read_excel(in_path, index_col='序号')
# read_data = pd.read_csv(in_path, index_col='序号')
# print(read_data)
# # read_data['销售金额'] = read_data['销售数量'] * read_data['单价'] # 最简单的列计算
# # for i in range(1,4): # 做循环且带条件的列计算
# #     if i % 2 != 0 : # 只对奇数行进行计算
# #         read_data['销售金额'].at[i] = read_data['销售数量'].at[i] * read_data['单价'].at[i]
# # # apply 函数
# # def rise_price(x):
# #     return(x+3)
# # read_data['单价'] = read_data['单价'].apply(rise_price) # 读取的单价会自动传递给apply里面的函数
# read_data['单价'] = read_data['单价'].apply(lambda x: x+3) # 用lambda来替代函数，读取的单价赋值给x
# print(read_data)

# in_path = './apply_function.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# # 加一列
# read_data['加分'] = read_data['民族'].apply(lambda x: 5 if x != '汉' else 0) # apply函数里面传递给x的值就是'民族'那一列
# read_data['最终分数'] = read_data['总分'] + read_data['加分']
# read_data['姓名字数'] = read_data['姓名'].apply(len) # 将姓名列里面的值传递给python的内置函数len
#
# print(read_data)

# # 计算数字的平方
# # data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['x','y','z'])
# data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=list('xyz'),index=list('abc')) # 把字符串转成列表
# print(data)
# # 用numpy应用到整个表格里面来计算
# print(data.apply(np.square))
# # 值针对某个列或者行来计算
# # new_data = data.apply(lambda i: np.square(i) if i.name == 'x' else i)
# # new_data = data.apply(lambda i: np.square(i) if i.name in ['x', 'y'] else i)
# new_data = data.apply(lambda i: np.square(i) if i.name == 'b' else i, axis=1) # axis默认是0，改为1 就是对进行操作
# print(new_data)

# # 计算日期的差值
# in_path = './date_cal.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# # read_data['日期间隔'] = read_data['结束日期'] - read_data['起始日期']
# # 先计算出来储存在变量中
# delta_days = read_data['结束日期'] - read_data['起始日期']
# # 然后通过apply函数来取得天数的数值, 然后用lambda函数来进行转换
# read_data['日期间隔'] = delta_days.apply(lambda x:x.days)
# print(read_data)

# # 排序
# in_path = './排序.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# print(read_data)
# # read_data.sort_values(by='序号', axis=0, inplace=True, ascending=False)
# # read_data.sort_values(by='语文', axis=0, inplace=True, ascending=False)
# # read_data.sort_values(by=['语文', '数学', '英语'], axis=0, inplace=True, ascending=[False, False, False])
# '''
# axis：如果axis=0，那么by="列名"；如果axis=1，那么by="行号"；
# ascending:True则升序，可以是[True,False]，即第一字段升序，第二个降序
# inplace=True：不创建新的对象，直接对原始对象进行修改；
# inplace=False：对数据进行修改，创建并返回新的对象承载其修改结果。
# '''
# # 按索引进行排列
# read_data.sort_index(inplace=True)
# print(read_data)

# in_path = '排序进阶.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data)
# # read_data.sort_values(by='a', axis=0, inplace=True, ascending=False) # 按照某个列的数值来排列
# read_data.sort_values(by=2, axis=1, inplace=True, ascending=False) # 按照某行的数值来排列
# print(read_data)

# # 数据查询
# in_path = '筛选.xlsx'
# # read_data = pd.read_excel(in_path)
# # 如果要以某个日期作为查询对象，最有效的办法就是设置为索引
# read_data = pd.read_excel(in_path, index_col='出生日期')
# read_data = pd.read_excel(in_path, index_col='出生日期', parse_dates=['出生日期'])
# new_data = read_data.sort_values('出生日期') # 用sort_values通过日期来排序, 这一步是truncate必须的
# read_data = pd.read_excel(in_path, index_col='序号', parse_dates=['出生日期']) # 用query来筛选日期，必须要用别的列来做索引
# print(read_data)
# print(read_data['1989'].head())
# print(read_data['1983-10'].head())
# print(read_data.sort_values('出生日期'))
# # 使用truncate函数有个前提就是要将日期设置为index，且要进行排序
# print(new_data.truncate(before='1987').head()) # 获取1980以后的数据
# print(new_data.truncate(after='1987-02').head()) # 获取1987年2月份以前的数据
# print(new_data['1983-10':'1987-07'].head()) # 获取1983至1987之间的数据
# # 用query来筛选多条件日期范围, 日期就不能是索引了，要用序号做索引
# condition = (
#     '@read_data.出生日期.dt.year > 1980 and'
#     '@read_data.出生日期.dt.year < 1990'
#     'and 性别 == "男"' # 这个and必须要写在这一行，不能跟在上面日期判断后面
# )
# print(read_data.query(condition))

# # 根据日期来查询
# print('*'*72)
# # 根据index来查询某个列的数值
# # print(read_data.loc['1983-10-27', '语文'])
# # print(read_data.loc['1983-10-27', ['语文','数学','英语']])
# # 按照某个时间区间范围来查询
# # print(read_data.loc['1983-10-27':'1990-12-31', ['语文','数学','英语']])
# # 按照某个时间区间范围来查询某个列范围的值
# # print(read_data.loc['1983-10-27':'1990-12-31', '语文':'数学'])
# # 带条件判断来筛选
# print(read_data.loc[(read_data['语文'] >= 60) & (read_data['英语'] <= 60)])

# in_path = '条件判断.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号', sheet_name='Sheet1') # sheet_name指定读取某个sheet
# read_data.loc[read_data['性别']=='男', '称呼'] = '先生' # loc 第一个参数就是表示行，第二个参数表示列
# read_data.loc[read_data['性别']=='女', '称呼'] = '女士' # loc 其实就是定位的意思，对应的值就是定位到这个位置的数值
# print(read_data)

# # 筛选
# in_path = '筛选.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# print(read_data)
# new_data = read_data.loc[2:4]
# print(new_data)
# 筛选出所有性别是男的
# print(read_data[read_data['性别'] == '男'])
# condition = read_data['性别'] == '男'
# print(read_data[condition])
# 用query来筛选条件
# 先创建条件
# condition = "性别 == '男' and 总分 >= 150"
# condition = "姓名 in ['李平平','王刚']"
# condition = "性别 == '女' and 60 <= 语文 <= 100" # =号始终是放在右边
# print(read_data.query(condition)) # query要用()来引用条件

# 用startswith或者endswith
# condition = read_data['姓名'].str.startswith('王')
# '''
# 语法：str.endswith("suffix", start, end) 或 str[start,end].endswith("suffix") 用于判断字符串中某段字符串是否以指定字符或子字符串结尾。
# —> bool 返回值为布尔类型（True,False）
# start —索引字符串的起始位置。
# end — 索引字符串的结束位置。
# str.endswith(suffix) start默认为0，end默认为字符串的长度减一（len(str)-1）
# suffix — 后缀，可以是单个字符，也可以是字符串，还可以是元组（"suffix"中的引号要省略）。
# '''
# print(read_data[condition])
# condition = read_data['地址'].str.startswith('上海市')
# print(read_data[condition])

# 用contains
# '''
# str.contains(pat, case=True, flags=0, na=nan, regex=True)是否包含查找的字符串
# 参数:
# pat : 字符串/正则表达式
# case : 布尔值, 默认为True.如果为True则匹配敏感
# flags : 整型,默认为0(没有flags)
# na : 默认为NaN,替换缺失值.
# regex : 布尔值, 默认为True.如果为真则使用re.research,否则使用Python
# 返回值:
# 布尔值的序列(series)或数组(array)
# '''
# condition = read_data['地址'].str.contains('信阳市')
# print(read_data[condition])
# condition = read_data['地址'].str.contains('[a-c]座', case=False)
# print(read_data[condition])

# # # drop删除
# in_path = '删除.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# print(read_data)
# # print(read_data.drop(2)) # 删除单行，直接写行标签
# # print(read_data.drop([1, 3]))
# # print(read_data.drop(labels=[1, 3])) # labels 是不是可以不要写？
# # print(read_data.drop('语文', axis=1)) # 删除单个列
# # print(read_data.drop(['语文', '数学'], axis=1))
# # print(read_data.drop(labels=['语文', '数学'], axis=1)) # 删除多个列
# # inplace参数：凡是会对原数组作出修改并返回一个新数组的，往往都有一个 inplace可选参数。
# # 如果手动设定为True（默认为False），那么原数组直接就被替换
# read_data.drop(labels=['语文', '数学'], axis=1, inplace=True) # 如果不设定inplace的话，后面的打印还是原先的数据
# print(read_data)

# # 如何查看空值，如何删除空值，如何替换空值
# in_path = '删除.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# print(read_data)
# # print(read_data.isnull()) # 缺失就是显示T
# # print(read_data.notnull()) # 不缺失显示T
# # print(read_data.dropna()) # 默认就是只要一行中有空值就删除整行
# # print(read_data.dropna(subset=['语文','英语'])) # 值对指定列上面有空值的进行删除
# # print(read_data.fillna(0)) # 对所有数值进行填空
# print(read_data.fillna({'语文':0.1,'数学':0.2,'英语':0.3})) # 对每一列填充不同的值, 需要用到字典

# in_path = '填充.xlsx'
# read_data=pd.read_excel(in_path)
# print(read_data)
# print(read_data.fillna(method='ffill')) # 用前面的数字填充后面，默认是按照列的方向
# print(read_data.fillna(method='bfill')) # 用后面的数字填充后面，默认是按照列的方向
# print(read_data.fillna(method='bfill', limit=2)) # limit表示只填充2个格子

# # 数据统计
# in_path = '数据统计.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# print(read_data)
# print('*'*45)
# # print(read_data.describe())
# # print('='*45)
# # print(read_data['语文', '英语'].describe()) # 只想统计某列
# print(read_data.mean()) # 只统计平均值
# print(read_data.max()) # 只统计最大值
# print(read_data.min()) # 只统计最小值

# # 去除重复和提取重复
# in_path = '去重.xlsx'
# read_data = pd.read_excel(in_path, index_col='序号')
# print(read_data)
# # print(read_data['姓名'].unique()) # 取名字的位置值，返回是一个列表
# # print(read_data['姓名'].value_counts()) # 计算名字重复重现的次数
# # drop_duplicate 函数
# print(read_data.drop_duplicates(subset=['姓名'], keep='first')) # subset 用法和drop一样
#
# # print(read_data.duplicated()) # 判断重复行，必须是每一列都是重复的
# # print(read_data.duplicated('姓名')) # 只判断某个列是否重复
# # print(read_data.duplicated(subset='姓名')) # 只判断某个列是否重复
# duplicated = read_data.duplicated(subset='姓名', keep='last') # 这里first, last和drop_duplicates好像反的
# print(read_data[duplicated]) # 用[]通过之前判定的标签来提取

# # 计算运算于数据对齐
# in_path = '计算.xlsx'
# read_data = pd.read_excel(in_path)
# # read_data['合计'] = read_data['1店'] + read_data['2店'] # 这里是不能直接打印的
# # read_data['合计'] = read_data['1店'].fillna(0) + read_data['2店'].fillna(0) # 将空值用0填充
# # read_data['合计'] = read_data['1店'].add(read_data['2店'], fill_value=0) # 加法
# pd.options.mode.use_inf_as_na = True # 可以把inf改为NaN
# read_data['比值'] = read_data['1店'].div(read_data['2店'], fill_value=0) # 除法
# print(read_data) # 包含空值就是空

# in_path = '对齐.xlsx'
# data1 = pd.read_excel(in_path, index_col='序号', sheet_name='Sheet1')
# data2 = pd.read_excel(in_path, index_col='序号', sheet_name='Sheet2')
# result = data1.add(data2, fill_value=0)
# print(result.fillna(0))

# # 多层索引和多层索引的计算方式
# in_path = '多层索引.xlsx'
# read_data = pd.read_excel(in_path, index_col=[0, 1], sheet_name = '有序') # index_col定义多个索引列
# read_data = pd.read_excel(in_path, sheet_name = '有序')
# read_data = read_data.set_index('班级','学号') # 也可以通过set_index来设置索引列
# new_data = read_data.loc['1班',:] # loc查询的格式是[,] 逗号前是行后是列，对所有列查询，就用:
# new_data = read_data.loc[(('1班','2班'), slice(None)),:] # 用元组的方式表示取多个行索引, slice类似于列上一行的':'，表示所有行
# new_data = read_data.loc[('1班','a'),:] # 用元组的方式表示取多个索引, 一个外标签，一个内标签
# print(read_data)
# print(new_data)
# print(read_data.index)
# print(read_data.index.levels[0])
# print(read_data.index.levels[1])
# read_data = pd.read_excel(in_path, index_col=[0, 1], sheet_name = '无序') # index_col定义多个索引列
# print(read_data)
# read_data = read_data.sort_index(level='科目') # 对某个index进行排序
# new_data = read_data.loc[('语文', slice(None)),:]
# print(new_data)

# # 多层索引的创建方式
# # 创建多层行索引
# # from_arrays 参数为一个二维数组
# multi_index = pd.MultiIndex.from_arrays([['a','a','b','b'],['1','2','1','2']],names=['x','y'])
# print(multi_index)
# # from_tuples 参数为一个元组
# multi_index = pd.MultiIndex.from_tuples([('a',1),('a',2),('b',1),('b',2)],names=['x','y'])
# print(multi_index)
# # from_product 参数为笛卡尔积
# multi_index = pd.MultiIndex.from_product([['a','b'],[1,2]],names=['x','y'])
# # data.index.names = ['x','y'] # 如果之前没有定义index的name 那么可以通过这个方法来指定
# print(multi_index)
# # 创建多层列索引
# out_path = '多层索引计算.xlsx'
# index = pd.MultiIndex.from_product([[2019, 2020], [5, 6]],names=['年', '月'])
# # columns = pd.MultiIndex.from_product([['香蕉', '苹果'], ['土豆', '茄子']],names=['水果', '蔬菜']) # 这个不对!!!
# columns = pd.MultiIndex.from_tuples([('水果','香蕉'),('水果','苹果'),('蔬菜','土豆'),('蔬菜','茄子')],names=['种类','名称'])
# data = pd.DataFrame(np.random.random(size=(4, 4)), index=index, columns=columns)
# print(data)
# data.to_excel(out_path)

# # 多层索引计算
# in_path = '销售.xlsx'
# out_path = '销售计算.xlsx'
# read_data = pd.read_excel(in_path, header=[0,1]) #
# # print(read_data)
# # print(read_data.columns) #查看列信息
# # 销量合计 = read_data[('土豆', '销量')] + read_data[('倭瓜', '销量')] # 通过两层索引进行相加
# # 毛利合计 = read_data[('土豆', '毛利')] + read_data[('倭瓜', '毛利')]
# 合计 = read_data['土豆'] + read_data['倭瓜']
# # print(合计.columns)
# 合计.columns = pd.MultiIndex.from_product([['合计'], 合计.columns]) # 切记外面要加一个[]
# result = pd.concat([read_data,合计], axis=1)
# print(result)
# result.to_excel(out_path)

# # 替换
# in_path = '替换.xlsx'
# read_data = pd.read_excel(in_path)
# # new_data = read_data.replace('城八区', '海淀区') # 修改数据需要常见新的数据, 或者用inplace
# # read_data.replace('城八区', '海淀区', inplace=True)
# # read_data['城市2'].replace('城八区', '海淀区', inplace=True) # 只替换某个列
# # read_data['城市2'] = read_data['城市2'].str.replace('城八', '市') # 只替换列中的某个字符串
# # 用字典定义进行数值替换
# # dict = {'A':20, 'B':30, 'C':40, 'D':50, 'E':60, 'F':70, 'G':80}
# # read_data['数值'].replace(dict, inplace=True)
# # 也可以用列表的方式进行数值替换
# # read_data['数值'].replace(['A','B'], 30, inplace=True)
# # read_data['数值'] = read_data['数值'].str.replace('[A-Z]', 88, regex=True, inplace=True) # 这个好像行不通
# read_data.replace('[A-Z]', 88, regex=True, inplace=True)
# print(read_data)

# # 分箱 一定是对一维数字进行操作
# 年份 = [1992, 1983, 1922, 1932, 1973]
# 箱子 = [1900, 1950, 2000]
# # 结果 = pd.cut(年份,箱子)
# # 结果 = pd.cut(年份,箱子,labels=False) #显示箱号, 从0开始编号
# 箱子名称 = ['50年代以前','50年代以后']
# 结果 = pd.cut(年份,箱子,labels=箱子名称) #用labels将箱子名称赋给不同的箱子
# # 等频分箱
# 年份 = [1992, 1983, 1922, 1932, 1973, 1963, 1981, 1997]
# 结果 = pd.qcut(年份, q=4)
# print(结果)
# print(pd.value_counts(结果))

# # 字符串操作
# in_path = '字符串.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data)
# print(read_data['温度'].str.replace('℃','').astype('int64'))
# # 分隔一个提取的字符串 str.cat
# # print(read_data['姓名'].str.cat(sep='、'))
# print(read_data['姓名'].str.cat([';']*len(read_data['姓名']))) # 每个名字后面都加上一个指定的字符
# # print(read_data['姓名'].str.cat([';']*len(read_data['姓名']), sep='^')) # 在和指定的中间加一个分隔符
# print(read_data['姓名'].str.cat([';']*len(read_data['姓名']), sep='^', na_rep='None')) # 把NaN替换为指定的字符
# # str.split
# print(read_data['状态'].str.split())
# print(read_data['状态'].str.split('血')) # 和python内置的split的用法是一样的
# print(read_data['状态'].str.split('血', expand=True)) # 先分割在分列
# print(read_data['状态'].str.partition('血')) # 按照指定字符分割, 分割的字符也是一列
# # str.get
# print(read_data['状态'].str.get(2)) # 从0开始提取字符, 只能传整型
# # str.slice
# print(read_data['状态'].str.slice(0)) # 从0开始都提取
# print(read_data['状态'].str.slice(0,3)) # 从0开始都提取到2
# print(read_data['状态'].str.slice(0,4,2)) # 从0开始都提取到4，隔2个去一次
# print(read_data['状态'].str.slice_replace(1,3,'xxx')) # 从第1个提取到第2个，然后用指定的字符串替代
# # str.join
# print(read_data['状态'].str.join('502')) # 将每一个字符中间用指定的字符串连接
# # str.contains
# print(read_data['状态'].str.contains('血')) # 判断是否包含某个指定的字符
# print(read_data['状态'].str.contains('血', na='没有')) # na用没有替代
# # str.startswith
# print(read_data['状态'].str.startswith('满', na='没有')) #
# # str.repeat
# print(read_data['姓名'].str.repeat(3))
# # str.pad 用指定的字符填充到满足定义的宽度
# read_data.fillna("XXX", inplace=True)
# print(read_data['姓名'].str.pad(5, fillchar="&")) # 默认是从左边开始补齐
# print(read_data['姓名'].str.pad(5, fillchar="&", side='right')) # 设置从右边开始补
# # str.zfill 用0填充
# print(read_data['姓名'].str.zfill(10)) # 用0填充到宽度为10
# # str.strip
# print(read_data['里程'].str.strip('中远近离')) # 去除指定的字符串
# # str.get_dummies
# print(read_data['里程'].str.get_dummies('距')) # 用指定字符分割，得到列表
# # str.translate
# dict = str.maketrans({'距':'ju','离':'li'})
# print(read_data['里程'].str.translate(dict)) # 用字典进行翻译
# # find
# print(read_data['日期'].astype('str')) #所有的日期必须都要先转换为字符型才能用str操作
# print(read_data['日期'].astype('str').str.find('-',5)) # 从指定的位置开始找，找不到就返回-1
# # 正则表达式
# print(read_data['状态'].str.match('.{2}激',na=False)) # 匹配成功了就返回True
# print(read_data['日期'].astype('str').str.extract('\d{4}-(\d{2})-(\d{2})')) # ()就是分组提取匹配的
# print(read_data['日期'].astype('str').str.replace('(\d+)-(\d+)-(\d+)','\3/\2/\1')) # 替换出来是乱码?
# print(read_data['日期'].astype('str').str.replace('(\d+)-(\d+)-(\d+)',r'\3/\2/\1')) # 用r就可以了

# # Excel文件的拆分与合并
# in_path='课件025-2/'
# out_path='合并表.xlsx'
# 合并表 = pd.DataFrame() # 为了合并，先用DataFrame创建一个空的表格
# for file in os.listdir(in_path):
#     # 表格 = pd.read_excel(in_path + file)
#     表格 = pd.read_excel(in_path + file, header=1) # 默认表头就是header=0
#     # file_path = os.path.join(in_path, file)
#     # 表格 = pd.read_excel(file_path)
#     # print(表格)
#     合并表 = pd.concat([合并表,表格])
# print(合并表.reset_index(drop=True))
# 合并表.to_excel(out_path)

# in_path = '合并2.xlsx'
# 数据 = pd.read_excel(in_path, None) # None表示读取所有Sheet的数据
# 合并表 = pd.DataFrame()
# 字段名 = list(数据.keys())
# for 列标签 in 字段名:
#     新数据 = 数据[列标签]
#     合并表 = pd.concat([合并表,新数据])
# print(合并表)

# in_path = '拆分.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data)
# 分割列 = list(read_data['部门'].drop_duplicates()) # 对部门进行list，并且先去重
# print(分割列)
#
# # # 拆分成多个工作表
# # 新数据 = pd.ExcelWriter('拆分结果.xlsx')
# # for i in 分割列:
# #     数据1 = read_data[read_data['部门'] == i]
# #     数据1.to_excel(新数据,sheet_name=i)
# # 新数据.save()
# # 新数据.close()
#
# # # 拆分成多个工作薄
# for i in 分割列:
#     数据1 = read_data[read_data['部门'] == i]
#     数据1.to_excel(i + '.xlsx')

# # 分组聚合groupby agg
# in_path = '分组聚合.xlsx'
# # read_data = pd.read_excel(in_path)
# read_data = pd.read_excel(in_path, index_col='城市') # 如果要通过函数的方法来分组，把需要分组的列设置为索引
# print(read_data)
# new_data = read_data.groupby(len).sum() # 通过index的长短来分组聚合
# print(new_data)
# # for (i,j),group in read_data.groupby(['城市', '区']):
# #     print(group)
# #     print(i, j)
# new_data = read_data.groupby(['城市','区'])[['人数', '金额']].sum() # 按城市，区来分组，按人数金额来聚合, 聚合函数是sum
# print(new_data)
# new_data.to_excel('分组聚合结果.xlsx')

# # agg函数，一版和groupby配合使用, 是基于列的聚合操作
# in_path = '分组聚合2.xlsx'
# # read_data = pd.read_excel(in_path)
# read_data = pd.read_excel(in_path, index_col='店号')
# print(read_data)
# 对应关系 = {'1月':'一季度','2月':'一季度','3月':'一季度','4月':'二季度'}
# # 对应关系 = {'1月':'mean','2月':'mean','3月':'mean','4月':'mean'}
# new_data = read_data.groupby(对应关系,axis=1).agg(sum) # agg的意思就是聚合,聚合的操作可以跟在分组后面，也可以后面再操作
# # new_data = read_data.groupby(对应关系,axis=1).sum()  # 不显示店号，需要在前面读入的时候指定index_col
# # new_data = read_data.groupby(对应关系,axis=1)  # 可以只分组，sum或者别的结果可以放到后面
# # print(new_data.sum())
# print(new_data)

# in_path = '分组聚合3.xlsx'
# read_data = pd.read_excel(in_path, index_col=[0, 1])
# print(read_data)
# # new_data = read_data.groupby(level='班级').mean()
# # new_data = read_data.groupby(level='班级').agg('mean') # 这个和上面的用法结果是一样的
# # new_data = read_data.groupby(level='性别').max()
# new_data = read_data.groupby(level='性别').agg(max) # 这个和上面用法结果一样
# print(new_data)

# in_path = '分组聚合4.xlsx'
# read_data = pd.read_excel(in_path, header=[0,1])
# print(read_data)
# # 创建两个列表为了多层索引
# L1 = ['1季度','1季度','1季度','2季度','2季度']
# L2 = ['1月','2月','3月','4月','5月']
# 多层索引 = pd.MultiIndex.from_arrays([L1, L2], names=['季度','月份'])
# new_data = pd.DataFrame(read_data, columns=多层索引)
# print(new_data)
# group_data = new_data.groupby(level='季度', axis=1)
# print(group_data.sum())

# # # groupby用法详解
# company=["A","B","C"]
# data=pd.DataFrame({
#     "company":[company[x] for x in np.random.randint(0,len(company),10)],
#     "salary":np.random.randint(5,50,10),
#     "age":np.random.randint(15,50,10)
# })
# print(data)
# # new_data = data.groupby('company').agg('mean')
# # new_data = data.groupby('company').agg({'salary':'median','age':'mean'}) # 这里agg里面的操作也可以用字典来实现
# # print(new_data)
#
# # # transform 把每个公司的平均值映射到每个公司后面, 用法和agg类似
# # data['avg_salary'] = data.groupby('company')['salary'].transform('mean') # 这个理解的意思就是按company来分组，按salary来聚合
# # '''
# # 这一行脚本的意思就是：再原先data表格后面添加新的一列，通过company的分组，然后对salary那一列求分别的平均值，并且把这个平均值分别映射到各个公司
# # '''
# # print(data)
# # # 如果不用transform:
# avg_salary_dict = data.groupby('company')['salary'].mean().to_dict() # 这个好厉害！！！
# data['avg_salary'] = data['company'].map(avg_salary_dict)
# print(data)

# # 分组对象和创建
# in_path = '分组.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data)
# # new_data = read_data.groupby(read_data.index % 2 ==0)[['数学','语文','英语']].sum()
# # new_data = read_data.groupby([read_data.姓名.str[0], read_data.姓名.str[1:]])[['数学','语文','英语']].sum()
# # new_data = read_data.groupby(read_data.班级)[['数学','语文','英语']].sum()
# # new_data = read_data.groupby([read_data.班级,read_data.性别])[['数学','语文','英语']].sum()
# # new_data = read_data.groupby([read_data.时间.dt.day, read_data.时间.dt.hour])[['数学','语文','英语']].sum()
# # # pipe
# # new_data = read_data.pipe(pd.DataFrame.groupby, '班级').sum()
# new_data = read_data.pipe(pd.DataFrame.groupby, '性别').sum()
# print(new_data)

# # 举个统计商品的例子吧
# n = 1000
#
# df = pd.DataFrame(
#     {
#         "Store": np.random.choice(["Store_1", "Store_2", "Store_3"], n),
#         "Product": np.random.choice(["Product_1", "Product_2", "Product_3"], n),
#         "Revenue": (np.random.random(n) * 50 + 10).round(2),
#         "Quantity": np.random.randint(1, 10, size=n),
#     }
# )
#
# print(df.head(10))
#
# result = df.groupby([df.Store, df.Product])['Revenue', 'Quantity'].agg('mean')
# print(result)

# # groupby 和 pipe
# # df = pd.DataFrame({'A':['a','b','a','b'], 'B':[5, 9, 4, 12]}) # 数字后面要运算不能加''
# df = pd.DataFrame({'A':'a b a b'.split(), 'B':[5, 9, 4, 12]}) # 字典A可以用str的方式+split
# print(df)
# result = df.groupby('A').pipe(lambda x: x.max()-x.min())
# print(result)

# # 数据透视表
# in_path = '透视.xlsx'
# out_path = '透视结果.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data.head())
# # # read_data = pd.read_excel(in_path, index_col=[1,2])
# # # new_data = pd.pivot_table(read_data, index=['部门', '销售人员'])
# # # new_data = pd.pivot_table(read_data, index=['部门', '销售人员'], values=['数量','金额']) # 只透视指定的列, 结果是平均值，为什么？
# # new_data = pd.pivot_table(read_data, index=['部门', '销售人员'], values=['数量','金额'], aggfunc=[sum, np.mean])
# # # new_data = pd.pivot_table(read_data, index=['部门', '销售人员'], values=['数量','金额'], fill_value=0)
# # # new_data = pd.pivot_table(read_data, index=['部门', '销售人员'], values=['数量','金额'], aggfunc='mean', columns=['所属区域']) #
# # # new_data = pd.pivot_table(read_data, index=['部门', '销售人员'], values=['数量','金额'], aggfunc='sum', columns=['所属区域']) #
# # print(new_data)
# # # new_data.to_excel(out_path)
# # # 交叉表，主要用来计数的
# new_data = pd.crosstab([read_data.日期.dt.month, read_data.所属区域], read_data.部门, margins=True) #
# '''
# 用日期和所属区域来做index分类，通过各个部门条目来计算记录的条数，margnis表示是否计总数
# '''
# print(new_data)

# # vlookup
# in_path = 'Vlookup.xlsx'
# 花名册 = pd.read_excel(in_path, sheet_name='花名册')
# 成绩单 = pd.read_excel(in_path, sheet_name='成绩单')
# # 结果 = pd.merge(花名册, 成绩单, on='学号')
# 结果 = pd.merge(花名册, 成绩单.loc[:,['学号','总分']], on='学号') # loc表示， 成绩单表格中选取所有行，但是列只要两列
# # print(花名册)
# # print(成绩单)
# print(结果)
# # 改变列的顺序
# 结果_总分 = 结果.总分 # 把总分那一列定义为一个变量
# 结果 = 结果.drop('总分', axis=1) # 把表格中的那一列删除掉
# 结果.insert(0, '总分', 结果_总分) # 把定义的变量插入到指定的列
# print(结果)

# # map allpy applymap
# in_path = '数据.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data.head())
# # 用map首先要构建一个字典,或者函数，只能传递一个参数
# # dict = {'男':'先生','女':'女士'}
# # read_data['称呼'] = read_data['性别'].map(dict)
# # 还可以用定义函数的方式
# def 替换(x):
#     称呼='先生' if x == '男' else '女士'
#     return 称呼
# read_data['称呼'] = read_data['性别'].map(替换)
# 用apply可以传递多个参数
# def 修改分数(x, 误差值):
#     return x+误差值
# read_data['语文'] = read_data['语文'].apply(修改分数, args=(-3,))
# print(read_data.head())
# # 对某一列执行指定的操作
# result = read_data[['语文', '数学', '英语']].apply('mean', axis=0)
# print(result)
# # 对某一行执行指定的操作
# def BMI(read_data):
#     身高 = read_data['身高']
#     体重 = read_data['体重']
#     BMI = 体重 / 身高 ** 2
#     return BMI
# read_data['BMI'] = read_data.apply(BMI, axis=1)
# print(read_data)
# # applymap
# in_path = '数据2.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data.head())
# new_data = read_data.applymap(lambda x:"%.3f" % x)
# print(new_data)

# # 转置
# in_path = '转换.xlsx'
# read_data = pd.read_excel(in_path)
# print(read_data.head())
# new_data = pd.DataFrame(read_data.values.T, index=read_data.columns, columns=read_data.index)
# print(new_data)

# # 环比
# in_path = '环比.xlsx'
# read_data = pd.read_excel(in_path, 'Sheet1')
# # print(read_data.head())
# 上月销售金额 = read_data.销售金额.shift()
# 环比 = read_data.销售金额 - 上月销售金额
# read_data['环比增长金额'] = 环比
# print(read_data)

# read_data = pd.read_excel(in_path, 'Sheet2')
# # print(read_data.head())
# def 公式(新数据):
#     新数据['环比'] = 新数据.金额 - 新数据.金额.shift()
#     return 新数据
# # new_data = read_data.sort_values(['城市', '月份']).groupby('城市').apply(公式)
# new_data = read_data.groupby('城市').apply(公式)
# print(new_data)

# # 同比
# in_path = '同比.xlsx'
# read_data = pd.read_excel(in_path, 'Sheet1')
# print(read_data.head())
# print('*'*30)
# 年 = read_data['日期'].dt.year
# new_data = pd.pivot_table(read_data, index='店号', values='金额', columns=年, aggfunc='sum')
# new_data['同比'] = (new_data[2019] - new_data[2018])/new_data[2018] # 这里应用年的时候为什么不加''?
# print(new_data)

# # 工时练习
# in_path = '2021工时.xlsx'
# out_path = 'temp.xlsx'
# 内饰工时 = pd.read_excel(in_path, sheet_name='内饰')
# 汇总表 = pd.DataFrame()
# print(内饰工时.head())
# for i in 内饰工时.index:
#     name = 内饰工时.loc[i,'姓名']
#     新工时表 = pd.DataFrame({
#         '月份' : ['1月','2月','3月','4月','5月', '6月','7月','8月','9月','10月','11月','12月'],
#         '工时' : [
#             内饰工时.loc[i, '1月'], \
#             内饰工时.loc[i, '2月'], \
#             内饰工时.loc[i, '3月'], \
#             内饰工时.loc[i, '4月'], \
#             内饰工时.loc[i, '5月'], \
#             内饰工时.loc[i, '6月'], \
#             内饰工时.loc[i, '7月'], \
#             内饰工时.loc[i, '8月'], \
#             内饰工时.loc[i, '9月'], \
#             内饰工时.loc[i, '10月'], \
#             内饰工时.loc[i, '11月'], \
#             内饰工时.loc[i, '12月'],
#             ],
#         '姓名' : ['XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX']
#     })
#     新工时表.replace('XXX', name, inplace=True)
#     汇总表 = pd.concat([汇总表, 新工时表])
# 汇总表.to_excel(out_path, index=False)

# in_path = 'temp.xlsx'
# out_path = 'temq.xlsx'
# data = pd.read_excel(in_path, index_col='月份')
# new_data = data.sort_index(inplace=False)
# new_data.to_excel(out_path)
# # new_data = data.sort_values(by='月份', axis=0, inplace=True, ascending=False)
# # print(new_data)
