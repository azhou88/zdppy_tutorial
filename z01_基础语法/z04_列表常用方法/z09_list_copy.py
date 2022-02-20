# coding:utf-8

arr = list(range(10))
print(arr)
arr1 = arr.copy()  # 复制
print(arr1)

arr1[0] = 111  # 不存在引用元素，所以不改变原来的元素
print(arr)
print(arr1)
print("----------------------------------")

a = [111]
arr = [a, [2], [3]]
print(arr)
arr1 = arr.copy()  # 复制
print(arr1)

arr1[0] = [222]  # 存在变量，不改变原来的元素
print(arr)
print(arr1)
print("----------------------------------")
