# coding:utf-8
d = {
    f"k{i}": f"v{i}"
    for i in range(10)
}
print(d)

# 复制
d1 = d.copy()
print(d1)
print("-------------------")

# 更新
d1.update({"k1": 111, "k2": 222})
print(d)
print(d1)
print("-------------------")
