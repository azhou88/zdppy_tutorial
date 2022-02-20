# coding:utf-8

# 集合常用操作

a = set(list("abcdef"))
b = set(list("defjhik"))
print(a)
print(b)
print("--------------------------------")

# 求交集
c = a.intersection(b)
print(c)
print("--------------------------------")

# 求并集
c = a.union(b)
print(c)
print("--------------------------------")

# 求差集
c = a - b
print(c)
print("--------------------------------")
