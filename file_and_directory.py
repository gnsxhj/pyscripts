import os
import time

import pandas as pd
import re
import glob
import fnmatch
import datetime as dt
import shutil

from tempfile import TemporaryFile
import zipfile
from pathlib import Path

# os.chdir(r'C:/Users/XUHAIJUN/PycharmProjects/pythonProject')
# os.chdir(r'C:\Users\XUHAIJUN\PycharmProjects\pythonProject')
#
# print(os.getcwd())
# print(os.listdir())
# data = pd.read_excel('xxx.xls')
#
# print(data)
#
# P1 = r'\1'
# P2 = '2'
# P3 = '3'
#
# path_1 = P1 + P2 + P3
# path_2 = os.path.join(P1, P2, P3)
# print('c:', path_1)
# print('c:', path_2)

# l = os.listdir()
# file = []
# dir = []
# for i in l:
#     if os.path.isdir(i):
#         dir.append(i)
#     else:
#         file.append(i)
# print(dir)
# print(file)
# print(i, os.path.isdir(i))
# for i in l:
#     print(i, os.path.isfile(i))

# l = os.listdir('c:/')
# for i in l:
#     path = 'c:/' + i
#     print(path)
#     print(i, os.path.isdir(path))

# file = []
# dir = []
#
# # for i in os.scandir("c:/Users/XUHAIJUN/SynologyDrive/事业部运营/2021年"):
# for i in os.scandir("c:/Projects/软件工具/LoCo/Tools_Referenz/SVW_Clusterskripte/PV15.22"):
# #     # print(file.name, file.path, file.is_dir())
# #     print(file.name, file.stat())
#     if i.is_dir():
#         dir.append(i.name)
#     else:
#         file.append(i.name)
#
# temp_list = []
# for file_name in file:
#     if ('经营数据' in file_name):
#         temp_list.append(file_name)
#
# print(len(temp_list), temp_list)

# temp_list = []
# for file_name in file:
#     pos = file_name.rfind('.')
#     if file_name[pos:] == '.pdf' or file_name[pos:] == '.pptx':
#         temp_list.append(file_name)
# print(len(temp_list), temp_list)

# temp_list = []
# for file_name in file:
#     re_ex = '.*runskript.*'
#     r = re.match(re_ex, file_name, re.I)
#     try:
#         temp_list.append((r.group()))
#     except:
#         pass
# print(f'runskript file {len(temp_list)}, are {temp_list}')


# # basename
# path = 'C:/Projects'
# print(os.path.basename(path)) # basename 返回路径最走的文件名
# path = 'C:/Projects/'
# print(os.path.basename(path)) # 如果路径以/结尾，返回空值

# skript_path = 'c:\Projects\软件工具\LoCo\Tools_Referenz\SVW_Clusterskripte'

# def get_filelist(dir, Filelist):
#     newDir = dir
#     if os.path.isfile(dir):
#         Filelist.append(dir)
#         ##如果只要返回文件名，用basename
#         #Filelist.append(os.path.basename(dir))
#     elif os.path.isdir(dir):
#         for s in os.listdir(dir):
#             newDir = os.path.join(dir,s)
#             get_filelist(newDir, Filelist)
#     return Filelist
# if __name__ == '__main__':
#     list = get_filelist(skript_path, [])
#     print(len(list))
#     for e in list:
#         print(e)

# j = 0
# for dir_path, dir_list_01, file_list in os.walk(skript_path):
#     # print(dir_path)
#     # print(dir_list_01)
#     # print(file_list)
#     for i in file_list:
#         # print(dir_path+'\\'+i)
#         print(os.path.join(dir_path, i))
#         j += 1
# print(f'total are {j} files.')

# skript_path = 'c:\Projects\软件工具\LoCo\Tools_Referenz\SVW_Clusterskripte\PV15.22'
# for i in os.scandir(skript_path):
#     if i.name.startswith('runskript') and i.name.endswith('psh'):
#         print(i.name)

