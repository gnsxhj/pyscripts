import sys
#1.1
def combine_sample():
    yield "www."
    yield "w3cschool."
    yield "cc"
# (a) simple join operator
text = ''.join(combine_sample())
print("菜鸟教程旧地址: ", text)
print("菜鸟教程旧地址: ", text.replace("w3cschool.cc", "runoob.com"))

#1.2)字符串里日期搜索-正则法
import re

# some sample text
text = 'Today is 11/27/2012. Pycon starts 3/13/2012.'

# (a) Find all matching dates
# re.compile(pattern[,flags]) 编译正则表达式，生成一个Pattern对象，供match()和search()函数使用
# pattern: 一个字符串形式的正则表达式
# flags: re.I 忽略大小写；re.M 多行模式
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four') #查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10) #从'1'的位置开始匹配，有匹配
print(m.group())

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I) #re.I 表示忽略大小写
m = pattern.match('This is a text line for testing!')
print(m)

datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.findall(text))

# (b) find all matching dates with capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall((text)):
    print('{}-{}-{}'.format(year,month,day))
    print(f'{year}-{month}-{day}')

# (c) Iterative search
for m in datepat.finditer(text):
    print(m.groups())

#1.3)字符串里日期替换-正则法
from calendar import month_abbr
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# (a) Simple substitution
print(datepat.sub(r'\3-\1-\2', text))

# (b) Replacement function
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

#1.4).字符串关键字搜索-1
from fnmatch import fnmatchcase as match
addresses = [
    '54123 N GREEN ST',
    '54124 X ORANGE ST',
    '54211 Y YELLOW AVE',
    '54222 Z RED ST',
    '311 K BLUE ',
    ]

a = [addr for addr in addresses if match(addr, '* ST')]
print(a)

b = [addr for addr in addresses if match(addr, '542[0-9][0-9] *ST*')]
print(b)

#1.5).长字符串排版切割
import textwrap
s = "If you want to help to develope Python, take a look at the developer area for further information.\
 Please note that you don't have to be an expert programmer to help.\
 The documentation is just as important as the compiler, and still needs plenty of work!"

print(textwrap.fill(s, 70))
print('\n')
print(textwrap.fill(s, 40))
print('\n')
print(textwrap.fill(s, 40, initial_indent='   '))

#1.6).字符串里面可变数据的动态替换
# 普通方法
name = 'leo'
n = 37
s = '{} has {} messages.'.format(name,n)
print(s)

# 高级方法
s = '{name} has {n} messages.'
print(s.format_map(vars()))

# 天外飞仙法
class safesub(dict):
    def __missing__(self, key):
        return '{%s}' % key
s = '{name} has {n} messages.'
name = 'leo'
n = 100
print(s.format_map(safesub(vars())))

prices = {
    'Apple': 145.23,
    'Aliyun': 112.78,
    'Tencent ': 105.55,
    'HP ': 37.20,
    'Google ': 100.75
}

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price: ', min_price)
print('max price: ', max_price)

print('sorted prices: ')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('              ', name, price)

from pprint import pprint

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }

print("All prices over 200: ")
pprint(p1)

# Make a dictionary of each stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = { key:value for key,value in prices.items() if key in tech_names }

print("All techs")
pprint(p2)

#2.3).提取字典里面相同的部分

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
print('Common keys: ', a.keys() & b.keys())
print('Keys in a not in b: ', a.keys() - b.keys())
print('(key, value) pairs in common: ', a.items() & b.items())

#2.4).合并字典
from collections import ChainMap
a = {
    'x' : 1,
    'z' : 3
}
b = {
    'y' : 2,
    'z' : 4
}
# (a) Simple example of combining
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])

#3.列表相关
#3.1)#过滤列表方法-青铜
mylist = [1,4,-5,10,-7,2,3,-1]
# All positive values
positive_value = [n for n in mylist if n > 0]
print(positive_value)
# All negative values
negative_value = [n for n in mylist if n < 0]
print(negative_value)

#3.2 过滤表方法
# Negative values clipped to 0
negative_clip = [n if n < 0 else 0 for n in mylist]
print(negative_clip)
# positive values clipped to 0
positive_clip = [n if n > 0 else 0 for n in mylist]
print(positive_clip)

#3.3 过滤列表方法
from itertools import compress
addresses = [
    '123 N apple',
    '234 N yahoo',
    '457 E google',
    '212 N ibm',
    '987 N hp',
    '653 W ali',
    '487 N baidu',
    '109 W xiaomi'
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(more5)
a = list(compress(addresses, more5))
print(a)

#3.4) 统计频率最高的单词
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
print(word_counts)
top_three = word_counts.most_common(3)
print(top_three)

# Example of merging in more words

morewords = ['how', 'are', 'you']
word_counts.update(morewords)
print(word_counts)

# 3.5)列表搜索
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 70},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# 3.6) 列表搜索
# heapq
import heapq
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]
print(heapsort([1, 3, 5, 7, 9, -1, 2, -20, 8, 0]))

# lambda
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1,2))

