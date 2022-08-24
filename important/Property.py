''''''
'''
    Python有一个伟大的概念，称为属性。
    它使面向对象的程序员生活变得更加简单。
'''

'''
    一个实例的开始。
    
    假设您决定创建一个以摄氏度为单位存储温度的类。
    它还将实现一种将温度转化为华氏温度的方法。其中一种方法如下:

'''
# class Celsius:
#     def __init__(self,temperature = 0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

# 我们可以从此类中制造出对象并根据需要操纵属性temperature。在Python shell中尝试这些。

'''
    每当我们分配或检索任何对象属性(如temperature)时，Python都会在对象的__dict__字典中进行搜索。
    因此，man.temperature内部变为man.__dict__['temperature']。
    现在，让我们进一步假设我们的课程在客户中很受欢迎，并且他们开始在程序中使用它。
    他们对对象进行了各种分配。
    有一天，一个值得信赖的客户来找我们，建议温度不能低于-273摄氏度，也被称为绝对零度。
    他进一步要求我们实现这个值约束。
    作为一家追求客户满意度的公司，我们很高兴地听取了这个建议，并发布了1.01版本(对现有类的升级)。
'''

'''
    使用getter和setter
    解决上述约束的一个明显方法是隐藏属性temperature(将其设为私有)，并定义新的getter和setter接口以对其进行操作。
    如下所示:
'''
# class Celsius:
#     def __init__(self,temperature = 0):
#         self.set_temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#
#     # new update
#     def get_temperature(self):
#         return self._temperature
#
#     def set_temperature(self,value):
#         if value < -273:
#             raise ValueError('-273度是不可能的')
#         self._temperature = value
'''
    我们在上面可以看到get_temperature(),set_temperature()已经定义了新的方法，
    此外，用_temperature替换了temperature。
    下划线(_)开头表示Python中的私有变量。
    
    此更新成功实施了新限制。我们不再被允许将温度设置为低于-273。
    请注意，私有变量在Python中不存在。只需遵守一些规范即可。语言本身没有任何限制。
'''

'''
    上述更新的最大问题在于，所有在程序中实现了上一类的客户端都必须将其代码从obj.temperature修改为obj.get_temperature()，
    并将所有分配(例如obj.temperature=val，修改为obj.set_temperature(val))。
    这种重构会给客户带来数十万行代码的麻烦。
    总而言之，我们的新更新不向后兼容。这是@property发挥作用的地方。
'''

'''
    @property的力量
    python处理上述问题的方法是使用property。我们可以这样来实现它。
'''
# class Celsius:
#     def __init__(self,temperature = 0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     # new update
#     def get_temperature(self):
#         print('获得值:')
#         return self._temperature
#
#     def set_temperature(self,value):
#         if value < -273:
#             raise ValueError('-273度是不可能的')
#         print('设定值:')
#         self._temperature = value
#
#     temperature = property(get_temperature,set_temperature)
#
# c1 = Celsius(37)
# c1.temperature = 36
# print(c1.to_fahrenheit())
# print(c1.temperature)

'''
    代码的最后一行创建了property对象temperature。
    简而言之，属性将一些代码(get_temperature,和set_temperature)附加到成员属性访问(temperature)。
    
    任何检索温度值的代码都将自动调用get_temperature()而不是字典(__dict__)查找。
    同样，任何为温度分配值的代码都将会自动调用set_temperature()。这是Python中一项很酷的功能。
    
    我们可以在上面看到即使创建对象时也会调用set_temperature()。
'''
'''
    创建对象时，将调用__init__()方法。此方法的线为self.temperature = temperature。
    此分配自动调用set_temperature()。
    
    同样，任何访问如c.temperature都会自动调用get_temperature()。
    这就是属性的作用。
    
    通过属性，我们可以看到，我们修改了类并实现了值约束，而无需更改客户端代码。
    因为，我们的实现是向后兼容的。
    最后请注意，实际温度值存储在私有变量_temperature中。
    temperature属性是一个属性对象，它提供了与此私有变量的接口。
'''

'''
    深入了解property
    
    在Python中，property()是一个内置函数，用于创建并返回属性对象。
    property(fget= None,fset=None,fdel=None,doc=None)
    其中，fget为获取属性值的函数，fset为设置属性值的函数。fdel为删除属性值的函数，doc为字符串(如注释)。
    从实现中可以看出，这些函数参数是可选的。因此，可以简单地按照一下方式创建属性对象。
'''
property()
''' 属性对象有三个方法，getter()、setter()和deleter()，用于稍后指定fget、fset和fdel。这意味着'''
# temperature = property(get_temperature,set_temperature)
''' 可以分解为'''
# # 创建空属性
# temperature = property()
# # 设置 fget
# temperature = temperature.getter(get_temperature)
# # 设置 fset
# temperature = temperature.getter(set_temperature)
''' 两段代码是等效的'''

'''
    熟悉Python装饰器的程序员会认识到上述构造可以实现为装饰器
    
    我们可以更进一步，不定义名称get_temperature，set_temperature，因为它们是不必要的，并且会影响类命名空间。
    为此，我们在定义getter和setter函数时重用了名称temperature。这是可以的。
'''
class Celsius:
    def __init__(self,temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print('获得值:')
        return self._temperature

    # 对_temperature私有属性进行约束
    @temperature.setter
    def temperature(self,value):
        if value < -273:
            raise ValueError('-273度是不可能的')
        print('设定值:')
        self._temperature = value













