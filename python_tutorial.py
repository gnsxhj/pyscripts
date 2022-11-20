# #输出和注释
# # print("hello world", end="\n") #输出,默认回车是结束
# # print("hello","world", sep="\t") #默认空格是分隔符
# # print("hello China!"+"I Love China")
# # print("hello world "*3) # *数字 表示重复
# # print("520"+"1314") #字符串可以双引号或者单引号
# # print(520+1314) #否则就是数字
# # print('I "love" you!')
# # print("I 'love' you!") #双引号或者单引号必须成对出现
# # print(r"C:\abc\def\nph.xls")
# # """
# # 1.多行注释
# # 2.
# # 3. ctrl + / 对选中的多行一起注释
# # """
#
# #变量与f格式化字符串
# # a=5
# # b=2
# # c=a
# # a,b,c=7,3,0 #多变量赋值
# # a=b=c=2
# # x = 5
# # y = 2
# # x,y = y,x #交换赋值
# # print(x,y)
# # name = "xuhaijun"
# # age = 40 #如果变量定义为数字就不能加“”，否则就会当作字符串处理
# # print(f'我的名字叫{name}, 今年的年龄是{age}岁')
# # print(f'我的名字叫{name}, 明年的年龄是{age+1}岁')
#
# #输入
# # name = input("please input your name:") #所有input默认都是字符串，是不能运算的
# # age = int(input("please input your age:")) #转换字符串为整型
# # print(f'你的姓名是{name}, 你的年龄是{age}岁')
# # print(f'你的姓名是{name}, 你明年的年龄是{age+1}岁')
#
# #数据类型转换
# # int(), float(), str()
# # type(): 检查数据类型
# # print(type(10/2)) #浮点类型
# # print(type(5//2)) #整数类型
#
# # #02课 字符串
# # # 下标和切片
# # str = "跟，着XYZ学习Python."
# # print(str[3:6:1])
# # print(str[3:])
# # print(str[::2])
# # print(str[:-1])
# # print(str[-4:-1])
# #
# # #find()从左向右
# # #rfind()从右向左查询
# # str = '只要地球不爆炸，我相信总有一天，全世界都说中国话！中国会成为全世界的风向标！'
# # print(str.find('中国'))
# # print(str.find('中国', 23, 32))
# # print(str.find('美国'))
# # #index和find的区别是查不到报错，find是报-1，其余一样
# # #count查找出现的次数
# #
# # #可变类型: 列表，字典，集合，变量值改变，id内存地址不变
# # #不可变类型: 整型，浮点，字符串，元组，变量值改变，id内存地址改变,需要修改变量，要进行重新定义变量名
# #
# # #replace 替换
# # print(str.replace('中国','China'))
# # print(str.replace('中国','China',2))
# #
# # #split 分割
# # str = "你好，世界！^你好，中国！^我们一起学习中文！"
# # print(str.split('^'))
# #
# # #join 合并
# # str = ['中','国','最','强']
# # print(str)
# # print("_".join(str))
# # print("".join(str))
# # print("...".join(str))
# # print(str)
# #
# # #startwith endwith
# # str = "你好，世界，你好，中国，祝伟大的祖国繁荣昌盛"
# # print(str.startswith('你好'))
# # print(str.endswith('繁荣昌盛'))
#
# # 03课 列表, 列表是可变数据
# list = ['abc', 'acb', 'bac', 'bca']
# print(list)
# print(f'列表中的第四个元素是：{list[3]}')
# # 切片
# print(list[1:3]) #第一个从0开始计数，最后一个不包含
# # index
# print(list.index('bac',0,4)) #找到返回下标数字，找不到报错
# # count
# print(list.count('abc'))
# # len
# print(len(list))
# # append 末尾追加单个数据
# list.append('cab')
# print(list)
# # extend 列表结尾增加多个数据, 需要用列表的方式[]
# list.extend(['efg', 'hij'])
# print(list)
# # insert 在指定位置插入数据
# list.insert(2, 'xyz')
# print(list)
# # del 删除; remove 移除; clear 清空列表
# del list[1]
# print(list)
# last = list.pop() #不带下标默认就是最后一个,可以用来取最后一个
# print(last)
# print(list)
# list.remove('abc') #移除第一个匹配项
# print(list)
# list.clear()
# print(list)
# list = [] #建立一个空列表
# print(list)
#
# # 修改
# list = ['abc', 'acb', 'bac', 'bca']
# list[1] = 'xyz'
# print(list)
# print(list[::-1])
# list.reverse()
# print(list)
# a = [1, 3, 4, 9, 6, 2]
# a.sort(reverse=False) #False首字母要大写
# print(a)
#
# #复制
# b = [1, 3, 5, 9, 6, 2]
# c = b.copy()
# print(b)
# print(c)
#
# #遍历列表
# list = ['abc', 'acb', 'bac', 'bca']
# for i in list:
#     if i == "abc":
#         print(i)
#
# list = [['abc', 'acb'], ['def', 'dfe'], ['xyz', 'xzy']]
# print(list[2][0]) #找到xyz
#
# #strip 删除开头或者结尾指定的字符，中间的不删除
# str = " ***this is **string** example ... wow!!!****   "
# print(str.strip())
# print(str.strip(" t*!"))
#
# # 元组, 不能被修改，操作方法就只有查询了
# tuple = () #定义空元组
# print(type(tuple))
# tuple = ('xyz') #单个数据不是元组，就是个字符串
# print(type(tuple))
# tuple = ('xyz',) #用逗号隔开，就是元组了
# print(type(tuple))
#
# tuple = ('abc', 'acb', 'xyz', 'xzy')
# print(tuple[1])
# print(tuple[1:3]) #切片
# print(tuple.index('abc')) #查询数据的下标
# print(tuple.count('xyz'))
# print(len(tuple)) #统计元组数据的个数
# tuple_n = tuple[0:2]+('def',)+tuple[2:]
# print(tuple_n)
#
# #字符串，列表，元组统称为序列！
# #类型转换 list(序列名) tuple(序列名)
#
# #04 if语句
# # height = float(input('Please input your height(m): '))
# # if height >= 1.3:
# #     print(f'Your height is {height}m, ticket please!')
# # else:
# #     print(f'Your height is {height}m, no ticket!')
# #
# # print('Have a nice journey!')
# #
# # age = int(input('Please input your age: '))
# # if age < 18:
# #     print(f'Your age is {age} years old.')
# # elif age > 70:
# #     print(f'Your age is {age} years old.')
# # else:
# #     print(f'Your age is {age} years old.')
# #
# # a = 3
# # b = 5
# # c = a if a > b else b
# # print(c)
#
# #05 字典与集合 字典用大括号，数据是键：值成对出现
# #什么时候用字典？当下标索引因为数据乱了不好用的时候用字典
# dict = {'huawei':520, 'xiaomi':320, 'apple':600, 'sumsung':550}
# dict['oppo']=430
# print(dict['xiaomi'])
# print(dict.get('oppo', 'None'))
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# for k in dict.keys():
#     print(k)
# for v in dict.values():
#     print(v)
# for i in dict.items():
#     print(i)
# for k, v in dict.items():
#     print(f'{k} = {v}')
#     if k == "xiaomi":
#         print(v)
#
# #set 可以用{} 或者 set()创建集合，创建空集合必须要用set(), 因为{}创建的空字典
# set = {1, 2, 3, 4, 5, 7, 9}
# print(set)
# set = {1, 2, 3, 4, 4, 5, 7, 9} #自动去重
# print(set)
# # n = set() #创建空集合
# # print(n)
# print(5 in set)
# print(10 in set)
# print(10 not in set)
# # set(序列) # 将某个序列转换成集合,集合自动去重，但不支持下标，没有顺序
# # 序列:
# # 有序序列： 有序，意味着有下标，可以进行下标操作、切片操作，列表，元组，字符串
# # 无序序列：字典、集合
# # 可变类型：列表、字典、集合
# # 不可变类型：整型、浮点型、字符串、元组
#
# #总结：
# #1、字符串：不能修改的字符序列。除了不能修改，可把字符串当成列表一样处理。
# #2、列表：我觉得列表就是我们日常生活中经常见到的清单。比如，统计过去一周我们买过的东西，把
# #这些东西列出来，就是清单。由于我们买一种东西可能不止一次，所以清单中是允许有重复项的。
# #3、元组：用来存放不能被轻易修改的数据，例如身份证号
# #4、字典：是除列表外python中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的
# #对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# #5、集合：目的就是去重复
#
# #for循环
# str = 'hello world!'
# for s in str:
#     print(s)
# list = ['abc', 'def', 'ghi', 'jkl']
# for l in list:
#     print(l)
# tuple = ('abc', 'def', 'ghi', 'jkl')
# for t in tuple:
#     print(t)
#
# #break
# str = '1234567890'
# for s in str:
#     if s == '7':
#         print('break at 7')
#         break
#     print(s)
#
# str = '1234567890'
# for s in str:
#     if s == '7':
#         print('continue at 7')
#         continue
#     print(s)
#
# #enumerate 用于将一个可遍历的数据对象(列表，元组或字符串)组合为一个索引序列，同时列出数据和数据下标
# list = ['abc', 'acb', 'bac', 'bca']
# for l in enumerate(list):
#     print(l)
#
# for k,v in enumerate(list):
#     print(f'下标是{k}, 对应的数据是{v}')
#
# #推导式，就是简化代码
# list = []
# for l in range(0,11):
#     list.append(l)
# print(list)
#
# list = [l for l in range(0, 11)]
# print(list)
#
# #创建[0, 2, 4, 6, 8, 10]
# list = [l for l in range(0, 11, 2)]
# print(list)
# list = []
# for l in range(0, 11, 2):
#     list.append(l)
# print(list)
# list = [l for l in range(0,11) if l %2 == 0]
# print(list)
#
# #字典推导式， 将两个列表快速合并成一个字典
# list_1 = ['huawei', 'xiaomi', 'apple', 'sumsung']
# list_2 = [500, 600, 40, 10] # 数字不能加引号，加了引号就是字符串了
# dict = {list_1[l]:list_2[l] for l in range(len(list_1))}
# print(dict)
# dict_n = { k:v for k, v in dict.items() if v >= 500}
# print(dict_n)
#
# #集合推导式
# list = [2, 2, 3]
# set = {l **3 for l in list}
# print(set) #集合自动去重
#
# #常用推导式
# # [xx for xx in range()] 列表推导式
# # {xx1 : xx2 for ... in ...} 字典推导式
# # {xx for xx in ...}
#
# # for循环用于针对序列中的每个元素的一个代码块
# # while 在条件满足时一直循环
# i = 1
# sum = 0
# while i <= 10:
#     print(i)
#     if i % 2 == 0:
#         sum += i
#         print(f'total is {sum}')
#     i += 1
#
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print(f'1 到 {n} 之和为：{sum}')
#
# count = 0
# while count < 5:
#     print(f'{count} 小于 5')
#     count += 1
# else:
#     print(f'{count} 大于等于 5')
#
# i = 1
# while i <= 5:
#     if i == 4:
#         print('我吃饱了。')
#         break
#     print(f'吃了第{i}个苹果。')
#     i += 1
#
# i = 1
# while i <= 5:
#     if i == 3:
#         print(f'第{i}个有虫子，不吃了。')
#         i += 1
#         continue
#     print(f'吃了第{i}个苹果。')
#     i += 1
#
# j = 1
# while j <= 5:
#     i = 1
#     while i <= j:
#         print('*', end="")
#         i += 1
#     # print(end='\n')
#     print()
#     j += 1
#
# j = 1
# while j <= 9:
#     i = 1
#     while i <= j:
#         # s = j * i
#         print(f'{i} * {j} = {i*j}', end="\t") #end表示每一个打印用tabel来间隔
#         i += 1
#     print()
#     j += 1
#
# #08 函数
# def sum(a,b):
#     """加法函数"""
#     c = a + b
#     print(c)
# sum(1, 2)
# help(sum)
#
# def info(name, age, gender, company="Yirui"): #可以定义默认参数
#     print(f'你的姓名是{name}, 性别是{gender}, 年龄是{age}, 公司是{company}.')
# info('徐海军', 40, '男')
# info('xuhaijun', age=40, gender="男") #位置参数必须是再前面，否则会报错
#
# #可变参数,收集参数
# #接受所有位置参数
# def test(*args):
#     print(args) #返回一个元组
# test('xxx',20)
# #接受所有关键字可变参数
# def test(**kwargs):
#     print(kwargs)
# test(name='xuhaijun', age=40, gender='male') #返回一个字典
#
# #函数内的局部变量
# def test():
#     a = 520 #内部变量，外部无法调用
#     print(a)
# test()
#
# a = 520
# def test():
#     global a #声明a为全局变量
#     a = 1314 #先声明了才能重新赋值
#     print(a)
# test()
#
# a = 1314
# def test_1():
#     global a  #先声明a是全局变量
#     a = 520 #修改a的值
# def test_2():
#     print(a)
# test_1()
# test_2()
#
# #return 函数返回值，多个返回值可以写成return a, b   返回是一个元组(a, b)
# #return 后面可以连接列表，元组，字典
# #遇到retrun退出当前函数!!!
# def test(a, b):
#     # return (a, b)
#     return a + b
# print(test(520, 1314))
#
# #多函数返回值做参数传递
# def name1():
#     return 520
# def name2(a):
#     print(a)
# b = name1()
# name2(b)
#
# #元组拆包
# def name():
#     return 520, 1314
# a, b = name() #分别赋值
# print(a)
# print(b)
#
# c = {'姓名':'孙兴华', '年龄':20}
# def name():
#     return c
# a, b = name()
# print(a)
# print(b)
# print(c[a])
# print(c[b])
#
# #递归, 必须要留有出口
# # 计算 100+99+98+97+...+1
# def test(a):
#     if a == 1: #如果是1, 直接返回1 -- 设置的出口
#         return 1
#     result = a + test(a-1) #如果不是1, 重复执行累加
#     return result #返回累加的结果
# v = test(4)
# print(v)
#
# #lambda 当函数有一个返回值，且只有一句代码
# test = lambda :520
# print(test())
#
# print((lambda a,b: a+b)(520, 1314)) # a,b 是形参； a+b是表达式；(520,1314)是实参
# print((lambda a, b, c=5: a+b+c)(2,6)) # c=5是默认参数
# print((lambda *args: args)(1,2,3)) #*args是可变位置参数, 返回一个元组
# print((lambda **kwargs: kwargs)(name='xuhaijun',age=40)) #**kwargs 可变关键字参数，返回的是一个字典
# print((lambda a,b: a if a > b else b)(3,2))
#
# #列表中的字典数据排列
# list = [{'name':'opq','age':20},{'name':'def','age':32},{'name':'xyz','age':45}]
# list.sort(key=lambda x: x['name'], reverse=True)
# print(list)
#
# #09 高阶函数
# import functools
#
# print((lambda a,b: abs(a)+abs(b))(-5, 3))
# print((lambda a,b,c=abs: c(a)+c(b))(-5, 3))
#
# #filter(函数名，可迭代对象), 这个函数可以直接用lambda来替代
# #筛选
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def test(x):
#     return x % 2 == 0
# result = filter(test, l)
# print(result) #打印的是对象地址
# print(list(result)) #用list函数转换为列表
# print(list(filter(lambda x: x % 2, l)))
# print(list(filter(lambda x: x % 2 == 0, l))) #加上==0的条件才会输出和上面函数一样的结果
# print(list(filter(lambda x: x % 2, range(1,11)))) #用range(1,11)替代列表
#
# # map(函数名，迭代对象)
# # 将可迭代对象的每一个元素传递给函数进行运算操作
# list_1 = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x: x**2, list_1)))
#
# # reduce(函数名(x,y), 可迭代的对象)
# # 函数中必须有2个参数，每次函数计算的结果继续和序列的下一个元素做累积运算
# list_2 = [1, 2, 3, 4, 5]
# print(functools.reduce(lambda x,y:x+y, list_2))
# print(functools.reduce(lambda x,y:x+y, range(1, 10)))

