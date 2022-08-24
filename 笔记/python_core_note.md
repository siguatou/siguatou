# python多线程 - 详解daemon属性值None,False,True的 区别

*每个进程至少要有一个线程，并为程序的入口，这个线程就是主线程;
*每个进程至少要有一个主线程，其他线程称为工作线程;
*父线程:如果线程A启动了线程B，A就是B的父线程;
*子线程:B就是A的子线程;

Python中，在构造线程对象时，可以设置daemon属性，这个属性必须在start()方法使用前设置好。
主线程是程序启动时的第一个线程，主线程可以再启动n个子线程。
daemon属性可以不设置 ，默认为None，主线程默认是False。

daemon属性值分为以下三种:
1)daemon = False
当子线程的daemon为False时，父线程在运行完毕后，会等待所有子线程退出才结束程序。

2)daemon = True
当子线程的daemon为True时，父线程在运行完毕后，子线程无论是否正在运行，都会伴随父线程一起退出。

3)不设置,或者daemon = None
daemon属性可以不设置，默认值是None
如果子线程设置 daemon = None，则实际运行的时候，子线程的 daemon属性值和父线程一致。

# 获取当前线程的名称

threading.currentThread().name

----------------------------------------------------------------------------------------------------

# 线程锁

Threading模块为我们提供了 一个类，Threading.Lock锁。
我们创建一个该类对象，在线程函数执行前，"抢占"该锁，执行完成后，"释放"该锁，则我们确保了每次只有一个线程占有该锁。
这时候对一个公共的对象进行操作，则不会发生线程不安全的现象了。

threading模块中提供了5种最常见的锁:

- 同步锁:lock(一次只能放行一个)
- 递归锁:rlock(一次只能放行一个)
- 条件锁:condition(一次可以放行任意个)
- 事件锁:event(一次全部放行)
- 信号量锁:semaphore(一次可以放行特定个)



# with语句

由于threading.Lock()对象中实现了__enter__()与__exit__()方法，故我们可以使用with语句进行上下文管理形式的加锁解锁操作:

num = 0

def add():

​	with lock:

​		#自动加锁

​			global num

​			for i in range(100):

​				print(i)

----------------------------------------------------------------------------------------------------

# 容器、迭代器、可迭代对象 、生成器之间的关系

-> list、set、tuple、dict都是容器;
-> 容器通常是一个可迭代对象;
-> 但凡可以返回一个迭代器的对象，都称之为可迭代对象;
-> 实现了迭代器协议方法的称作一个迭代器;
-> 生成器是一种特殊的迭代器;

# 容器

简单来说，容器就是存储一些事物的概念统称，它最大的特性就是给你一个事物，告诉我这个事物是否在这个容器内 。
在Python中，使用in或not in来判断某个事物是存在或者不存在某个容器内。

也就是说，一个对象实现了__contains__方法，我们都可以称之为容器。
在Python中，str、list、tuple、set、dic都是容器，因为我们可以用in或not in语法得知某个元素是否在容器内，它们内部都实现了__contains__方法。

如果我们想自定义一个容器，只需像下面这样:
class A(object):
	
	def __init__(self):
		self.items = [1,2]
		
	def __contains__(self,item):  # x in y
		return item in self.items

a = A()
print 1 in A  # True
print 2 in A  # True
print 3 in A  # False

但一个容器不一定支持输出存储在内的所有元素的功能。
一个容器要想输出保存在内的所有元素，其内部需要实现迭代器协议。 (重要!!!)

# 迭代器

一个对象如果实现了迭代器协议，就可以称之为迭代器。

在Python中实现迭代器，需要实现以下2个方法:
-> iter,这个方法返回对象本身;
-> Python2实现next，Python3实现__next__，这个方法每次返回迭代的值，在没有可迭代元素时，抛出StopIteration异常

下面我们实现一个自定义的迭代器:
class A(object):
	''' 内部实现了迭代器协议，这个对象就是一个迭代器'''
	def __init__(self,n):
		self.idx = 0
		self.n = n
		
	def __iter__(self):
		print('__iter__')
		return self
		
	def __next__(self):
		if self.idx < self.n:
			val = self.idx
			self.idx += 1
			return val
		else:
			raise StopIteration()

