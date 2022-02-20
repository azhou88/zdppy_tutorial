# coding:utf-8

name = '张大鹏'
name_02 = '张大鹏'

# 查看变量的内存地址
print(id(name))
print(id(name_02))

# 修改
new_name = name
print(id(new_name))
print(type(name))

# 创建字符串
info = '''今天的天气真好呀'''
print(info)

# 创建字符串
info1 = 'asdf'
info2 = "asdf"

# 创建字符串
new_str = "nihao 张大鹏 'nihao' '' 张大鹏"
str_01 = ''
print(len(str_01))
print(new_str)
