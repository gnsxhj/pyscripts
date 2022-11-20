import os
import json
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

import seaborn as sns
import matplotlib.pyplot as plt

os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/exercise')

# # 练习一
# in_path = 'example.txt'
#
# # print(open(in_path).readline())
# records = [json.loads(line) for line in open(in_path)]
# time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# frame =pd.DataFrame(records)
# # # frame.info()
# # # 分析前十的时区数量
# # # print(frame['tz'][:10])
# # # tz_counts = frame['tz'].value_counts() # 对tz下面的值进行计数
# # clean_tz = frame['tz'].fillna('Missing')
# # clean_tz[clean_tz == ''] = 'Unknown'
# # tz_counts = clean_tz.value_counts()
# # subset = tz_counts[:10]
# # sns.barplot(y=subset.index, x=subset.values)
# # plt.show()
# # # # 对a列数据进行分析
# # results = pd.Series([x.split()[0] for x in frame.a.dropna()]) # 对每一行的a列数据进行split, 取第一个值
# # a0_counts = results.value_counts()[:8]
# #
# # cframe = frame[frame.a.notnull()]
# # # print(cframe['a'].str.contains('Windows'))
# # cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
# # by_tz_os = cframe.groupby(['tz', 'os'])
# # agg_counts = by_tz_os.size().unstack().fillna(0)
# # indexer = agg_counts.sum(1).argsort()
# # count_subset = agg_counts.take(indexer[-10:])
# # count_subset = count_subset.stack()
# # count_subset.name = 'total'
# # count_subset = count_subset.reset_index()
# # # sns.barplot(x='total', y='tz', hue='os', data=count_subset)
# # # plt.show()
# # def norm_total(group):
# #     group['normed_total'] = group.total / group.total.sum()
# #     return group
# # results = count_subset.groupby('tz').apply(norm_total)
# # print(results)
# # sns.barplot(x='normed_total', y='tz', hue='os', data=results)
# # plt.show()

# # 练习二
# pd.options.display.max_rows = 10
# unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
# users = pd.read_table('users.dat', sep='::', header=None, names=unames)
# # print(users.head())
# rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
# ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames)
# print(ratings.head())
# mnames = ['movie_id', 'title', 'genres']
# movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames, encoding='ISO-8859-1')
# # print(movies.head())
# data = pd.merge(pd.merge(users, ratings), movies)
# print(data.head())
# # print(data.iloc[0])
# # mean_ratings = pd.pivot_table(data, index=['title'], values=['rating'], aggfunc='mean', columns=['gender'])
# mean_ratings = data.pivot_table('rating', index='title', aggfunc='mean', columns='gender')
# ratings_by_title = data.groupby('title').size() # 按照title来分组，并且计算每个title的条目数
# active_titles = ratings_by_title.index[ratings_by_title >= 250] # 通过条目数量来判定选取的index的目标
# mean_ratings = mean_ratings.loc[active_titles] # 通过active_titles来筛选
# top_femal_ratings = mean_ratings.sort_values(by='F', ascending=False) # 对F列进行排序
# mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F'] # 对M列和F列求差值
# sorted_by_diff = mean_ratings.sort_values(by='diff')
# # print(sorted_by_diff[:10])
# # print(sorted_by_diff[::-1][:10]) # 倒序前10
# ratings_std_by_title = data.groupby('title')['rating'].std() # 按照title来分组，对ratings列来进行方差计算
# ratings_std_by_title = ratings_std_by_title.loc[active_titles]
# print(ratings_std_by_title.sort_values(ascending=False)[:10])

