''''''
'''
    Python装饰器
    
    装饰器接受一个函数，添加一些功能并返回它。
    Python有一个有趣的功能，称为装饰器。可将功能添加到现有代码中。
    这也称为元编程。 -> 程序的一部分试图在编译时修改程序的另一部分。
'''

'''
    学习装饰器的先决条件:
    Python中的所有内容都是对象。我们定义的名称只是绑定到这些对象上面的标识符。
    函数也不例外，它们也是对象(带有属性)。可以将各种不同的名称绑定到同一功能对象。
    
    函数可以作为参数传递给另一个函数。
    这种以其他函数为参数的函数也称为高阶函数。
    下面是例子:
'''
# def inc(x):
#     return x + 1
#
# def dec(x):
#     return x - 1
#
# def operate(func , x):
#     result = func(x)
#     return result
#
# print(operate(inc, 3))
# print(operate(dec, 3))

'''
    此外，一个函数可以返回另一个函数
'''
# def is_called():
#     def is_returned():
#         print('Hello')
#     return is_returned
#
# new =  is_called()
# # 输出 Hello
# new() # 在这里，is_returned()是一个嵌套函数，每次调用is_called()函数时，该函数都会定义并返回。
# 最后，我们必须了解Python中的闭包！见闭包.py
'''
    回到装饰器
    
    函数和方法被称为可调用的，因为它们可以被调用。
    实际上，任何实现特殊方法__call__()的对象都称为可调用的。
    因此，从最基本的意义上讲，装饰器是可调用的，可返回的。
    
    基本上，装饰器接受一个函数，添加一些功能并返回它。
    例子:
'''
# def make_pretty(func):
#     def inner():
#         print('我被装饰了！')
#         func()
#     return inner
# def ordinary():
#     print('我是一个普通函数!')
# pretty =  make_pretty(ordinary)
# pretty()
#
# ordinary()
# o1 = ordinary
# make_pretty(ordinary)()
# make_pretty(o1)()

'''
    在上面显示的示例中，make_pretty()是一个装饰器。在分配步骤中，
    pretty =  make_pretty(ordinary)
    函数ordinary()被修饰，返回的函数被命名为pretty。
    我们可以看到ordinary函数被make_pretty函数添加了一些新的功能。
    这类似于包装礼物，装饰器充当包装器。被装饰的物品(里面的礼物)的性质不会变。
    但是现在，它看起来很漂亮(自从装饰后)。
    
    通常，我们装饰一个函数并将其重新分配为:
    ordinary = make_pretty(ordinary)
    这是一个常见的构造，因此，Python具有简化此语法的语法-> 语法糖
    我们可以将@符号与装饰器函数的名称一起使用，并将其放置在要装饰的函数的定义上方。
    例如:
'''

# def make_pretty(func):
#     def inner():
#         print('我被装饰了！')
#         func()
#     return inner
#
# @make_pretty  # 装饰器的语法糖
# def ordinary():
#     print('我是普通的函数')
#
# ''' 相当于 '''
# def ordinary():
#     print('我是普通的函数')
# ordinary = make_pretty(ordinary)
# ''' 这只是实现装饰器的语法糖'''

# ordinary()
'''
    用参数装饰函数
    
    上面的装饰器只适用于没有任何参数的函数。
    如果函数具有一个或多个参数怎么办?
    
    -> 我们可以使用嵌套函数来传参
    示例如下:
'''
# def smart_divide(func):
#     def inner(a,b):
#         print('我要做除法',a,'和',b)
#         if b ==0:
#             print('诶呀，不能除')
#             return
#         return func(a,b)
#     return inner
#
# @smart_divide
# def divide(a,b):
#     return a/b
#
# divide(2,0)
# print(divide(2, 3))

'''
    通过这种方式，我们可以装饰带有参数的函数。
    敏锐的观察者会注意到，inner()装饰器内部的嵌套函数的参数与其装饰的函数的参数相同。
    考虑到这一点，现在我们可以使通用装饰器可以使用任意数量的参数。
    
    在Python中，此魔术是通过function(*args,**kwargs)完成的。
    这样，args是位置参数的元组，kwargs是关键字参数的字典。
    这样的装饰器的一个实例如下:
'''
# def works_for_all(func):
#     def inner(*args,**kwargs):
#         print('我可以装饰任何函数')
#         return func(*args,**kwargs)
#     return inner

'''
    Python链接多个装饰器
    
    可以在Python中链接多个装饰器。
    这就是说，一个函数可以用不同(或相同)的装饰器多次装饰。
    我们只需将装饰器放置在所需的函数之上。
    
    示例如下:
'''
# def star(func):
#     def inner(*args,**kwargs):
#         print('*'*30)
#         func(*args,**kwargs)
#         print('*'*30)
#     return inner
# #
# def percent(func):
#     def inner(*args,**kwargs):
#         print('%'*30)
#         func(*args,**kwargs)
#         print('%'*30)
#     return inner
#
# @star # 再装饰star
# @percent # 先装饰percent
# def show(msg):
#     print(msg)
# #
# show('你好')

# def pretty(func):
#     print('func被装饰了!')
#     return func
#
# def pretty_double(func):
#     def inner():
#         print('我是装饰器')
#         func()
#     return inner
#
# @pretty
# @pretty_double
# def func():
#     print('我是func')
#
# func()