# coding:utf-8

d = {
    f"k{i}": f"v{i}"
    for i in range(10)
}

# 删除指定建
v1 = d.pop("k1")
print(v1)
print(d)
print("--------------------------")

# 删除指定建
del d["k2"]
print(d)
print("--------------------------")

# 随机删除
item = d.popitem()
print(item, type(item))
print(d)
print("--------------------------")

# 清空
d.clear()
print(d)
print("--------------------------")

# 删除字典
del d
