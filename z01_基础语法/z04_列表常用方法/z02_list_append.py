# coding:utf-8

books = []

# 列表添加
print(id(books))
books.append('python入门课程')
print(books)
print(id(books))

# 添加不同类型的元素
number = 1.1
books.append(number)
books.append('django')
books.append(1)

# 列表内存地址没有变化
print(books)
print(id(books))
