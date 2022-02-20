# coding:utf-8
arr = list(range(5)) * 3
print(arr)
arr.sort()  # 升序
print(arr)
arr.sort(reverse=True)  # 降序
print(arr)
print("------------------------")

arr = list("abcde") * 3
print(arr)
arr.sort()  # 升序
print(arr)
arr.sort(reverse=True)  # 降序
print(arr)
print("------------------------")
