# coding:utf-8

a = set(list("abc"))

# 添加
a.add("d")
print(a)
print("--------------------------------")

# 更新
b = set(list("bcdef"))
a.update(b)
print(a)
print("--------------------------------")

# 删除
a.remove("b")
print(a)
print("--------------------------------")

# 清空
a.clear()
print(a)
print("--------------------------------")