#10课 文件和文件夹

# a = open("1.txt", "w+")
# a.write("""test line 1
# test line 2
# test line 3
# """)
# a = open('1.txt', 'r+')
# a.seek(2,0) #偏移指针，2，偏移量，0，从开头计算
# print(a.read(2))
# print(a.read(4))
# print(a.readlines())
# line1 = a.readline()
# line2 = a.readline()
# line3 = a.readline()
# print(line3)
# a.close()

# 文件备份
# import os
#
# filename = input('please input backup file: ')
# position = filename.rfind('.')
# if position > 0:
#     suffix = filename[position:]
# else:
#     print('wrong file name!')
# new_filename = filename[:position]+'backup'+suffix
#
# # old = open(filename, 'rb')
# # new = open(new_filename, 'wb')
#
# # while True:
# #     readdata = old.read(1024)
# #     if len(readdata) == 0: #读完了
# #         break
# #     new.write(readdata)
# os.rename(filename, new_filename)

# file_1 = open('main.py', 'r')
# for lines in file_1.readlines():
#     print(lines)
# import os
# os.mkdir('abc') #创建文件夹
# os.remove('1.txt') #删除文件
# os.rmdir('ccc') #删除文件夹
# os.rename('bbb', 'ccc') #重命名文件夹
# print(os.listdir())
# print(os.listdir('venv'))

