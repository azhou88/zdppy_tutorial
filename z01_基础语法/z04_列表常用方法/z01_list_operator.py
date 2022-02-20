# coding:utf-8

# 列表相加
a = [1, 2, 3]
b = [11, 22, 33]
print(a + b)
print(tuple(a) + tuple(b))  # 元组相加
print("--------------------------------------")

# 列表乘法
print(a * 3)
print(tuple(a) * 3)
print("--------------------------------------")

# 赋值运算
a += [111]
b *= 2
print(a)
print(b)
print("--------------------------------------")

# in 操作符
flag1 = 1 in a
flag2 = 1 not in a
print(flag1, flag2)
print("--------------------------------------")
