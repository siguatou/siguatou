''''''
'''
    闭包是函数里面嵌套函数，外层函数返回里层函数，这种情况称之为闭包
    # 闭包 内部函数调用外部函数的变量，外部函数返回内部函数的引用
'''
# def func():
#     def func1():
#         return 'hello'
#     return func1
#
# print(func())

# def func(x):
#     def func1():
#         return 'hello'+x
#     return func1
#
# print(func('world')())

'''
    什么是引用？
    在python中一切都是对象，包括整型数据1，函数，其实都是对象
    当我们进行a=1的时候，实际上在内存当中有一个地方存了一个值1，然后用a这个变量存了1所在内存位置的引用
    引用就好像c语言里的指针，大家可以把引用理解成地址
    a只不过是一个变量名字，a里面存的是1这个数值所在的内存地址，就是a里面存了数值1的引用。
    
    
    相同的道理，当我们在python中定义了一个函数def demo():的时候，
    内存当中会开辟一些空间，存下这个函数的代码、内部的局部变量等等。这个demo只不过是一个变量名字，
    它里面保存了这个函数所在位置的引用而已。我们还可以进行 x = demo, y = demo，
    这样的操作就相当于，把demo里面存的东西赋值给x和y，这样x和y都指向了demo函数所在的引用，
    在这之后我们可以使用x() 和y()来调用我们创建的demo()，
    调用的实际上根本就是一个函数，x、y和demo三个变量名存了同一个函数的引用。
'''

# def dome1():
#     a = 100
#     def dome2():
#         # b = a+a # b 200
#         # a 不能作为被赋值的变量
#         # a只能作为被调用的变量，而不能作为赋值变量
#         # 即，a变量不能被修改，只能被调用
#         # a += 1
#         # return a
#
#         # 如果要a作为被赋值的变量，需要对a进行nonlocal声明
#         nonlocal a
#         a += 1
#         return a  # 101
#     return dome2
#
# a = dome1()
# print(a())

# li = []
# for i in range(4):
#     def func():
#         return i
#     li.append(func)
#
# for f in li:
#     print(f()) # 3 3 3 3
#
# # ------------------------------
#
# li = []
# for i in range(4):
#     def func(i):
#         def func1():
#             return i
#         return func1
#     li.append(func(i))
#
# print(li)
# for f in li:
#     print(f()) # 0 1 2 3

'''
    什么是嵌套函数和非局部变量
    在另一个函数内部定义的函数称为嵌套函数。嵌套函数可以访问封闭范围的变量。
    在python中，默认情况下，这些非本地变量是只读的，并且我们必须将它们明确声明为非本地变量(nonlocal)才能进行修改。
    
'''
# def print_msg(msg):
# # 这是外部封闭函数
#     def printer():
# # 这是嵌套函数
#         print(msg)
#     return printer
#
# another = print_msg('Hello')
# another()
'''
    这很不寻常
    这种将一些数据('Hello')附加到代码上的技术在Python中称为闭包。
    即使变量超出范围或函数本身已从当前命名空间中删除，也会记住封闭范围中的这个值。(重要！！！)    
'''

'''
    闭包的条件:
        从以上的实例可以看出，在Python中，当嵌套函数在其封闭范围内引用一个值时，我们有一个闭包。
        
    以下几点总结了Python中创建闭包必须满足的条件:
        I 我们必须有一个嵌套函数(函数在函数的内部)
        II 嵌套函数必须引用在封闭函数中定义的值
        III 封闭函数必须返回嵌套函数
'''

'''
    何时使用闭包? -> 闭包有什么用呢?
    闭包可以避免使用全局值，并提供某种形式的数据隐藏。它还可以为该问题提供面向对象的解决方案。
    当在一个类中实现的方法很少(大多数情况下是一个方法)时，闭包可以提供另一种更优雅的解决方案。
    但是，当属性和方法的数量变大时，最好实现一个类。
    下面是一个例子:
'''
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
#
# 3的乘数
times3 = make_multiplier_of(3)

# 5的乘数
times5 = make_multiplier_of(5)
#
# # 输出 27
# print(times3(9))
#
# # 输出:15
# print(times5(3))
#
# # 输出:30
# print(times5(times3(2)))

'''
    Python中的装饰器也大量使用了闭包。
    最后，最好指出可以找到封闭在封闭函数中的值。
    
    所有的函数都有一个__closure__属性，如果它是一个闭包函数，则该属性返回单元格对象的元组。
    参考上面的示例，我们知道times3,times5是闭包函数。
    
    单元格对象具有存储关闭值的属性cell_contents。
'''
print(times3.__closure__)
print(times3.__closure__[0].cell_contents)

print(times5.__closure__)
print(times5.__closure__[0].cell_contents)