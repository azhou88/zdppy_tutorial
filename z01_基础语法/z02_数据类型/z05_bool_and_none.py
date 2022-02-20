# coding:utf-8

# 空类型
test = None
print(f"test={test} bool(test)={bool(test)} type(test)={type(test)}")

a = 0  # 非0即真
c = 0.0
print(f"a={a} c={c} bool(a)={bool(a)} bool(c)={bool(c)}")

b = 1
d = 0.1
print(f"b={b} d={d} bool(b)={bool(b)} bool(d)={bool(d)}")

e = ''  # 非空即真
f = 'None'
g = None
print(f"e={e} bool(e)={bool(e)} f={f} bool(f)={bool(f)} g={g} bool(g)={bool(g)}")

# 布尔类型
test1 = True
test2 = False
print(f"test1={test1} test2={test2}")
