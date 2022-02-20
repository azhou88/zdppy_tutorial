# coding:utf-8

students = [
    {'name': 'dewei', 'age': 33, 'sex': '男', 'id': 1, 'top': '174'},
    {'name': '张大鹏', 'age': 10, 'sex': '男', 'id': 2, 'top': '175'}
]

xiaoyun = {
    'name': 'xiaoyun',
    'age': 18,
    'sex': '女',
    'id': 3,
    'top': '160'
}

# 插入元素
students.insert(0, xiaoyun)
print(students)

xiaogao = {
    'name': 'xiaogao',
    'age': 18,
    'sex': '男',
    'id': 4,
    'top': '188'
}

# 插入空的元素
students.insert(3, None)
students.insert(4, None)
students.insert(5, None)

# 插入
students.insert(6, xiaogao)
print(students)

# 插入到中间
xiaoming = {
    'name': 'xiaoming',
    'age': 19,
    'sex': '男',
    'id': 5,
    'top': '178'
}

students.insert(3, xiaoming)
print(students)