迭代元素

a = A(3)
for i in a:
	print i
print('-----------')

再次迭代，没有元素输出，迭代器只能迭代一次

for i in a:
	print(i)

__iter__

0

1 

2

---------

__iter__

在执行for循环时，我们看到__iter__的打印被输出，然后依次输出__next__中的元素。
其实，在执行for循环时，实际调用顺序是这样的:
for i in a => b=iter(a) => next(b) => next(b) ... => StopIteration => end

首选执行iter(a),iter会调用__iter__,在得到一个迭代器后，循环执行next,next会调用迭代器的next,在遇到StopIteration异常时停止迭代。
但注意，再次执行迭代器，如果所有元素都已经迭代完成，将不会再次迭代。
如果我们想每次执行都能迭代元素，只需在迭代时，执行的都是一个新的迭代器即可:
for i in A(3):
	print(i)
	每次执行一个新的迭代对象

for i in A(3):
	print(i)
	

# 可迭代对象

但凡是可以返回一个迭代器的对象，都可以称之为可迭代对象。
这句话怎么理解?

可以翻译为: __iter__方法返回迭代器，这个对象就是可迭代对象。
我们在上面看到的迭代器，也就是说实现了__iter__和__next__/next方法的类，这些类的实例就是一个可迭代对象。
迭代器一定是一个可迭代对象，但是可迭代对象不一定是迭代器。

这句话怎么理解?我们看代码:

class A(object):
	"""
		A的实例不是迭代器，因为A只实现了__iter__
		但这个类的实例是一个可迭代对象
		因为__iter__返回了B的实例，也就是返回了一个迭代器，因为B实现了迭代器协议
		返回一个迭代器的对象都被称为可迭代对象
	"""
	def __init__(self,n):
		self.n = n
		
	def __iter__(self):
		return B(self.n)

class B(object):
	"""
		这个类是个迭代器，因为实现了__iter__和__next__方法

"""

def __init__(self,n):
	self.idx = 0
	self.n = n
	
def __iter__(self):
	return self
	
def __next__(self):
	if self.idx < self.n:
		val = self.idx
		self.idx += 1
		return val
	else:
		raise StopIteration()	



b = B(3)           # b是一个迭代器，同时b是一个可迭代对象
for i in b:
	print(i)
print(iter(b))     # <__main__.B object at 0x10eb95450>

a = A(3)           # a不是一个迭代器，但a是可迭代对象，它把迭代细节都交给了B，B的实例是迭代器
for i in a:
	print(i)
print(iter(a))     # <__main__.B object at 0x10eb95550>
		
对于B:
-> B的实例是一个迭代器，因为其实现了迭代器协议__iter__和__next__方法;
-> 同时B的__iter__方法返回了self实例本身，也就是说返回了一个迭代器，所以B的实例b也是一个可迭代对象;

对于A:
-> A的实例不是一个迭代器，因为没有同时满足__iter__和__next__方法;
-> 由于A的__iter__返回了B的实例，而B的实例是一个迭代器，所以A的实例a是一个可迭代对象，换句话说，A把迭代细节交给了B;

其实我们使用的内置对象list、tuple、set、dict，都叫做可迭代对象，但不是一个迭代器，因为其内部都把迭代细节交给了另外一个类，这个类才是真正的迭代器。


生成器
生成器是一种特殊的迭代器，它也是一个可迭代对象。
有2种方式可以创建一个生成器:
-> 生成器表达式
-> 生成器函数

生成器表达式如下:
g = (i for i in range(5))   # 创建一个生成器
g
<generator object <genexpr> at 0x101334f50>
iter(g)                     # 生成器就是一个迭代器
for i in g:					# 生成器也是一个可迭代对象
	print(i)
	
生成器函数,包含yield关键字的函数:
def gen(n):
	# 生成器函数
	for i in range(n):
		yield i
		
g = gen(5)		# 创建一个生成器函数
print(g)		# <generator object gen at 0x10bb46f50>
print(type(g))	# <type 'generator'>

