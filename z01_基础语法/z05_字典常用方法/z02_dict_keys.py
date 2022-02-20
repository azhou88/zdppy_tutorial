# coding:utf-8

# 生成字典
d = {
    f"k{i}": f"v{i}"
    for i in range(10)
}
print(d)
print("-------------------------------")

# 所有的key
print(d.keys())
print(list(d.keys()))
print("-------------------------------")

# 所有的value
print(d.values())
print(list(d.values()))
print("-------------------------------")
