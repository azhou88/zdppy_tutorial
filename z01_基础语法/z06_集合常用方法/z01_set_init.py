# coding:utf-8

# 创建空集合
a = set()
print(a)
print(type(a))
print("--------------------------------")

# 将列表转换为集合
b = set(['python', 'django', 'flask'])
print(b)
print("--------------------------------")

# 集合可以存储任何类型
c = {(1, 2, 3), '123', 1}
print(c)
print("--------------------------------")

# 定义空集合
d = {}
print(d, type(d))
print("--------------------------------")

# 列表转集合
a_list = ['python', 'django', 'python', 'flask']
b_set = set(a_list)
print(b_set)
print("--------------------------------")
