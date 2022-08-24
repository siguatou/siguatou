
# 如何验证循环体内定义的变量是局部变量？
# 验证结果: 循环体中定义的变量不是局部变量！
while True:
    a = 1
    a += 1
    a += 1
    break

# print(a)
for i in range(10):
    pass

def func(i):
    result = i * 8
    return result

print(func(i))