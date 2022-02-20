# coding:utf-8

d = {
    f"k{i}": f"v{i}"
    for i in range(10)
}
print(d)

# 获取只
print(d.get("k1"))

# 获取不存在的只
print(d.get("k11"))

# 如果不存在设置默认值
print(d.get("k11", "v11"))
