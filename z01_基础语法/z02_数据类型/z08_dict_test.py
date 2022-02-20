# coding:utf-8

# 创建字典
user_info = {'name': '张大鹏同学', 'age': 10, 'top': '180cm'}
result = 'name' in user_info
print(result)
result = 'hope' in user_info
print(result)
result = 'hope' not in user_info
print(result)
print("-------------------------")

# 字典元素个数
count = len(user_info)
print(count)
print("-------------------------")

# 字典转布尔
result_bool = bool(user_info)
print(result_bool)
empty_dict = {}
print(bool(empty_dict))
print("-------------------------")