# 批量修改文件名字
# import os
# input_0 = input(r'please input the path of directory(i.e. c:\abc): ') #加r的目的是为了让\不是转义字符
# input_1 = input('please input the file name for adding or deleting: ')
# input_2 = int(input('adding for 1, deleting for 2: ')) #int把输入转换为整型
#
# dir_list = os.listdir(input_0)
#
# for file in dir_list:
#
#     if input_2 == 1:
#         new_name = input_1 + file
#         print(new_name)
#     elif input_2 == 2:
#         prefix_length = len(input_1)
#         new_name = file[prefix_length:]
#         print(new_name)
#     else:
#         print('input error!')
#         break
#     os.chdir(input_0)
#     os.rename(file, new_name)
#

# 闭包
# def fun1(a, b, c=200):
#     c = 300
#
#     def fun2(): # 外部函数中定义了内部函数
#         s = a + b + c #内部函数使用了外部函数的变量值
#         print(f'result is: {s}')
#     return fun2 #不能加()，加了就是表示调用函数了; 外部函数中有返回值，返回值就是内部函数名
#
# var = fun1(6, 9) #变量名就是fun2, 因为fun1的返回值是fun2
# var() #执行fun2, 得到计算结果
#
# 装饰器
# def fun1(x):
#
#     def fun2():
#         print('Start')
#         x() #通过形参传递过来，然后执行这个形参函数
#         print('End')
#     return fun2
#
# @fun1 #语法糖，就不用手动将fun3传递给fun1的形参再将返回值重新赋值，替代的就是var = fun1(fun3)

