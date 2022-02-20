# coding:utf-8

arr = list('abc' * 3)
print(arr)

# 移除 a
print(arr.remove("a"))  # 只会移除第一个遇到的元素
print(arr)

# 移除 b
arr.remove("b")
arr.remove("b")
arr.remove("b")
print(arr)