# os.chdir("c:/Users/XUHAIJUN/SynologyDrive/事业部运营/2021年")
# # print(glob.glob('*.pdf'))
# # print(glob.glob('2021.*'))
# l = glob.glob('*.pdf')
# print(l)
# for file in l:
#     print(file)

# skript_path = 'c:\Projects\软件工具\LoCo\Tools_Referenz\SVW_Clusterskripte'
# os.chdir(skript_path)
# skript_list = glob.glob('**/*.psh', recursive=True)
# for file in skript_list:
#     print(file)

# skript_path = 'c:\Projects\软件工具\LoCo\Tools_Referenz\SVW_Clusterskripte\PV15.22'
# file_list = os.listdir(skript_path)
# for file_name in file_list:
#     if fnmatch.fnmatch(file_name, '*pampbs*psh'):
#         print(file_name)

# dir_path = r'c:\Users\XUHAIJUN\SynologyDrive\Allgemein\公司介绍\2021年版'
# os.chdir(dir_path)
# pdf_list = glob.glob('**/*.pdf', recursive=True)
# for file in pdf_list:
#     file_size = os.stat(file).st_size/1024/1024
#     file_year = dt.datetime.fromtimestamp(os.stat(file).st_ctime).year
#     if (file_size > 2) and (file_year > 2021):
#         print(f'{file}, {file_size:<4.2f}MB, {file_year}')
    # time_group = time.localtime(os.stat(file).st_ctime)
    # file_date = time.strftime('%Y-%m-%d', time_group)
    # if (file_size > 2) and (file_date > '2021-12-31'):
    #     # print(f'{file}, {file_size:<4.2f}MB, {file_date}')
    #     print(f'{file}, {int(file_size)}MB, {file_date}')

# dir_path = r'c:\Users\XUHAIJUN\PycharmProjects\pythonProject'
# os.chdir(dir_path)
# if not os.path.exists('./temp'):
#     os.mkdir('./temp')
# else:
#     print('exists already!')

# cur_path = os.getcwd()
# new_dir = cur_path + r'\temp'
#
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)
#     print('created successfully!')
# else:
#     print('exists already, will be removed!')
#     os.rmdir(new_dir)

# def make_new_dir(path):
#     # basename: 返回目录路径中的最后一个元素
#     dir_name = os.path.basename(path)
#     # 判断路径是否存在
#     exists = os.path.exists(path)
#     if not exists:
#         # 如果不存在，则创建单层目录
#         os.mkdir(path)
#         print('Directory has benn created: '+ dir_name)
#         return True
#     else:
#         # 如果目录存在则不创建，并提示目录已存在
#         print('Directory already exists: '+ dir_name)
#         return False
#
# if __name__ == '__main__':
#     # make_new_dir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp')
#     os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject')
#     make_new_dir('temp')

# def make_new_dir(path):
#     if not os.path.exists(path):
#         os.makedirs(path)
#         print('Directory has been created!')
#         return True
#     else:
#         print('Directory already exists!')
#         return False
# if __name__ == '__main__':
#     os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject')
#     make_new_dir('./temp/temq')

# os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject')
# src_file = 'xxx.xls'
# dst_dir = 'temp/yyy.xls'
# shutil.copy(src_file, dst_dir)
# shutil.copytree('temp', 'temq/temo')
# shutil.move('temp', 'temq') # 目标文件夹一定要先存在
# shutil.rmtree('temq')

# os.rename('xxx.xls', 'zzz.xls')
# os.rename('zzz.xls', 'temp/xxx.xls')
# os.rename('temp/xxx.xls', 'yyy.xls')