# def fun3():
#     print('Python')
#
# # var = fun1(fun3) #fun3本身作为一个函数名字，又作为fun1的形参, var变量名也可以直接用fun3来替代
# # var()
#
# fun3() #如果使用@fun1，就可以直接调用fun3()函数，这里就不能用var()了

# 如果fun3有参数，哪怎么办？
# def fun1(x):
#
#     def fun2(name): #将fun3的参数传递给x,x其实就是fun3
#         print('Start')
#         x(name) #通过形参传递过来，然后执行这个形参函数
#         print('End')
#     return fun2
#
# @fun1 #语法糖，就不用手动将fun3传递给fun1的形参再将返回值重新赋值，替代的就是var = fun1(fun3)
# def fun3(name):
#     print(f'Python for {name}')
#
# fun3('LoCo')
#
# 多个被装饰函数和多参数怎么办？
# def fun1(x):
#
#     def fun2(*args):
#         print('开始')
#         x(*args)
#         print('结束')
#
#     return fun2
#
# @fun1
#
# def fun3(name, time):
#     print(f'{name}')
#     print(f'{time}')
#
# fun3('LoCo', '2022')
#
# @fun1
#
# def fun4(company):
#     print(f'{company}')
#
# fun4('YiRui')
#
# 关键字参数怎么办？最终的装饰器
# def fun1(x):
#     def fun2(*args, **kwargs):
#         print('开始')
#         x(*args, **kwargs)
#         print('结束')
#     return fun2
#
# @fun1
# def fun3(name, time):
#     print(f'{name}')
#     print(f'{time}')
#
# @fun1
# def fun4(company):
#     print(f'{company}')
#
# @fun1
# def fun5(name, time, **kwargs):
#     print(f'{name}')
#     print(f'{time}')
#     print(kwargs)
#
# fun3('LoCo', 2022)
# fun4('YiRui')
# fun5('LoCo', 2022, a=1, b=2, c='Simulation')

