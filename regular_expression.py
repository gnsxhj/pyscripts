#re.match, re.search

import re
print(re.match('www','www.runoob.com'))
print(re.match('www','www.runoob.com').span())
print(re.match('com','www.runoob.com'))

line = "Cats are smarter than dogs."
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print(matchObj.group())
    print(matchObj.group(1))
    print(matchObj.group(2))
else:
    print("No match!!!")

print(re.search('www','www.runoob.com').span())
print(re.search('com','www.runoob.com').span())

line = "Cats are smarter than dogs."
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
    print(searchObj.group())
    print(searchObj.group(1))
    print(searchObj.group(2))
else:
    print("No match!!!")
#re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None
#re.search 匹配整个字符串，直到找到一个匹配。

line = "Cats are smarter than dogs."
matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print(matchObj.group())
else:
    print("No match!!!")

searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print(searchObj.group())
else:
    print("No match!!!")

# re.sub
phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'#.*$', " ", phone)
print("电话号码：",num)

num = re.sub(r'\D', "", phone) #删除非数字字符
print("电话号码：",num)

s = '2017-11-27'
print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1', s))

#re.compile

pattern = re.compile(r'\d+') #用于匹配至少一个数字
m = pattern.match('one12twothree34four') #查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10) #从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10) #从数字1开始匹配，匹配成功
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I) #re.I表示忽略大小写
m = pattern.match('Hello World Wide Web.')
print(m)
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.span())
print(m.span(2))
print(m.groups())

#findall
#match 和 search 是匹配一次 findall 匹配所有
result1 = re.findall(r'\d+', 'runoob 123 google 456')
pattern = re.compile(r'\d+') #查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('runoob123google 456', 0, 10)

print(result1)
print(result2)
print(result3)

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)

#re.finditer
it = re.finditer(r"\d+", "123a32bc45jf45")
for match in it:
    print(match.group())

#re.split
print(re.split(' ', 'hello world!'))

# re.I 对大小写不敏感
# re.M 多行匹配，影响^和$


