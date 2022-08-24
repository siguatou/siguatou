''''''
'''
    Python类中方法总结 —— 实例方法、静态方法和类方法
    
    在Python的类语法中，可以出现三种方法，具体如下:
    (1) 实例方法
        1）第一个参数必须是实例本身，一般使用[self]表示。
        2）在实例方法中，可以通过[self]来操作实例属性，[类名]来操作类属性。
        3）实例方法只能通过实例对象去调用，尽管也可以通过类名间接调用[类名.方法名(self,...)]，但此时仍然需要传入self对象。
        
    (2) 类方法
        1）使用[@classmethod]修饰函数，且第一个参数必须是类本身，一般使用[cls]表示。
        2）在类方法中，可以使用[cls = 类名]来操作类属性，但是不能操作实例属性(self对象中存储的变量)。
        3）类方法可以通过实例对象或者类对象调用。
        
    (3) 静态方法
        1）使用[@staticmethod]修饰函数，不需要使用任何参数表示。与普通函数一样，只是将该方法放到了类中实现而已。
        2）使用方式与类方法一样，参考类方法中的2)、3)。（注：静态方法只能通过[类名]去操作类属性）
        
'''
# 案例一
# class Foo(object):
#     ''' 类三种方法语法形式 '''
#     count = 0 # 统计实例对象的数量
#     class_method_count = 0 # 统计类方法的调用次数
#
#     # 实例方法
#     def __init__(self,name):
#         self.name = name
#         Foo.count += 1
#
#     # 实例方法
#     def instance_method(self):
#         print('是类{}的实例方法，只能被实例对象调用'.format(Foo))
#         print('产生了一个<{}>实例，共有<{}>个实例对象'.format(self.name,Foo.count))
#
#     # 类方法
#     @classmethod
#     def class_method(cls):
#         print('是类{}的类方法，可以被实例对象、类对象调用'.format(cls))
#         cls.__static_method_test()
#         cls.class_method_count += 1
#
#     # 静态方法
#     @staticmethod
#     def static_method():
#         print('是类{}的静态方法，可以被实例对象、类对象调用'.format(Foo))
#         print('+++以下内容为类方法class_method()的运行结果:')
#         Foo.class_method()
#
#     @staticmethod
#     def __static_method_test():
#         print('调用静态方法 static_method_test()')
#
# print('--'*20 + '实例方法测试' + '--'*20)
# obj1 = Foo('dog')
# obj1.instance_method()  # <=> Foo.instance_method(obj1)
#
# print('--'*20 + '类方法测试' + '--'*20)
# obj1.class_method()
# print('--'*20)
# Foo.class_method()
#
# print('--'*20 + '静态方法测试' + '--'*20)
# obj1.static_method()
# print('--'*20)
# Foo.static_method()
''' 从案例1可以得到，类方法与静态方法可以相互调用，但是静态方法只能用[类名]表示，而类方法用[cls]就比较方便了 '''

# 案例2:实例方法、类方法、静态方法在继承中(子类重写父类中的方法)的使用
# class Foo(object):
#     X = 1
#     Y = 14
#
#     @staticmethod
#     def average(*mixes):
#         print('父类中的静态方法 average(*mixes)')
#         print('*****',mixes)
#         return sum(mixes) / len(mixes)
#
#     @staticmethod
#     def static_method():
#         print('父类中的静态方法 static_method()')
#         return Foo.average(Foo.X,Foo.Y)  # 注: 因为这儿已经限定了只允许调用父类中的average()
#
#     @classmethod
#     def class_method(cls):  # 父类中的类方法
#         print('父类中的类方法 class_method(cls)')
#         return cls.average(cls.X,cls.Y)  # 注: 若子类对象调用该函数，此时的cls==Son，故调用子类重写后的average()
#
# class Son(Foo):
#     @staticmethod
#     def average(*mixes): # 子类重载了父类的静态方法
#         print('子类中重载了父类的静态方法 average(*mixes)')
#         print('*****',mixes)
#         return sum(mixes) / len(mixes)
#
# print(Son.average(1, 2, 3), "\n" + "---" * 20)
# print(Son.class_method(),   "\n" + "---" * 20)
# print(Son.static_method(),  "\n" + "---" * 20)