# 面向对象
# class Info():
#     def __init__(self, name, age): #self = 对象名 是个可变的对象
#         # 添加实例属性
#         self.name = name #和对象关系在一起的变量叫实例变量
#         self.age = age #语法：self.变量名
#
#     def fun1(self): #实例方法
#         print(f'name is {self.name}')
#         print(f'age is {self.age}')
#
# person_1 = Info('XHJ', 41) #创建对象1
# person_1.fun1() #调用实例方法

# class Test():
#     def __init__(self, name, age):
#         #添加实例属性
#         self.name = name
#         self.age = age
#
#     def action(self):
#         print(f'My name is {self.name}, {self.age} years old.')
#
# item_1 = Test('abc', 20)
# item_1.action()
# item_2 = Test('xyz', 30)
# item_2.action()

# class Mooncake():
#     def __init__(self):
#         # time
#         self.time = 0
#         # status
#         self.status = '生的'
#         # 调料列表
#         self.调料 = []
#
#     def action(self, time):
#         # 1. 计算总共的时间
#         self.time += time
#         # 2. 用统计的时间来判断
#         if 0 <= self.time < 3:
#             self.status = '生的'
#         elif 3 <= self.time < 5:
#             self.status = '半生不熟'
#         elif 5 <= self.time < 8:
#             self.status = '熟了'
#         else:
#             self.status = '糊了'
#
#     def add(self, 调料):
#         self.调料.extend(调料)
#
#     # 书写str魔法方法，用于输出对象状态
#     def __str__(self):
#         return f'时间是{self.time}, 状态是{self.status}, 调料有{self.调料}'
#
# item_1 = Mooncake()
# item_1.action(2)
# item_1.add(['豆沙','蔓越莓'])
# print(item_1)
#
# item_1.action(4)
# item_1.add(['鸡蛋清'])
# print(item_1)

