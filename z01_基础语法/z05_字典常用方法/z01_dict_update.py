# coding:utf-8

# 创建字典
d = {}

# 添加元素
d["a"] = 11
print(d)

# 修改元素
d["a"] = 22
print(d)

# 通过字典更新
d1 = {"a": 11, "b": 22}
d2 = {"a": 111, "c": 333}
d1.update(d2)
print(d1)
print(d2)
print("-----------------------")

# 设置值，不存在则设置，存在则不修改
d1.setdefault("d", 444)
print(d1)
d1.setdefault("d", 444444)
print(d1)
print("-----------------------")