#--------------------------------------------------------------------------
'''
    Python中的类方法和静态方法
    
    实例方法
    首先，我们先简单回顾下Python中实例方法的定义
'''
# class Hello:
#     def say_hello(self,name):
#         print('hello',name)

'''
    如果要调用Hello类中定义的say_hello实例方法，需要先实例化一个实例对象Hello()，再进行调用。
'''
# h = Hello()
# h.say_hello('world') # hello world

'''
    类方法 -> 我们再来看看类方法如何使用
    定义如下:
'''
# class Hello:
#     @classmethod
#     def print_class_name(cls):
#         print(cls.__name__)

'''
    通过cls.__name__的方式，我们打印了Hello类的类名。
    类方法中cls等价于Hello，就像实例方法中self等价于实例对象Hello()一样。
    同self一样，cls也是约定俗成的变量名，我们也可以不写成cls而写成任何我们喜欢的变量名。
    
    类方法其实也可以通过实例对象调用,如下所示:
'''
# h = Hello()
# h.print_class_name()  # Hello

'''
    得到的结果是一样的，其实当我们用实例对象调用类方法的时候，Python解释器会自动帮我们获取到实例对象所属的类，
    然后将其作为参数传给类方法。
    
    现在我们了解了类方法的语法后，那么什么时候需要用到类方法呢？
    类方法最常用的两个场景一个是①类的继承，另一个是②构造方法。(重要！！)
'''
'''
    类的继承中使用类方法
    
    首先来看如何在类继承中使用cls来做子类的名称绑定。
'''
# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def shout(cls):
#         print(f"{cls.__name__} shout")
#
#
# class Cat(Animal):
#     pass
#
# class Dog(Animal):
#     pass
#
# cat = Cat('a')
# cat.shout()
#
# dog = Dog('b')
# dog.shout()
'''
    这里我们定义了一个动物类Animal，其中有一个shout方法用来打印哪种动物在叫。
    Cat和Dog类都继承自Animal类，当通过Cat类或Dog类的实例对象调用shout类方法时，就会分别打印出Cat Shout和Dog Shout。
    这样我们就实现了只需在父类中定义一个类方法，便可以在子类调用父类方法的时候根据类型的不同自动获取子类的类型名称。
    如果不使用类方法来定义，我们可能会写出如下代码:
'''
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def shout(self):
#         print('Animal shout')
#
# class Cat(Animal):
#     # def __init__(self,name):
#     #     super().__init__(name)
#     def shout(self):
#         print('Cat shout')
#
# class Dog(Animal):
#     # def __init__(self,name):
#     #     super().__init__(name)
#     def shout(self):
#         print('Dog shout')
#
# cat = Cat('cat')
# cat.shout()
#
# dog = Dog('dog')
# dog.shout()

'''
    虽然同样能实现功能，但这种实现大大增加了工作量。
    一是子类需要重写父类方法，二是将类名Cat、Dog都进行了硬编码，这种写法极不推荐。
'''
'''
    使用类方法实现构造方法
    我们定义一个Person类，它的__init__方法接收两个参数first和last分别用来接收用户的first_name和last_name。
    它还有一个name方法用来获取用户的全名。
'''

# class Person:
#     def __init__(self,first,last):
#         self.first_name = first
#         self.last_name = last
#
#     def name(self):
#         return self.first_name+self.last_name
#
# p = Person('江湖','十年')
# print(p.name()) # 江湖十年
#
# def generate_person(name):
#     if '-' in name:
#         first,last = name.split('-')
#     elif '_' in name:
#         first , last = name.split('_')
#     else:
#         first,last = name,''
#     return Person(first,last)
#
# p1 = generate_person('江湖-十年')
# p2 = generate_person('江湖_十年')
# p3 = generate_person('江湖十年')
#
# print(p1.name())
# print(p2.name())
# print(p3.name())

