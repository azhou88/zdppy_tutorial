# coding:utf-8

# 作用：转换为全小写
info = "hello world"
print(info.lower(), info.casefold())
print("----------------------")

info = "HELLO WORLD"
print(info.lower(), info.casefold())
print("----------------------")

info = "Hello woRLD"
print(info.lower(), info.casefold())
print("----------------------")

info = "你好 Hello  世界 woRLD"
print(info.lower(), info.casefold())
print("----------------------")