# # # 练习三
# names1880 = pd.read_csv('yob1880.txt', names=['name', 'sex', 'births'])
# # print(names1880.head())
# # sex_sum = names1880.groupby('sex').births.sum() # 注意一下这个用法 !!!
# sex_sum = names1880.groupby('sex')['births'].sum()
# years = range(1880, 2011)
# pieces = []
# columns = ['name', 'sex', 'births']
# for y in years:
#     path = 'yob%d.txt' % y
#     frame = pd.read_csv(path, names=columns)
#     frame['year'] = y
#     # names = pd.concat([frame], ignore_index=True) # 直接再循环里面concat好像不行, 会循环覆盖掉
#     pieces.append(frame)
# names = pd.concat(pieces, ignore_index=True) # concat将多个DataFrame组合到一起, 这里pieces就是多个dataframe的List
# total_births = names.pivot_table('births', index='year', aggfunc='sum', columns='sex')
# # print(total_births.tail())
# # total_births.plot(title='Total births by sex and year')
# # plt.show()
# def add_prop(group):
#     group['prop'] = group.births / group.births.sum()
#     return group
# # names = names.groupby(['year', 'sex']).apply(add_prop) # 根据year sex进行分组，对每一个分组执行函数
# # print(names.groupby(['year','sex']).prop.sum()) # 验证一下prop的和为1
# grouped = names.groupby(['year','sex'])
# names = grouped.apply(add_prop) #
# # print(names.head())
# def get_top1000(group):
#     top_1000 = group.sort_values(by='births', ascending=False)[:1000] # 排序，然后选择前1000名
#     return top_1000
# grouped = names.groupby(['year','sex'])
# top1000 = grouped.apply(get_top1000)
# top1000.reset_index(inplace=True, drop=True) # 重置索引列，之前的索引列被直接删除
# # print(top1000.head())
# # # 用函数的方法实现top1000
# # pieces = []
# # for year, group in names.groupby(['year','sex']):
# #     pieces.append(group.sort_values(by='births', ascending=False)[:1000])
# # top1000 = pd.concat(pieces, ignore_index=True)
# # print(top1000.head())
#
# # 把前1000个名字分男女
# # boys = top1000[top1000.sex == 'M']
# # girls = top1000[top1000.sex == 'F']
# # # 对to1000进行求和透视, 用name作为列
# # total_births = top1000.pivot_table('births', index='year', aggfunc='sum', columns='name')
# # # 用DataFrame的plot方法绘制选定名字的曲线
# # subset = total_births[['Alice', 'Tom', 'Mike', 'Jack']]
# # subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
# # plt.show()
#
# # # 分析top1000的名字所占的比例, 按year和sex进行聚合
# # table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc='sum')
# # table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
# # plt.show()
#
# # # 计算占比50%名字个数
# # df_boys_2010 = boys[boys.year == 2010]
# # prop_cumsum = df_boys_2010.sort_values(by='prop', ascending=False).prop.cumsum()
# # # print(prop_cumsum.values.searchsorted(0.5))
# # df_boys_1900 = boys[boys.year == 1900]
# # in1900 = df_boys_1900.sort_values(by='prop', ascending=False).prop.cumsum()
# # # print(in1900.values.searchsorted(0.5)+1)
# # def get_quantile_count(group, q=0.5): # 找到占比50%的名字位置
# #     group = group.sort_values(by='prop', ascending=False)
# #     return group.prop.cumsum().values.searchsorted(q) + 1
# # diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
# # diversity = diversity.unstack('sex') # 如果有多层索引，unstack进行索引转换
# # # print(diversity.tail())
# # diversity.plot(title="Number of popular names in top 50%")
# # plt.show()
#
# # # 最后一个字母的统计
# get_last_letter = lambda x: x[-1] # 传递一个字符串x, 然后截取字符串的最后一个字母
# last_letters = names.name.map(get_last_letter) # 选取names表格的name列，然后通过map调用函数，截取最后一个字母
# last_letters.name = 'last_letter' # 上面一步返回的也是一个表，这里指定这一列的名字
# # print(last_letters.head())
# table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)
# # print(table.head())
# # # 选取其中三年数据显示, 通过reindex重置索引
# # subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
# # print(subtable.head())
# # print(subtable.sum())
# # letter_prop = subtable / subtable.sum()
# # print(letter_prop.head())
# #
# # fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# # letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# # letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
# # plt.show()
#
# # # 对整表进行求比例
# # letter_prop = table / table.sum()
# # # print(letter_prop.head())
# # # 选取男性以dny三个字母结尾进行分析. T 进行转置
# # dny_ts = letter_prop.loc[['d','n','y'], ['M']].T
# # # print(dny_ts.head())
# # dny_ts.plot()
# # plt.show()
#
# # # 同一个名字随时间的性别差异
# all_names = pd.Series(top1000.name.unique()) # 创建一维表格,把top1000的名字提取出来
# lesley_like = all_names[all_names.str.lower().str.contains('lesl')] # 过滤名字
# filtered_name = top1000[top1000.name.isin(lesley_like)]
# filtered_name.groupby('name').births.sum()
# table = filtered_name.pivot_table('births', index='year', columns='sex', aggfunc='sum')
# table = table.div(table.sum(1), axis=0) # 这个1在这里是什么意思? 不懂！
#
# table.plot(style={'M': 'k-', 'F': 'k--'})
# plt.show()

# # 暂停