portfolio = [
    {'name': 'ali', 'shares': 100, 'price': 91.1},
    {'name': 'baidu', 'shares': 50, 'price': 543.22},
    {'name': 'yahoo', 'shares': 200, 'price': 21.09},
    {'name': 'tencent', 'shares': 35, 'price': 31.75},
    {'name': 'pingduoduo', 'shares': 45, 'price': 16.35},
    {'name': 'sina', 'shares': 75, 'price': 115.65}
]

cheap  = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive  = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print('cheap: ', cheap)
print('expensive: ', expensive)

# 3.7) 复杂列表分类 - group法
from itertools import groupby
rows = [
 {'city': 'nanjing', 'date': '07/01/2012'},
 {'city': 'beijing', 'date': '07/04/2012'},
 {'city': 'shanghai', 'date': '07/02/2012'},
 {'city': 'suzhou', 'date': '07/03/2012'},
 {'city': 'guangzhou', 'date': '07/02/2012'},
 {'city': 'tianjin', 'date': '07/02/2012'},
 {'city': 'chengdu', 'date': '07/01/2012'},
 {'city': 'wuxi', 'date': '07/04/2012'},
]

rows.sort(key=lambda r: r['date'])
for date, items in groupby(rows, key=lambda r: r['date']):
    print(date)
    for i in items:
        print('    ', i)

# 3.8) 复杂列表分类方法 - defaultdict法
rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from collections import defaultdict
rows_by_date = defaultdict(list)

rows.sort(key=lambda r: r['date'])
for i in rows:
    rows_by_date[i['date']].append(i)

for r, v in rows_by_date.items():
    print(r, v)

#3.9)复杂列表的分类
records = [
 ('Apple', 'Good', 20),
 ('IBM', 'common'),
 ('Apple', 'better', 19),
 ('IBM', 'excellent'),
]

def do_apple(x, y):
    print('Apple:', x, y)

def do_IBM(s):
    print('IBM:', s)

for tag, *args in records:
    if tag == 'Apple':
        do_apple(*args)
    elif tag == 'IBM':
        do_IBM(*args)
#这里设计得非常巧妙，利用*args这一招巧妙对tuple元素进行切割，分类

#3.10)复杂列表数据mapping-namedtuple法
from collections import namedtuple
records = [
    ('GOOG', 100, 490.1),
    ('ACME', 100, 123.45),

    ('IBM', 50, 91.15)
]

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

print(compute_cost(records))

#3.11) 列表重复数据的删除并保序
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ =='__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    print(list(dedupe(a)))

#yield
def foo():
    print("starting ... ")
    while True:
        res = yield 4 #类似于return 赋值给了res后程序停止
        print("res:", res) #上一步return出去了，所以这里res的赋值就是none
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(next(g))

def foo():
    print("starting ... ")
    while True:
        res = yield 4
        print("res:", res)
g = foo()
print(next(g))
print("*"*20)
print(g.send(7))
#send是发送一个参数给res, return的时候并没有把4赋值给res,
#下次执行的时候只好继续执行赋值操作，只好赋值为none,如果遇到send,开始执行的时候，接着上次(return 4)执行
#先把7赋值给了res,然后执行next的作用，遇到下一个yield, return除结果后结束

# 用range生成list很占内存，所以可以用yield组合成生成器
# for n in range(100):
#     a = n
#     print(a)
def foo(num):
    print("starting ... ")
    while num < 10:
        num += 1
        yield num
for n in foo(0):
    print(n)

#3.12)重复列表重复数据的删除并保存
def dedupe(items, key=None):
    seen = set()
    for i in items:
        val = i if key is None else key(i)
        if val not in seen:
            yield i
            seen.add(val)
if __name__ == '__main__':
    a = [
        {'x': 2, 'y': 3},
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 4},
        {'x': 10, 'y': 15}
    ]
    print(a)
    print(list(dedupe(a, key=lambda a: (a['x'], a['y']))))

#3.13)复杂列表的排序
from operator import itemgetter
from pprint import pprint

rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print("Sorted by fname: ")
pprint(rows_by_fname)

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print("Sorted by uid: ")
pprint(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print("Sorted by lnam, fname: ")
pprint(rows_by_lfname)

# #3.14)复杂对象的排序
from operator import attrgetter
class User:
    def __init__(self, user_id, user_name, user_age):
        self.user_id = user_id
        self.user_name = user_name
        self.user_age = user_age

    def __repr__(self):
        return 'User(id:{}, name:{}, age:{})'.format(self.user_id,self.user_name,self.user_age)

users = [User('0002','aa',31), User('0001','ab',30), User('0003','ac',20)]
print('user:', users)

#3.15 碾平一个序列
#
# from collections import Iterable
#
# def flatten(items, ignore_types=(str, bytes)):
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x)
#         else:
#             yield x
# # items =  [1, 2, [3, 4, [5, 6], 7], 8]
#
# items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
# for x in flatten(items):
#     print(x)

#3.16) 连接多个列表
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
c = [True, False, True]
print(list(chain(a, b, c)))

#3.17)合并多列表排序
import heapq
a = [1, 3, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
#
#4.1

class Countdown:
    def __init__(self, start):
       self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

c = Countdown(5)
print("Forward:")
print ([x for x in c])

print("Reverse:")
print([x for x in reversed(c)])

#class
class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print(f'{self.name}说：我{self.age}岁。')
p = people('runoob', 10, 30)
p.speak()