# os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp')
# dir_path = os.getcwd()
# if not os.path.exists('../backup'):
#     os.mkdir('../backup')
# for dir_path, ch_dir_path, file_list in os.walk(dir_path):
#     # print(dir_path, ch_dir_path, file_list)
#
#     # for file in file_list:
#     #     pos = file.rfind('.')
#     #     if file[pos:] == '.pdf':
#     #         file_date = dt.datetime.fromtimestamp(os.stat(file).st_mtime)
#     #         new_file = str(file_date.year)+'-'+str(file_date.month)+'-'+str(file_date.day)+'-'+file
#     #         # print(dir_path+'\\'+file, '../backup/'+new_file)
#     #         os.rename(dir_path+'\\'+file, '../backup/'+new_file)
#
#     # for file in os.scandir(dir_path):
#     #     if file.name.endswith(".pptx"):
#     #         file_date = dt.datetime.fromtimestamp(os.stat(file).st_mtime)
#     #         new_file = str(file_date.year)+'-'+str(file_date.month)+'-'+str(file_date.day)+'-'+file.name
#     #         print(f'{file.name} will be renamed {new_file}.')
#     #         os.rename(dir_path+'/'+file.name, '../backup/'+new_file)
#     #

# os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp')
# # with open('./location.txt', 'r+', encoding='utf-8') as file:
# #     data = file.readlines()
# #     print(data)
# #     data = 'test line 1 \ntest line 2 \n'
# #     file.write(data)
# #     file.write('test line 3\n')
# path = './location.txt'
# data = pd.read_csv(path)
# data.to_csv('./xxx.txt', index=False)

# file = TemporaryFile('w+')
# file.write('Python'*100)
# file.seek(0)
# # data = file.readlines()
# # data = file.read(12)
# # print(data)
# print(file)
# file.close()

# with TemporaryFile('w+') as file:
#     file.write('Python '*100)
#     file.seek(0)
#     data = file.readlines()
#     print(data)

# os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp')
# with zipfile.ZipFile('./excel.zip', 'r') as file: #如果是中文可能是乱码
    # for file_name in file.namelist():
    #     file_info = file.getinfo(file_name)
    #     file_name = file_name.encode('cp437').decode('gbk') #编码转换，显示中文
    #     print(file_name, file_info.file_size, file_info.compress_size)
    # file.extract('location.txt', path='./backup') #解压单个文件到指定文件夹中
    # file.extractall(path = './backup') #path是可以省略的

# os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp/backup')
# with zipfile.ZipFile('../excel.zip', 'r') as file:  # 如果是中文可能是乱码
#     for file_name in file.namelist():
#         extracted_file = Path(file.extract(file_name))
#         extracted_file.rename(file_name.encode('cp437').decode('gbk'))

# # 创建压缩文件
# def zipDir(dirPath, outFileName = None):
#     '''
#     :param dirPath: 目标文件或者文件夹
#     :param outFileName: 压缩文件名，默认和目标文件相同
#     :return: none
#     '''
#     # 校验路径是否正确
#     if not os.path.exists(dirPath):
#         raise Exception('文件路径不存在：', dirPath)
#
#     # zip文件名默认和被压缩的文件名相同，文件位置默认在待压缩文件的同级目录
#     if outFileName == None:
#         outFileName = dirPath + '.zip'
#
#     if not outFileName.endswith('zip'):
#         raise Exception('压缩文件名的扩展名不正确！应以.zip作为扩展名！')
#
#     zip = zipfile.ZipFile(outFileName, 'w', zipfile.ZIP_DEFLATED)
#     # 遍历文件或者文件夹
#     for path, dirnames, filenames in os.walk(dirPath):
#         fpath = path.replace(dirPath, '')
#         for filename in filenames:
#             zip.write(os.path.join(path, filename), os.path.join(fpath,filename))
#     zip.close()
#
# if __name__ == '__main__':
#     zipDir(r'C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp/backup')

# # 判断重复文件并删除
# os.chdir('C:/Users/XUHAIJUN/PycharmProjects/pythonProject/temp')
# f_list = []
# for dir_path, sub_dir_list, file_list in os.walk('./'):
#     for file_name in os.scandir(dir_path): # 文件夹中遍历所有文件用os.scandir
#         if file_name.is_file(): # 判断是否是文件
#             file = open(file_name, 'rb').read() # 提取hash码
#             if hash(file) in f_list: # 判断hash码是否已经存在列表中
#                 os.remove(file_name) # 如果已经存在则删除文件
#             else:
#                 f_list.append(hash(file)) # 默认把所有遍历的文件hash码保存到列表中