# 面向对象，单继承
# class Dad(object):
#     def __init__(self):
#         self.age = 30
#     def info(self):
#         print(f'Dad is {self.age} years old.')
#
# class Son(Dad):
#     pass
#
# x = Son()
# x.info()

# 面向对象，多继承
# class Master_1(object):
#     def __init__(self):
#         self.name = 'yongchun'
#     def action(self):
#         print(f'{self.name}')
# class Master_2(Master_1):
#     def __init__(self):
#         self.name = 'jiequandao'
#     def action(self):
#         print(f'{self.name}')
# class Student(Master_2): #如果是两个平级的基类，默认继承第一个的属性和方法
#     pass
#
# item = Student()
# item.action()
# print(Student.__mro__) #手动查找继承的顺序
#
# class Master_1(object):
#     def __init__(self):
#         self.name = 'yongchun'
#     def action(self):
#         print(f'{self.name}')
# class Master_2(object):
#     def __init__(self):
#         self.name = 'jiequandao'
#     def action(self):
#         print(f'{self.name}')
# class Student(Master_2, Master_1):
#     def __init__(self):
#         self.name = 'jianshen'
#     def action(self):
#         self.__init__() #防止被先调用的父类属性覆盖，需要先用自己子类进行初始化
#         print(f'{self.name}')
#     def Master1_action(self): #调用父类的属性和方法
#         Master_1.__init__(self)
#         Master_1.action(self)
#     def Master2_action(self):
#         Master_2.__init__(self)
#         Master_2.action(self)
#
# item = Student()
# item.action() #子类和父类具有同名属性和方法，默认使用子类自己的
# item.Master1_action()
# item.Master2_action()