'''
    这样，不管我们爬到的用户名是哪种形式，都可以通过generate_person函数先预处理一下获取到first_name和last_name，
    然后实例化Person对象进行返回。
    
    其实，有一种更好的方式对用户名进行预处理，那就是使用类方法:
'''
# class Person:
#     def __init__(self,first,last):
#         self.first_name = first
#         self.last_name = last
#
#     def name(self):
#         return self.first_name+self.last_name
#
#     @classmethod
#     def new(cls, name):
#         if '-' in name:
#             first,last = name.split('-')
#         elif '_' in name:
#             first , last = name.split('_')
#         else:
#             first,last = name,''
#         return cls(first,last) # 返回了以该类为基础生成的对象
#
# p1 = Person.new('江湖-十年')#这里通过new方法，生成了一个对象，即通过类方法中的关键字cls(参数1，参数2)也可以创建对象
# p2 = Person.new('江湖_十年')#这里通过new方法，生成了一个对象，即通过类方法中的关键字cls(参数1，参数2)也可以创建对象
# p3 = Person.new('江湖十年')#这里通过new方法，生成了一个对象，即通过类方法中的关键字cls(参数1，参数2)也可以创建对象
#
# print(p1.name())
# print(p2.name())
# print(p3.name())

'''
    我们将generate_person函数移动到Person类内部作为一个类方法，并将其重命名为new,
    最后通过return一个cls实例来返回Person实例对象。
    
    熟悉Java等静态语言的同学应该很容易想到，这个类方法new实际上就是其他编程语言中的构造函数。
    所以我们也就通过类方法的形式，在Python中实现了构造方法(函数)。
    
    相比于使用generate_person函数生成Person实例对象，使用new构造方法的好处是代码封装性更强，也更容易理解。
    构造函数本就应该属于类的一部分，而不是单独写一个函数来实现。
    
    爬虫框架Scrapy的Item Pipeline中有一个from_crawler的类方法。
    实际上就是Scrapy提供给我们的一个构造方法。
'''

'''
    静态方法
    静态方法定义如下:
'''
from datetime import datetime

class Hello:
    def __init__(self,name):
        self.name = name

    def say_hello(self,create_time):
        print(f'hello {self.name} - {self.process_datetime(create_time)}' )

    @staticmethod # 静态方法主要用于处理一些突发的需要进行大量逻辑处理的代码块，便于封装
    def process_datetime(dt):
        return dt.strftime("%Y-%m-%d %H:%M:%S")

h = Hello('tim')
h.say_hello(datetime.now())

'''
    Hello类的process_datetime方法即为一个静态方法。
    可以看到静态方法的定义跟一个普通函数区别不大，只是在上面多了个@staticmethod装饰器。
    这个函数作用是对日期时间类型做格式化操作，返回我们想要的str类型的日期时间。
    在调用say_hello时可以通过参数传递进来一个create_time，我们想把它打印到hello name问候语句的后面。
    于是调用了process_datetime静态方法来对日期时间进行格式化处理。
    
    这个示例代码比较简单，所以优势不是很明显，但假设我们的process_datetime方法要大量逻辑要处理。
    这样单独提取出来一个静态方法，会比把所有逻辑写在say_hello方法内部更加合理，因为这样的话代码可读性会提高，并且可复用。
    
    对比来看，相较于类方法来说，静态方法更加简单，使用场景也更少。
    Django框架源码中有多处用到了staticmethod。
    比如在models中RegisterLookupMixin类下有一个merge_dicts方法作用就使用了静态方法将多个dict进行合并操作，
    这个操作不涉及类属性或实例属性的引用，所以使用静态方法比较合适。
    
'''