# 迭代
for i in g:
	print(i)

0 1 2 3 4

一般情况下，我们使用比较多的情况是以函数的方式创建生成器，也就是函数中使用yield关键字。

这个函数与包含return的函数执行机制不同:
-> 包含return的方法会以return关键字终结返回，每次执行都返回相同的结果;
-> 包含yield的方法一般用于迭代，每次执行遇到yield即返回yield后的结果，但内部会保留上次执行的状态，下次迭代继续执行yield之后的代码，直到再次遇到yield并返回;

当我们想得到一个很大的集合时，如果使用普通方法，一次性生成出这个集合，然后return返回:
def gen_data(n):
	return [i for i in range(n)] 	# 一次性生成大集合
	
但如果这个集合非常大时，就需要在内存中一次性占用非常大的内存。

使用yield能够完美解决这类问题，因为yield是懒惰执行的，一次只会返回一个值:
for gen_data(n):
	for i range(n):
		yield i  		# 每次只生成一个元素
		
生成器在Python中还有更大的用处，我们来看生成器中还有哪些方法:
g = (i for i in range(3))
dir(g)
['__class__','__init__','__iter__','__next__','send','throw'...]

我们发现生成器中包含了一个叫做send的方法，如何使用?
def gen(n):
	for i in range(n):
		a = yield i
		if a == 100:
			print('a is 100')
			
a = gen(10)
print(a.next())		# 0
print(a.next())		# 1
print(a.send(100))	# send(100)赋值给a，然后打印输出'a is 100'
print(a.next())		# 2

生成器允许在执行时，外部自定义一个值传入生成器内部，从而影响生成器的执行结果。
正因为有了这个机制，Python的生成器在开发中有了很大的应用场景。

总结:
迭代器、可迭代对象、生成器它们之间的区别和联系:
-> 迭代器必须实现迭代器协议__iter__和next/__next__方法
-> __iter__返回迭代器的对象称作可迭代对象 
-> 迭代器一定是一个可迭代对象，但可迭代对象不一定是迭代器，有可能迭代细节交付给另一个类，这个类才是迭代器
-> 生成器一定是一个迭代器，同时也是一个迭代对象
-> 生成器是一种特殊的迭代器，yield关键字可实现懒惰计算，并使得外部影响生成器的执行成为了可能！

-------------------------------------------------------------------------------------------------

Python技术进阶————yield

yield关键字在Python开发中使用较为频繁，它为我们在某些开发场景中提供了便利 ，这篇文章我们来深入讲解yield相关知识。

生成器
在讲yield之前，我们先复习一下迭代器与生成器的区别。
简单总结如下:
-> 实现了迭代器协议__iter__和next/__next__方法的对象被称作迭代器;
-> 迭代器可以使用for执行输出每个元素
-> 生成器是一种特殊的迭代器

一个函数内，如果包含了 yield关键字，这个函数就是一个生成器。

coding:utf8

def gen(n):

生成器函数

​	for i in range(n):
​		yield i
​		
g = gen(5)		# 创建一个生成器

生成器迭代

for i in g:
	print(i)
	

output:

0 1 2 3 4

注意,在执行g = gen(5)时，函数中的代码并没有执行，此时我们只是创建了一个生成器对象，他的类型是generator。
当执行for i in g时，每执行一次循环，直到执行到yield时，返回yield后面的值。

换句话说，我们想输出5个元素，在创建生成器时，这个5个元素此时并没有有产生，什么时候产生呢?
在执行for循环遇到yield时，此时才会逐个生成每个元素。

生成器除了实现迭代器协议之外，还包含了一些方法:
-> generator.next():每次执行到遇到yield后返回，直到没有yield，抛出StopIterator异常
-> generator.send(value):将yield的值设置为value
-> generator.throw(type[,value[,traceback]]):向生成器当前状态抛出一个异常
-> generator.close():关闭生成器

next
为了更便于理解只有在遇到yield时才产生值，我们改写程序如下:

coding:utf8

def gen(n):
	# 生成器函数
	for i in range(n):
		print('yield before')
		yield i
		print('yield after')
		