# # 面向对象，组合
# class Master_1(object):
#     def __init__(self, x):
#         self.name = x
# class Master_2(object):
#     def __init__(self, x):
#         self.name = x
# class Hongkong(object):
#     def __init__(self, x, y): #直接把类放进去实例化
#         self.m1 = Master_1(x) #这里m1, m2的名字可以和上面类名相同，也可以自己定义
#         self.m2 = Master_2(y)
#     def print_name(self):
#         print(f'{self.m1.name}, {self.m2.name}')
#
# i = Hongkong(1, 100)
# i.print_name()

# super 方法
# 一次调用多个父类同名属性和方法
# class Master_1(object):
#     def __init__(self):
#         self.name = 'yongchun'
#     def action(self):
#         print(f'usr {self.name}')
#
# class Master_2(Master_1):
#     def __init__(self):
#         self.name = 'jiequandao'
#     def action(self):
#         print(f'use {self.name}')
#
# class Student(Master_2):
#     def __init__(self):
#         self.name = 'jianshen'
#     def action(self):
#         self.__init__() #因为父类属性会覆盖子类，所以先调用自己子类的初始化
#         print(f'use {self.name}')
#     def master1_action(self): #调用父类的属性和方法
#         Master_1.__init__(self)
#         Master_1.action(self)
#     def master2_action(self):
#         Master_2.__init__(self)
#         Master_2.action(self)
#     def master1_master2_action(self): #一次调用所有父类的同名属性和方法
#         Master_1.__init__(self)
#         Master_1.action(self)
#         Master_2.__init__(self)
#         Master_2.action(self)
#
# i = Student()
# # i.action()
# # i.master1_action()
# # i.master2_action()
# i.master1_master2_action()

# #super的用法
# class Master_1(object):
#     def __init__(self):
#         self.name = 'yongchun'
#     def action(self):
#         print(f'usr {self.name}')
#
# class Master_2(Master_1):
#     def __init__(self):
#         self.name = 'jiequandao'
#     def action(self):
#         print(f'use {self.name}')
#
#         super().__init__()
#         super().action()
#
# class Student(Master_2):
#     def __init__(self):
#         self.name = 'jianshen'
#     def action(self):
#         self.__init__() #因为父类属性会覆盖子类，所以先调用自己子类的初始化
#         print(f'use {self.name}')
#     def master1_action(self):
#         Master_1.__init__(self)
#         Master_1.action(self)
#     def master2_action(self):
#         Master_2.__init__(self)
#         Master_2.action(self)
#     #用super().函数()一次调用父类同名属性和方法
#     def master1_master2_action(self):
#         super().__init__()
#         super().action()
# i = Student()
# i.master1_master2_action()

# # 14 面向对象 多态
# class 复仇者联盟(object):
#     def 实例方法(self): #定义父类，并提供公共方法
#         print('打灭霸')
#
# class 钢铁侠(复仇者联盟):
#     def 实例方法(self): #子类，重写父类同名的方法
#         print('空中作战')
#
# class 美国队长(复仇者联盟):
#     def 实例方法(self): #子类，重写父类同名的方法
#         print('地面作战')
#
# class 神盾局(object):
#     def 指挥_实例方法(self, 复仇者联盟):
#         复仇者联盟.实例方法()
#
# 帮派1 = 钢铁侠()
# 帮派2 = 美国队长()
#
# 对象 = 神盾局()
# 对象.指挥_实例方法(帮派1)
# 对象.指挥_实例方法(帮派2)
#
# class Info():
#     name = '' #类属性，被该类的所有实例对象所共有
#     age = 0   #和类关联在一起的变量叫类变量
#
#     def __init__(self, name, age):
#         #添加实例属性
#         self.name = name #和对象关系在一起的叫实例变量
#         self.age = age
#
#     def action(self):
#         print(f'Your name is {self.name}.')
#         print(f'You are {self.age} years old.')
#
# person_1 = Info('xuhaijun', 40) #创建对象
# person_1.action()
# person_2 = Info('abc', 20)
# person_2.action()
#
# class 圣斗士():
#     守护神 = '雅典娜'
#
# 黄金圣斗士 = 圣斗士() #创建的对象能够调用到类属性
# 青铜圣斗士 = 圣斗士()
# # 通过类来访问
# print(圣斗士.守护神) #类.类属性
# # 通过对象来访问
# print(黄金圣斗士.守护神) #对象.类属性
# print(青铜圣斗士.守护神) #对象.类属性
#
# # 类属性只能通过类对象修改, 不能通过实例对象来修改
# 圣斗士.守护神 = '哈迪斯'
# print(圣斗士.守护神)
# print(黄金圣斗士.守护神)
#
# # 面向对象 类方法
# class 圣斗士():
#     __武器 = '天秤座黄金圣衣'
#
#     @classmethod
#     def get_武器(cls):
#         return cls.__武器
#
# 黄金圣斗士 = 圣斗士()
#
# print(黄金圣斗士.get_武器())
#
# class 圣斗士(object):
#     @staticmethod
#     def 静态方法():
#         print('同样的招式对圣斗士只能使用一次。')
#
# 对象 = 圣斗士()
# 对象.静态方法()
# 圣斗士.静态方法()
#
# class 圣斗士(object):
#     #静态属性
#     @property
#     def 函数名(self):
#         print('同样的招式对圣斗士只能使用一次。')
#
# 对象 = 圣斗士()
# 对象.函数名

