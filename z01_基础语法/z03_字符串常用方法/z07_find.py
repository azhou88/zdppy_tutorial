# coding:utf-8

info = 'abcd dcba'

# 查找子串在总串中第一次出现的索引
print(info.index("b"))
print(info.find("b"))

# 从右边开始找
print(info.rindex("b"))
print(info.rfind("b"))

# find找不到不会报错，index找不到会报错
print(info.find("xxx"))  # 找不到返回-1
print(info.index("xxx"))
