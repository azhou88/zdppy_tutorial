# coding:utf-8

# 将列表追加到当前列表
arr1 = list(range(5))
arr2 = list(range(5, 10))
print(arr1)
print(arr2)

arr1.extend(arr2)  # 拓展
print(arr1)
print(arr2)