g = gen(3)		# 创建一个生成器
print(g.next()) # 0
print('-'*5)	
print(g.next()) # 1
print('-'*5)
print(g.next()) # 2
print('-'*5)
print(g.next()) # StopIteration

Output:

yield before

0 

-----

yield after

yield before

1

-----

yield after

yield before

2

-----

yield after

Trackback (most recent call last):

File "test.py", line 17, in <modules>

print(g.next())

StopIteration

只有在执行g.next()时，才会产生值，并且生成器会保留上下文信息，在再次执行g.next()时继续返回。

send
上面的例子只展示了在yield后面有值的情况，其实也可以使用j = yield i这种语法，我们看下面的代码:

coding:utf8

def gen():
	i = 1
	while True:
		j = yield i
		i *= 2
		if j == -1:
			break
			
如果我们执行:
g = gen()

for i in g:
	print(i)

Output:

1

2

4

8

16

32

64

...

这个生成器函数相当于无限生成每次翻倍的数字，一直循环下去，直到我们杀死进程才能停止。
在上面的代码中你会发现，永远执行不到j == -1这个分支里，如果想让代码执行到这，如何做？

这里就要用到生成的send()方法，它可以在外部传入一个值，使得改变生成器当前的状态。

g = gen()		# 创建一个生成器
print(g.next())	# 1
print(g.next())	# 2
print(g.next())	# 4
print(g.send(-1)) # j = -1 程序退出

执行g.send(-1),相当于把-1传入生成器，赋值给了yield之前的j，从而改变了生成器内部的执行状态。


throw
除了可以向生成器内部传入指定值，还可以传入指定异常:

coding:utf8

def gen():
	try:
		yield 1
	except ValueError:
		yield 'ValueError'
	finally:
		print('finally')
	
g = gen()	# 创建一个生成器
print(g.next())	# 1
print(g.throw(ValueError))	# 向内部传入异常，返回ValueError，并打印出finally

throw与next类似，但是以传入异常的方式使生成器执行，throw一般在开发中很少被用到。


使用场景
大列表的生成
如果你想生成一个非常大的列表，使用list时只能一次性在内存中创建出这个列表，这 可能导致内存资源申请非常大，甚至有可能被操作系统杀死进程。
直接在内存中生成一个大列表:

coding:utf8

def big_list():
	result = []
	for i in range(100000000000000000000):
		result.append(i)
	return result
	
# 一次性在内存中生成大列表，内存占用非常大
for i in big_list():
	print(i)
	
由于生成器只有在执行到 yield时才会产生值，我们可以使用这个特性优雅地解决这类问题。

coding:utf8

def big_list():
	for i in range(100000000000000000000000):
		yield i
		

大列表只有在迭代时，才逐个生成元素，减少内存占用 

for i in big_list():
	print(i)
	
简化代码结构

# 小贴士:

1、遇到json字典形式的字符串数据，可以将其保存在Pycharm的.json文件中，然后使用格式化命令进行文件格式化;

通过快捷键Ctrl+Shift+"+"展开.json文件,通过Ctrl+Shift+"-"收缩.json文件



### GIT简介：

1、什么是GIT

git是一个开源的分布式版本控制系统，用于高效地管理各种大小项目和文件。

2、代码管理工具的用途

- 防止代码丢失，做备份；
- 项目的版本管理和控制，可以通过设置节点进行跳转；
- 建立各自的开发环境分支，互不影响，方便合并；
- 在多终端开发时，方便代码的相互传输；

3、git的特点

- git是开源的，多在*nix下使用，可以管理各种文件；
- git是分布式的项目管理工具(svn是集中式的)；
- git数据管理更多样化，分享速度快，数据安全；
- git拥有更好的分支支持，方便多人协调；

4、git安装

sudo apt-get install git

### GIT使用：

![git](/home/xieyiyang/Pictures/git.png)



基本概念：

- 工作区：项目所在操作目录，实际操作项目的区域
- 暂存区：用于记录工作区的工作(修改)内容
- 仓库区：用于备份工作区的内容
- 远程仓库：远程主机上的GIT仓库






























​	







​	