# print(1/0)

# a = int(input('请输入被除数：'))
# b = int(input('请输入除数:'))
# # try:
# #     print(a/b)
# # except:
# #     print('出错了！')
# try:
#     print(a/b)
# except Exception as 出错信息: #任何出错信息定义给变量：出错信息
#     print(f'出错了，出错信息：{出错信息}')
# else:
#     print('我是else, 看到我证明这个程序没有异常。')

# try:
#     var_name = open('location.txt', 'r')
# except Exception:
#     var_name = open('location.txt', 'w')
# else:
#     print('没有异常，我很开心。')
# finally:
#     var_name.close()

# try:
#     var_name = open('location.txt', 'w')
#     for file in var_name:
#         print(file)
# except Exception as error_msg:
#     print(f'{error_msg}')
# finally:
#     var_name.close()

# try:
#     with open('location.txt', 'w') as var_name:
#         for file in var_name:
#             print(file)
# except OSError as error_msg:
#     print(f'{error_msg}')

# import time
# try:
#     open_file = open('xxx.py')
#
#     try:
#         while True:
#             content = open_file.readlines()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     except:
#         print('Stops for some error.')
#     finally:
#         open_file.close()
#         print('close file.')
# except:
#     print('no file exists')

# class password(Exception):
#     def __init__(self, length, min_length):
#         self.length = length
#         self.min_length = min_length
#
#     def __str__(self):
#         return f'The length of your password is {self.length}, should be more than {self.min_length}!'
#
# def warning():
#     try:
#         user_input = input('please input passowrd: ')
#         if len(user_input) < 8:
#             raise password(len(user_input), 8)
#     except Exception as err_msg:
#         print(err_msg)
#     else:
#         print('password has been inputed successfully.')
#
# warning()

# import json

# list = [5, 2, 7, 3, 0]
#
# filename = 'xhj.json'
# with open(filename, 'w') as varname:
#     json.dump(list, varname)
#
# filename = 'xhj.json'
# with open(filename) as varname:
#     varname_1 = json.load(varname)
#
# print(varname_1)

# import json
# username = input('please input your name:')
# filename = 'username.json'
# with open(filename, 'w') as fileobject:
#     json.dump(username, fileobject)
#     print(f'{username}')
#
# import json
# filename = 'username.json'
# with open(filename) as fileobject:
#     username = json.load(fileobject)
#     print(f'{username}')

# import json
# def welcome():
#     filename = 'username.json'
#     try:
#         with open(filename) as fileobject:
#             username = json.load(fileobject)
#     except Exception:
#         username = input('Please input your username: ')
#         with open(filename, 'w') as fileobject:
#             json.dump(username, fileobject)
#             print(f'{username} we will remember you!')
#     else:
#         print(f'{username} welcome back!')
#
# welcome()

# def function(a, b):
#     print(a + ' and ' + b + ' are good friends.')
#
# if __name__ == '__main__':
#     function('Tom', 'Jerry')

# import  tutorial
# tutorial.function('Tom', 'Jerry')

# import random
# print(random.randint(1, 10))