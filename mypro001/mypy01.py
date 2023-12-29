# 我的第一个python程序
print("hello world!")
print("你好，世界！")

"""
多行注释
"""

a = "asdfghjkl\
zxcvbnm"
print(a)

b = 3
print(b)
print(id(b))
print(type(b))

x, y, z = 10, 20, 30
print(x, y, z)

#逻辑运算符
print((x < y) and (y < z))
print((x > y) or (y > z))
print(not (y < z))

p, q = 1, 2
p, q = q, p   #变量值互换
print(p, q)

#round(value)   四舍五入产生新值

#位运算符
e = 0b11001
f = 0b01000

print(bin(e | f))     #bin()可以将数字转成二进制表示0b11001
print(bin(e & f))     #与
print(bin(e ^ f))     #异或

print(3 << 2)     #左移一位相当于乘以2.左移两位相当于:3*4
print(20 >> 1)    #右移一位相当于除以2
