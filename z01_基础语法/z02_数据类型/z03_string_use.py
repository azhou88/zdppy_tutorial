# coding:utf-8

# 字符串定义
info = 'python是一个非常有魅力的语言'

# 字符串包含
result = '魅力' in info
print(result)

# 字符串不包含
result = '语言' not in info
print(result)

# 字符串字符
info2 = '12345468746378'
print(max(info2))  # 最大的成员
print(min(info2))  # 最小的成员

# 字符串拼接
info3 = '天气好 要多锻炼身体。'
info4 = '多锻炼身体 身体会变得更好'
new_str = info3 + info4 + '!'
print(new_str)

# 字符串长度
print(len(new_str))
length = len(new_str)
print(type(length))
