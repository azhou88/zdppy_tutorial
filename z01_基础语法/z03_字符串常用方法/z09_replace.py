# coding:utf-8

# 将字符串中的字符串替换为新的字符串
info = "abc aaa bbb ccc abc abc"

# 将全部a替换为 我
print(info.replace("a", "我"))

# 将前三个a替换为 我
print(info.replace("a", "我", 3))
