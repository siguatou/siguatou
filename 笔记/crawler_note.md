## 爬取网站思路

1.先确定是否为动态加载网站  ->  通过查看网页源代码，来确定是否有自己需要的信息(注意：有些网页虽然是静态网页，但是随着下拉框的移动，有些标签的class属性会发生改变。此时，通常是原来的class属性值是可以定位元素的！)
2.找URL规律
3.正则表达式
4.定义程序框架，补全并测试代码

## 第一次安装mysql数据库之后的注意事项：

1.第一次登录使用sudo mysql,否则登录不上;
2.如果使用sudo mysql也登录不上的话，找到mysqld.cnf配置文件，在[mysqld]下添加skip-grant-tables，保存即可。注意要修改文件权限，保存完成之后要把文件权限再改回来;
3.然后进入mysql中，use mysql,找到user表;
4.输入update user set authentication_string=password('新密码') where user='root';
　　　　flush privileges;
5.更改好新的密码之后，退出mysql;
6.再把mysqld.cnf中的skip-grant-tables注释掉;
7.重启mysql;
8.然后就可以正常进入mysql了;
注意：如果上述方法还是不行，那就把现有的root账户删除，然后重新创建一个Host=%的root账户，plugin为空;
       再把所有的权限加给新创建的root账户;

## 爬虫增量爬取的思路

1.MySQL中新建表 request_finger，存储所有爬取过的链接的指纹;
2.在爬取之前，先判断该指纹是否爬取过，如果爬取过，则不再继续爬取;

## 使用requests库遇到字符编码问题的对应

下面这种写法可以规避字符编码错误的情况

html = requests.get(url=url,headers=headers).content.decode()
html = requests.get(url=url,headers=headers).text

## 使用os创建文件夹的两种方法

如果使用os.mkdir()，则不能递归创建，即如果存在两级文件路径不存在，就无法使用。

而使用os.makedirs(directory)，就可以全过程生成文件夹。



contains():匹配属性值中包含某些字符串节点

查找id属性值中包含字符串"car_"的li节点

//li[contains(@id,'car_')]

## 如果xpath的解析路径复杂，可以考虑使用//

.//p[@class='name']/a/text()   即获取在当前元素节点下的🥰️后代节点🥰️属性class='name'的p节点下的a字节点的文本数据，使用//可以跳过中间节点，直接定位到p节点;

目前反爬总结
1.基于User-Agent反爬;
2.如果数据出不来可考虑更换**IE**的User-Agent尝试，数据返回最标准;

## urllib库使用流程

编码

params = {
	'':'',
	'':''
}
params = urllib.parse.urlencode(params)
url = baseurl + params  # url拼接

#请求
request = urllib.request.Request(url,headers = headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')

## requests模块使用流程

params = {
	'':'',
	'':''
}
baseurl = 'http://tieba.baidu.com/f?'
html = requests.get(baseurl,params = params,headers = headers).content.decode('utf-8','ignore')

响应对象res属性
res.text : 字符串
res.content : bytes
res.encoding : 字符编码  res.encoding = 'utf-8'
res.status_code : HTTP响应码
res.url : 实际数据URL地址

正则解析re模块
import re

pattern = re.compile(r'正则表达式',re.S)
r_list = pattern.findall(html)

----------------------------------------------------------

lxml解析库
from lxml import etree

parse_html = etree.HTML(res.text)
r_list = parse_html.xpath('xpath表达式')

----------------------------------------------------------
xpath表达式
->匹配规则
1.节点对象列表://div、//div[@class="student"]、//div/a[@title='stu']/span
2.字符串列表:xpath表达式中末尾为：@src、@href、text()

->xpath高级
1.基准xpath表达式：得到节点对象列表
2.for r in [节点对象列表]:
      username = r.xpath('./xxxxxx')

此处注意遍历后继续xpath一定要以:  . 开头,代表当前节点

----------------------------------------------------------
## 爬虫时注意：

# 最终目标: 不要使你的程序因为任何异常而终止
1.页面请求设置超时时间,并用try捕捉异常，超过指定次数则更换下一个URL地址;
2.所抓取任何数据，获取具体数据前先判断是否存在该数据，可使用列表推导式;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
(重要！)3.通常的网页爬取，使用get再加上headers即可爬取;如果获取不到数据，要注意检查headers里的参数，有些参数是不需要的。一般保留cookie,User-Agent,即可。

# 多级页面数据爬取注意：
1.主线函数：解析一级页面函数(将所有数据从一级页面中解析并抓取)

----------------------------------------------------------

## 增量爬虫如何实现？

1.数据库中创建指纹表，用来存储每个请求的指纹;
2.在抓取之前，先到指纹表中确认是否之前抓取过;

## 爬虫基本步骤：

1.查看是否为静态页面;
2.确定xpath表达式;
3.对所要爬取的内容进行source code检查，如果源代码难以区分，可以进行在线格式化的工具生成一下，然后再源代码里查找所要定位的内容;

## requests中的params参数

特点：1.url为基准的url地址，不包含查询参数;
            2.该方法会自动对params字典编码，然后和url拼接;
      
Web客户端验证参数-auth
1.针对于需要web客户端用户名密码认证的网站
2.auth=('username','password') # 注意参数类型为一个元组，元组里是用户名和密码
3.requests.get(url=url,headers=headers,auth=auth)

## SSL证书认证参数-verify

适用网站及场景

1、适用网站：https类型网站但是没有经过证书认证机构认证的网站;
2、适用场景：抛出SSLError异常则考虑使用此参数;

# 参数类型
1、verify=True(默认):检查证书认证
2、verify=False(常用):忽略证书认证

# 示例
response = requests.get(
	url = url,
	params = params,
	headers = headers,
	verify = False
)

-------------------------------------------------------------------
代理参数-proxies
#定义
1.定义：代替你原来的IP地址去对接网络的IP地址;
2.作用：隐藏自身真实IP，避免被封;

普通代理
# 获取代理IP网站
西刺代理、快代理、全网代理、代理精灵、……

# 参数类型
1、语法结构
	proxies = {
		'协议':'协议://IP:端口号'
	}
2、示例
	proxies = {
		'http':'http://IP:端口号',
		'https':'https://IP:端口号'
}		

高匿：高度匿名，web站点只能看到代理IP -> 优先选择
透明：Web站点能看到代理IP和用户自身真实IP
普通:   Web站点能看到代理IP和知道有人通过代理IP访问，但是不知道用户真实IP

思考：建立一个自己的代理IP池，随时更新用来抓取网站数据
1、从西刺代理IP网站上，抓取免费代理IP;
2、测试抓取的IP，可用的保存在文件中;

-------------------------------------------------------------------

常见的反爬机制及处理方式
1、Headers反爬虫：Cookie、Referer、User-Agent
   解决方案：通过F12获取headers，传给requests.get()方法
2、IP限制：网站根据IP地址访问频率进行反爬，短时间内限制IP访问
   解决方案：  1、构造自己IP代理池，每次访问随机选择代理，经常更新代理池;
            			 2、购买开放代理或私密代理IP;
             			3、降低爬取的速度;
3、User-Agent限制：类似于IP限制
   解决方案：构造自己的User-Agent池，每次访问随机选择;
4、对查询参数或Form表单数据认证(salt、sign)
   解决方案：找到JS文件，分析JS处理方法，用Python按同样方法处理;
5、对响应内容做处理
   解决方案：打印并查看响应内容，用xpath或正则做处理;

-------------------------------------------------------------------

## 控制台抓包

打开方式及常用选项

1、打开浏览器，F12打开控制台，找到network选项卡;
2、控制台常用选项：
   *Network:抓取网络数据包
   	1、ALL:抓取所有的网络数据包;
   	2、XHR:抓取异步加载的网络数据包;
   	3、JS:抓取所有的JS文件;
   *Sources:格式化输出并打断点调试JavaScript代码，助于分析爬虫中一些参数（重要！！！！）
   *Console:交互模式，可对JavaScript中的代码进行测试;
3、抓取具体网络数据包后
   1、单击左侧网络数据包地址，进入数据包详情，查看右侧;
   2、右侧:
       1、Headers:整个请求信息
           General、Response Headers、Request Headers、Query String、Form Data
       2、Preview:对响应内容进行预览
       3、Response:响应内容
4、JS抓包的时候，如果遇到无法辨别的变量，可以进行断点调试，进行一个输入操作，然后查看无法辨别变量的值;  (重要！！！）
5、抓包时，在FormData中如果发现salt,sign这样的字段，就要提高警惕，会存在反爬操作，需要自己编码生成必要的数据。具体要查看js的编码方式，然后确定如何通过python脚本生成数据；

扩展
1.建立增量爬虫 - 网站有更新时抓取，否则不抓
	#数据库中建立version表，存储抓取过的url地址
	
2.所抓数据存到数据库，按照层级关系分表存储 - 省、市、县表
	北京市  北京市 东城区 
	广东省  广州市 越秀区
	
-------------------------------------------------------------------

## 动态加载数据抓取-Ajax

# 特点
1、右键 -> 查看网页源码中没有具体数据;
2、滚动鼠标滑轮或其他动作时加载，或者页面局部刷新;

# 抓取
1、F12打开控制台，页面动作抓取网络数据包;
2、抓取json文件URL地址;
# 控制台中 XHR : 异步加载的数据包
# XHR -> QueryStringParameters(查询参数)

-------------------------------------------------------------------

有道翻译爬虫案例详细分析
1、打开首页
2、准备抓包:F12开启控制台
3、寻找地址
	页面中输入翻译单词，控制台中抓取到网络数据包，查找并分析返回翻译数据的地址
4、发现规律
	找到返回具体数据的地址，在页面中多输入几个单词，找到对应URL地址，分析对比Network - ALL(或者XHR）- Form Data，发现对应规律
5、寻找JS文件
	右上角 ... -> Search -> 搜索关键字 -> 单击 -> 跳转到Sources,左下角格式化符号{}

-------------------------------------------------------------------

知识点回顾
*队列
#导入模块
from queue import Queue

#使用
q = Queue()
q.put(url)
q.get() # 当队列为空时，阻塞
q.get(block=True,timeout=3) # 超过3秒抛异常
q.get(block=False) # 为空直接抛异常
q.empty() # 判断队列是否为空，True/False

## *线程模块

导入模块

from threading import Thread

# 使用流程
t = Thread(target=函数名) # 创建线程对象
t.start()  # 创建并启动线程
t.join()  # 阻塞等待回收线程

# 如何创建多线程？
技巧：多线程爬虫，要注意创建一个队列对象，from queue import Queue，用来存储所有的URL。
     对应爬取网页URL时，分别一个线程分配一个URL。

-------------------------------------------------------------------

多线程爬虫流程：
1、将待爬取的URL地址存放到队列中;
2、多个线程从队列中获取地址，进行数据抓取;
3、注意获取地址过程中程序阻塞问题;
	# 写法:
​	while True:
​	    try:
​	        url = q.get(block=True,timeout=3)
​		xxx xxx
​	    except Exception as e:
​	    	break


*将抓取数据保存到同一文件
# 注意多线程写入的线程锁问题
from threading import Lock
lock = Lock()
lock.acquire()
python代码块
lock.release()

## 线程安全

下面有一个数值num初始值为0,我们开启2条线程:

-> 线程1对num进行一千万次+1的操作

-> 线程2对num进行一千万次-1的操作

*# 结果三次采集*
*# num result : 669214*
*# num result : -1849179*
*# num result : -525674*

上面就是非常好的案例,想要解决这个问题就必须通过锁来保障线程切换的时机。

需要注意的是，在Python基本数据类型中list、typle、dict本身就是线程安全的，所以如果有多个线程对这3种容器做操作时，我们不必考虑线程安全的问题。

## 锁的作用

锁是Python提供给我们能够自行操控线程切换的一种手段，使用锁可以让线程的切换变得有序。

一旦线程的切换变得有序后，各个线程之间对数据的访问、修改就变得可控，所以若要保证线程安全，就必须使用锁。

threading模块中提供了5种最常见的锁，按照功能划分如下:

- 同步锁:lock(一次只能放行一个)

- 递归锁:rlock(一次只能放行一个)

- 条件锁:condition(一次可以放行任意个)

- 事件锁:event(一次全部放行)

- 信号量锁:semaphore(一次可以放行特定个)

  

-------------------------------------------------------------------

cookie模拟登录
适用网站及场景 -> 抓取需要登录才能访问的页面

cookie和session机制
# http协议为无连接协议
cookie:存放在客户端浏览器
session:存放在web服务器

方法1：headers中加入对应cookie

方法2：
原理 -> 1、把抓取到的cookie处理为字典;
        2、使用requests.get()中的参数:cookies;
	res = requests.get(
		url = url,
		params = params,
		auth = auth,
		proxies = proxies,
		headers = headers,
		timeout = 5,
		cookies = cookies
	)
        
处理cookie为字典，用过requests.get(cookies=cookies)发起请求

方法3：
原理思路及实现

#1.思路
requests模块提供了session类，来实现客户端和服务端的会话保持;

#2.原理
1、实例化session对象
   session = requests.session()
2、让session对象发送get或者
请求
   res = session.post(url=url,data = data,headers = headers)
   res = session.get(url = url, headers = headers)

#3.思路梳理
浏览器原理：访问需要登录的页面会带着之前登录过的cookie;
程序原理: 同样带着之前登录的cookie去访问 - 由session对象完成
1、实例化session对象
2、登录网站：session对象发送请求，登录对应网站，把cookie保存在session对象中
3、访问页面：session对象请求需要登录才能访问的页面，session能够自动携带之前的这个cookie，进行请求

具体步骤：
1、寻找Form表单提交地址 - 寻找登录时POST的地址
	查看网页源码，查看Form表单，查找action对应的地址：http://www.renren.com/PLogin.do
2、发送用户名和密码信息到POST的地址
	* 用户名和密码信息以什么方式发送? -- 字典
	键 :  <input>标签中的name值 (email,password)
	值 :  真实的用户名和密码 post_data = {'email':'','password':''}
	

session = requests.session()
session.post(url=url,data=data)

-------------------------------------------------------------------

phantomjs浏览器
# 定义
	无界面浏览器(又称无头浏览器),在内存中进行页面加载，高效。

Tip:如何快速在windows中找到某文件的保存位置？  -> CMD打开DOS，输入where + 文件名，回车，即可

Linux系统中下载geckodriver.tar.gz
1、下载后解压 -> tar -zxvf geckodriver.tar.gz
2、拷贝解压后文件到 /usr/bin/ (添加环境变量) -> sudo cp geckodriver /usr/bin/
3、更改权限  ->  sudo -i; cd /usr/bin/;  chmod 777 geckodriver;
4、更改完毕后，可以通过命令查看geckodriver文件的权限 -> ls -l geckodriver;
(重要)Tip:如何判断网页是否为最后一页？ -> self.browser.page_source.find('pn-next disabled') == -1?   -1说明没找到，不是最后一个页，故点击 下一页 按钮

-------------------------------------------------------------------

回顾

cookie模拟登录
1、适用网站类型：爬取网站页面时需要登录后才能访问，否则获取不到页面的实际响应数据;
2、方法1(利用cookie)
    1、先登录成功1次，获取到携带登录信息的cookie(处理headers)
    2、利用处理的headers向URL地址发请求
3、方法2(利用requests.get()中cookies参数)
    1、先登录成功一次，获取到cookie，处理为字典
    2、res=requests.get(xxx,cookies=cookies)
4、方法3(利用session会话保持)
    1、实例化session对象
       session = requests.session()
    2、先post :
       session.post(post_url,data = post_data,headers = headers)
       1、登录，找到POST地址: form -> action对应地址
       2、定义字典，创建session实例发送请求 —> 字典key:<input> 标签中name的值(email,password)
       					   ——> post_data = {'email':'','password':''}
       3、再get: session.get(url,headers=headers)   

三个池子
1、User-Agent池
2、代理IP池
3、cookie池

-------------------------------------------------------------------
chromedriver设置无界面模式
from selenium import webdriver

options = webdriver.ChromeOptions()
#添加无界面参数
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.png')
       					
#导入鼠标事件类
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 移动到 设置，perform()是真正执行操作，必须有
element = driver.find_element(By.XPATH,'//*[@id="ul"]/a[8]')
ActionChains(driver).move_to_element(element).perform()

# 单击，弹出的Ajax元素，根据链接节点的文本内容查找
driver.find_element(By.XPATH,'text()="高级搜索"').click()

-------------------------------------------------------------------

selenium -  切换页面

# 适用网站 -> 页面中点开链接出现新的页面，但是浏览器对象browser还是之前页面对象

# 应对方案 
   获取当前所有句柄(窗口) -> all_handles = browser.window_handles
   切换browser到新的窗口,获取新窗口的对象 -> browser.switch_to.window(all_handles[1])

-------------------------------------------------------------------

mysql数据库select查询语句举例
sel = "select * from version where url=%s"
result = self.cursor.execute(sel,[href])  # result返回数字，表示受影响的记录条数，即，可以查看是否为0,来判断有没有select到数据记录

if result:
   print('网站未更新,无需抓取')
else:
   (执行代码语句)

self.db.commit()

-------------------------------------------------------------------

#### (重要)python语法中的切片用法 -> 取列表的后四位: list1[-4:];  取列表的后两位: list1[-2:] ; 取列表的前两位: list1[:2]; 取列表的前四位: list1[:4]

-------------------------------------------------------------------

selenium - Web客户端验证
弹窗中的用户名和密码如何输入？
-> 不用输入，在URL地址中输入就可以

-------------------------------------------------------------------

selenium - Web客户端验证
弹窗中的用户名和密码如何输入？ -> 不用输入，在URL地址中输入即可;

-------------------------------------------------------------------

selenium - iframe子框架(重要)

# 特点 -> 网页中嵌套了网友也，先切换到iframe子框架，然后再执行其他操作;
# 方法 -> browser.switch_to.iframe(iframe_element)

例: QQ邮箱登录


# selenium常用操作
1、键盘操作
   from selenium.webdriver.common.keys import Keys
   node.send_keys(Keys.SPACE)
   node.send_keys(Keys.CONTROL,'a')
   node.send_keys(Keys.CONTROL,'c')
   node.send_keys(Keys.CONTROL,'v')
   node.send_keys(Keys.ENTER)

2、鼠标操作
   from selenium.webdriver import ActionChains
   mouse_action = ActionChains(browser)
   mouse_action.move_to_element(node)
   mouse_action.perform()

3、切换句柄
   all_handles = browser.window_handles
   browser.switch_to.window(all_handles[1])

4、iframe子框架
   browser.switch_to.frame(iframe_element)

5、web客户端验证
url = 'http://用户名:密码@正常地址'

-------------------------------------------------------------------

# execjs模块使用
1、安装
sudo pip3 install pyexecjs

2、使用
with open('file.js','r') as f:
   js = f.read()

obj = execjs.compile(js)
result = obj.eval('string')

-------------------------------------------------------------------

百度翻译破解案例
#目标 -> 破解百度翻译接口，抓取翻译结果数据

#实现步骤
1、F12抓包，找到json的地址，观察查询参数
     1、POST地址: https://fanyi.baidu.com/v2transapi
     2、Form表单数据(多次抓取在变的字段)
     	from: zh
     	to: en
     	sign : 54706.276099 # 这个是如何生成的？
     	token: a927248ae7146c842bb4a94457ca35ee # 基本固定，但是也想办法获取
     	
2、抓取相关JS文件
     1、右上角 - 搜索 - sign: - 找到具体JS文件
       (index_c8a141d.js) - 格式化输出

3、在JS中寻找sign的生成代码
     1、在格式化输出的JS代码中搜索: sign: 找到如下JS代码: sign : m(a),
     2、通过设置断点，找到m(a)函数的位置，即生成sign的具体函数
     
具体代码实现
1、获取token和gtk的值
  GET地址：百度翻译首页发请求，从响应内容获取;https://fanyi.baidu.com/?aldtype=16047
2、POST请求
  https://fanyi.baidu.com/v2transapi
  res = requests.post(URL,data=data,headers=headers)

-------------------------------------------------------------------

scrapy框架
#定义 -> 异步处理框架，可配置和可扩展程度非常高，Python中使用最广泛的爬虫框架;

#安装 ->
   # Ubuntu安装
   1、安装依赖包
       1、sudo apt-get install libffi-dev
       2、sudo apt-get install libssl-dev
       3、sudo apt-get install libxml2-dev
       4、sudo apt-get install python3-dev
       5、sudo apt-get install libxslt1-dev
       6、sudo apt-get install zlib1g-dev
       7、sudo pip3 install -I -U service_identity
       
   2、安装scrapy框架
       1、sudo pip3 install Scrapy

# Scrapy五大组件:
   1、引擎 ->      : 整个框架核心
   2、调度器 ->    : 维护请求队列
   3、爬虫文件 ->  : 数据解析提取
   4、下载器 ->    : 获取响应对象
   5、项目管道 ->  : 数据入库处理


   1、引擎 ->  I 整个框架的核心，所有数据流的传输都要经过引擎;引擎向爬虫文件索要第一个要爬取的URL地址;
   2、调度器 -> II 引擎把获取到的URL地址传给调度器队列;然后出队列，再把URL传给引擎;
   3、爬虫文件 -> V 引擎把response传给爬虫文件，爬虫文件解析数据; VI 爬虫文件把解析好的数据和继续跟进的URL，传给引擎;
   4、下载器 ->  III 引擎再把URL传给下载器; IV 下载器根据URL，通过Internet访问服务器，将获取到的response返回给引擎;
   5、项目管道 -> VII 引擎将解析好的数据传给项目管道;

-------------------------------------------------------------------

(重要！)
# 下载器中间件(Downloader Middlewares) : 引擎 -> 下载器，包装请求(随机代理等)
# 蜘蛛中间件(Spider Middlewares) : 引擎 -> 爬虫文件，可修改响应对象属性

# Scrapy爬虫工作流程
doesn't match either of '*.cdn.myqcloud.com',
# 爬虫项目启动
1、由引擎向爬虫程序索要第一个要爬取的URL，交给调度器去入队列
2、调度器处理请求后出队列，通过下载器中间件交给下载器去下载
3、下载器得到响应对象后，通过蜘蛛中间件交给爬虫程序
4、爬虫程序进行数据提取:
   1、数据交给管道文件去入库处理;
   2、对于需要继续跟进的URL，再次交给调度器入队列，依次循环;

-------------------------------------------------------------------

# Scrapy常用命令
1、创建爬虫项目

scrapy startproject 项目名

2、创建爬虫文件

scrapy  genspider 爬虫名 域名

3、运行爬虫

scrapy crawl 爬虫名

-------------------------------------------------------------------

全局配置文件settings.py详解

1.定义User-Agent

USER_AGENT= 'Mozilla/5.0'

2.是否遵循robots协议，一般设置为False

ROBOTSTXT_OBEY = False

3.最大并发量，默认为16

CONCURRENT_REQUESTS = 32

4.下载延迟时间，控制爬取时间

#### DOWNLOAD_DELAY = 1（重要！！）

5.请求头，此处也可以添加User-Agent

-------------------------------------------------------------------

创建爬虫项目步骤
1、新建项目: scrapy startproject 项目名
2、cd 项目文件夹
3、新建爬虫文件 : scrapy genspider 文件名 域名
4、明确目标(items.py)
5、写爬虫程序(文件名.py)
6、管道文件(pipelines.py)
7、全局配置(settings.py)
8、运行爬虫:scrapy crawl 爬虫名

-------------------------------------------------------------------

Tips:linux系统中，查看文件存储结构路径的命令: tree 文件名

-------------------------------------------------------------------

Scrapy知识点汇总
## 节点对象.xpath('')
1、列表，元素为选择其['<selector data='A'>]
2、列表.extract():序列化列表中所有选择其为Unicode字符串['A','B','C']
3、列表.extract_first()或者get():获取列表中第1个序列化的元素(字符串)

## pipelines.py中必须有1个函数叫process_item
def process_item(self,item,spider):
    return item
## 必须返回item，此返回值会传给下一个管道的此函数继续处理

-------------------------------------------------------------------

日志的变量及日志的级别(settings.py)

## 日志相关变量
LOG_LEVEL = ''
LOG_FILE = '文件名.log' -> 输出log文件，记录log信息

# 日志级别

5 CRITICAL : 严重错误
4 ERROR : 普通错误
3 WARNING : 警告
2 INFO : 一般信息
1 DEBUG : 调试信息

## 注意: 只显示当前级别的日志和比当前级别日志更严重的

-------------------------------------------------------------------

管道文件使用
1、爬虫文件中为items.py中类做实例化，用爬下来的数据给对象赋值
	from ..items import MaoyanItem
	item = MaoyanItem()
	item['数据变量名'] = 数据变量
2、管道文件(pipelines.py)
3、开启管道(settings.py)
	ITEM_PIPELINES = {'项目目录名.pipelines.类名':优先级}

-------------------------------------------------------------------

(重要！)Scrapy中，将输出信息保存为csv、json文件

命令格式

scrapy crawl maoyan -o maoyan.csv
scrapy crawl maoyan -o maoyan.json

## settings.py中设置导出编码
FEED_EXPORT_ENCODING = 'utf-8'

-------------------------------------------------------------------

Scrapy工作流程
1、Engine向Spider索要URL，交给 Scheduler入队列
2、Scheduler处理后出队列，通过Downloader Middlewares交给Downloader去下载
3、Downloader得到响应后，通过Spider Middlewares交给Spider
4、Spider数据提取:
    1、数据交给Pipeline处理
    2、需要跟进URL，继续交给Scheduler入队列，依次循环
    
-------------------------------------------------------------------

常用命令
#创建爬虫项目
scrapy startproject 项目名

#创建爬虫文件
cd 项目文件夹
scrapy genspider 爬虫名 域名

#运行爬虫
scrapy crawl 爬虫名

-------------------------------------------------------------------

Scrapy使用流程
1.scrapy startproject Tencent
2.cd Tencent
3.scrapy genspider tencent tencent.com
4.items.py(定义爬取数据结构)
	import scrapy
	class TencentItem(scrapy.Item):
		job_name=scrapy.Field()
5.tencent.py(写爬虫文件)
	import scrapy
	class TencentSpider(scrapy.Spider):
		name = 'tencent'
		allowed_domains = ['tencent.com']
		start_urls = ['http://tencent.com/']
		def parse(self,response):
			pass
		
6.pipelines.py(数据处理)
	class TencentPipeline(Object):
		def process_item(self,item,spider):
			return item
7.settings.py(全局配置)
	ROBOTSTXT_OBEY = False
	DEFAULT_REQUEST_HEADERS = {}
	ITEM_PIPELINES = {'':200}
8.终端:scrapy crawl tencent

-------------------------------------------------------------------

响应对象属性及方法
## 属性
1、response.text: 获取响应内容 - 字符串
2、response.body: 获取bytes数据类型
3、response.xpath('')

## response.xpath('')调用方法
1、结果:列表，元素为选择器对象
	# <selector xpath='//article' data=''>
2、.extract():提取文本内容，将列表中所有元素序列化为Unicode字符串
3、.extract_first():提取列表中第一个文本内容
4、.get():提取列表中第一个文本内容

-------------------------------------------------------------------

爬虫项目启动方式

方式一
1、从爬虫文件(spider)的start_urls变量中遍历URL地址，把下载器返回的响应对象(response)交给爬虫文件的parse()函数处理
2、# start_urls = ['http://www.baidu.com/']

方式二
重写start_requests()方法，从此方法中获取URL，交给指定的callback解析函数处理

1、去掉start_urls变量
2、def start_requests(self):
	# 生成要爬取的URL地址，利用scrapy.Request()方法交给调度器
	
-------------------------------------------------------------------

日志级别

DEBUG < INFO < WARNING < ERROR < CRITICAL

-------------------------------------------------------------------

数据持久化存储(MySQL、MongoDB)
1、在 settings.py中定义相关变量
2、pipelines.py中新建管道类，并导入settings模块
	def open_spider(self,spider):
		# 爬虫开始执行1次，用于数据库连接
		
	def process_item(self,item,spider):
		# 用于处理抓取的item数据
		
	def close_spider(self,spider):
		# 爬虫结束时执行1次，用于断开数据库连接
3、settings.py中添加此管道
	ITEM_PIPELINES ={'':200}
	
## 注意: process_item() 函数中一定要return item

-------------------------------------------------------------------

保存为csv、json文件
## 命令格式
scrapy crawl maoyan -o maoyan.csv
scrapy crawl maoyan -o maoyan.json
## settings.py FEED_EXPORT_ENCODING = 'utf-8'

-------------------------------------------------------------------

settings.py常用变量
#1、设置日志级别
LOG_LEVEL = ''
#2、保存到日志文件(不在终端 输出)
LOG_FILE = ''
#3、设置数据导出编码(主要针对于json文件)
FEED_EXPORT_ENCODING = ''
#4、非结构化数据存储路径
IMAGES_STROE = '路径'
#5、设置User-Agent
USER_AGENT = ''
#6、设置最大并发数(默认为16)
CONCURRENT_REQUESTS = 32
#7、下载延迟时间(每隔多长时间请求一个网页)
###### DOWNLOAD_DELAY 会影响 CONCURRENT_REQUESTS,不能使并发显现’
###### 有CONCURRENT_REQUESTS,没有DOWNLOAD_DELAY: 服务器会在同一时间收到大量的请求
###### 有CONCURRENT_REQUESTS,有DOWNLOAD_DELAY时，服务器不会在同一时间收到大量的请求
DOWNLOAD_DELAY = 3
#8、请求头
DEFAULT_REQUEST_HEADERS = {}
#9、添加项目管道
ITEM_PiPELINES = {}
#10、添加下载器中间件
DOWNLOADER_MIDDLEWARES = {}

-------------------------------------------------------------------

非结构化数据抓取
1、spider
	yield item['链接']
2、pipelines.py
	from scrapy.pipelines.images import ImagesPipeline
	import scrapy
	class TestPipeline(ImagesPipeline):
		def get_media_requests(self,item,info):
			yield scrapy.Request(url=item['url'],meta={'item':item['name']})
		
		def file_path(self,request,response=None,info=None):
			name = request.meta['item']
			filename = name
			return filename
3、settings.py
	IMAGES_STORE = 'D:\\Spider\\images'			


-------------------------------------------------------------------

scrapy.Request()参数
1、url
2、callback
3、meta:传递数据，定义代理
	
-------------------------------------------------------------------

scrapy.Request()

#### 参数

1、url
2、callback
3、headers
4、meta : 传递数据，定义代理
5、dont_filter : 是否忽略域组限制 - 默认False，检查allowed_domains['']

#### request属性
1、request.url
2、request.headers
3、request.meta

-------------------------------------------------------------------

item对象到底该在何处创建？
1、一级页面: 都可以，建议在for循环外
2、大于二级页面: for循环内

-------------------------------------------------------------------
scrapy shell的使用

$基本使用
#scrapy shell URL地址
1、request.url        : 请求URL地址
2、request.headers    : 请求头(字典)
3、request.meta       : item数据传递，定义代理(字典)

4、response.text      : 字符串
5、response.body      : bytes
6、response.xpath('') 

-------------------------------------------------------------------

#scrapy.Request()参数  -> 入队列
1、url
2、callback
3、headers
4、meta : 传递数据，定义代理
5、dont_filter : 是否忽略域组限制
   默认False，检查allowed_domains['']

eg: yield scrapy.Request(url=url,dont_filter=True)

-------------------------------------------------------------------

设置中间件(随机User-Agent)

少量User-Agent切换

#方法一
#settings.py
USER-AGENT = ''
DEFAULT_REQUEST_HEADERS = {}

#方法二
#spider
yield scrapy.Request(url,callback=函数名,headers={})

-------------------------------------------------------------------

大量User-Agent切换(中间件)
#middlewares.py设置中间件
1、获取User-Agent
	# 方法1: 新建useragents.py，存放大量User-Agent，random模块随机切换  -> headers = {'User-Agent': random.choice(ua_list)}
	# 方法2: 安装fake_useragent模块(sudo pip3 install fake_useragent)
​		from fake_useragent import UserAgent
​		ua_obj = UserAgent()
​		ua = ua_obj.random
2、middlewares.py新建中间件类
​	class RandomUseragentMiddleware(object):
​		def process_request(self,request,spider):
​			ua = UserAgent()
​			request.headers['User-Agent'] = ua.random
3、settings.py添加此下载器中间件
​	DOWNLOADER_MIDDLERWARES = {'':优先级}

-------------------------------------------------------------------

### 添加中间件 - 随机代理IP

from .proxies import proxy_list
import random
class MiddleRandomProxyMiddleware:
    def process_request(self,request,spider):
        proxy = random.choice(proxy_list)
        print(proxy)
        # request.meta属性: 类型为字典
        request.meta['proxy'] = proxy

    # 捕获异常
    def process_exception(self,request,exception,spider):
        # 一旦捕获到异常，把request重新交给中间件
        return  request

-> 随机代理IP参考上述代码，独享IP不用考虑上述代码

-------------------------------------------------------------------

Fiddler抓包工具
#配置Fiddler
#添加证书信任
1、Tools - Options - HTTPS
	勾选Decrypt Https Traffic 后弹出窗口，一路确认
	
#设置只抓取浏览器的数据包
2、...from browsers only

#设置监听端口(默认为8888)
3、Tools - Options - Connections

#配置完成后重启Fiddler(重要)
4、关闭Fiddler，再打开Fiddler

-------------------------------------------------------------------

#配置浏览器代理
1、安装Proxy SwitchyOmega插件
2、浏览器右上角:SwitchyOmega->选项->新建情景模式->AID1904(名字)->创建
	输入  : HTTP:// 127.0.0.1 8888
	点击  : 应用选项
3、点击右上角SwitchyOmega可切换代理

-------------------------------------------------------------------

#Fiddler常用菜单 
1、Inspector : 查看数据包详细内容
	整体分为请求和响应两部分
2、常用菜单
	Headers: 请求头信息
	webForms
		#1、POST请求Form表单数据: <body>
		#2、GET请求查询参数: <QueryString>
	Raw:将整个请求显示为纯文本
	
	
-------------------------------------------------------------------

分布式爬虫
分布式爬虫介绍

*原理
多台主机共享1个爬取队列

*实现
重写scrapy调度器(scrapy_redis模块)

*为什么使用redis
1、Redis基于内存，速度快;
2、Redis非关系型数据库，Redis中集合，存储每个request的指纹;
3、scrapy_redis安装
	sudo  pip3 install scrapy_redis

-------------------------------------------------------------------

scrapy_redis详解
* GitHub地址
* settings.py说明
#重新指定调度器:启用Redis调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#重新指定去重机制:确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#不清除Redis队列:暂停/恢复/断电续爬
SCHEDULER_PERSIST = True  # True表示不清除

#优先级队列(默认)
SCHEDULER_QUEUE_CLASS='scrapy_redis.queue.PriorityQueue'

#可选用的其他队列
#先进先出队列
SCHEDULER_QUEUE_CLASS= 'scrapy_redis.queue.FifoQueue'

#后进先出队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

#redis管道
ITEM_PIPELINES ={
	'scrapy_redis.pipelines.RedisPipeline':300
}

#指定连接到redis时使用的端口和地址
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

-------------------------------------------------------------------

1、正常项目数据抓取(非分布式)
2、改写为分布式(同时存入redis)
	1、settings.py
		#使用scrapy_redis的调度器
		SCHEDULER = "scrapy_redis.scheduler.Scheduler"
		
		#使用scrapy_redis的去重机制
		DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"
		
		#是否清除请求指纹,True:不清除  |   False:清除
		SCHEDULER_PERSIST = True
		
		#在ITEM_PIPELINES中添加redis管道
		'scrapy_redis.pipelines.RedisPipeline':200
		
		#定义redis主机地址和端口号
		REDIS_HOST = '111.111.111.111'
		REDIS_PORT = 6379

-------------------------------------------------------------------

改写为分布式(同时存入mysql)
#修改管道
ITEM_PIPELINES = {
	'Tencent.pipelines.TencentPipeline':300,
	# 'scrapy_redis.pipelines.RedisPipeline':200,
	'Tencent.pipelines.TencentMysqlPipeline':200
}

-------------------------------------------------------------------

清除redis数据库 -> flushdb

代码拷贝一份到分布式中其他机器，两台或多台机器同时执行此代码

-------------------------------------------------------------------
# 远程连接MySQL设置

1、配置文件 - 允许远程连接
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

### bind-address = 127.0.0.1  -- 把此行注释

2、添加授权用户 - mysql -uroot -proot
mysql> grant all privileges on *.* to '用户名'@'%' identified by '密码' with grant option;
mysql> flush privileges;

3、重启MySQL服务
sudo /etc/init.d/mysql restart

-------------------------------------------------------------------

腾讯招聘分布式改写 - 方法二
使用redis_key改写

#第一步:settings.py和第一种写法一致
settings.py和上面分布式代码一致

#第二步:爬虫文件 - tencent.py修改
from scrapy_redis.spiders import RedisSpider

class TencentSpider(RedisSpider):
	#1.去掉start_urls
	#2.定义redis_key
	redis_key = 'tencent:spider'
	def parse(self,response):
		pass
		
#第三步:把代码复制到所有的爬虫服务器，并启动项目
#第四步:到redis命令行，执行LPUSH命令压入第一个要爬取的URL地址

分布式总结: -> 多台主机共享一个爬取队列
如何实现? -> 通过重写scrapy调度器

-------------------------------------------------------------------

scrapy - post请求

### 方法 + 参数
scrapy.FormRequest(
	url=posturl,
	formdata=formdata,
	callback=self.parse
)

# 有道翻译案例实现
1、创建项目+爬虫文件
scrapy startproject Youdao
cd Youdao
scrapy genspider youdao fanyi.youdao.com

2、items.py
result = scrapy.Field()

3、youdao.py

温馨提示：写代码先写结构，具体的实现可以之后再补

-------------------------------------------------------------------

scrapy添加cookie的三种方式
#1、修改 settings.py文件
1、COOKIE_ENABLED = False 取消注释
2、DEFAULT_REQUEST_HEADERS = {}  添加Cookie

#2、DownloadMiddleware
COOKIES_ENABLED = True
def process_request(self,request,spider):
	request.cookies={}
	
#3、爬虫文件
COOKIES_ENABLED = True
def start_requests(self):
	yield scrapy.FormRequest(url=url,cookies ={},callback=xxx)
	
------------------------------------------------------------------

机器视觉与tesseract

作用——> 处理图形验证码

三个重要概念

OCR
#定义 -> OCR: 光学字符识别(Optical character Recognition)
#原理 -> 通过扫描等光学输入方式将各种票据、报刊、书籍、文稿及其它印刷品的文字转化为图像信息，再利用文字识别技术将图像信息转化为电子文本

tesseract-ocr
OCR的一个底层识别库(不是模块，不能导入)
# Google维护的开源OCR识别库

pytesseract
Python模块，可调用底层识别库
# 对tesseract-ocr做的一层Python API封装

Ubuntu安装tesseract-ocr
sudo apt-get install tesseract-ocr
	
搜索'tessdata'
sudo find / -name 'tessdata'

进入管理员模式
sudo -i
退出管理员模式
exit

安装pytesseract
安装-> sudo pip3 install pytesseract


#爬取网站思路(验证码)
1、获取验证码图片
2、使用PIL库打开图片
3、使用pytesseract将图片中验证码识别并转化为字符串
4、将字符串发送到验证码框中或者某个URL地址

------------------------------------------------------------------

在线打码平台

为什么使用在线打码平台?
tesseract-ocr识别率很低，文字变形、干扰，导致无法识别验证码

云打码平台使用步骤
1、下载并查看接口文档
2、调整接口文档，调整代码并接入程序测试
3、真正接入程序，在线识别后获取结果并使用


------------------------------------------------------------------

md5加密步骤:
1、导入md5模块 -> from hashlib import md5
2、创建md5对象 -> s = md5()
3、创建需要加密的字符串对象 -> string = 'fanyideskweb'
4、将字符串对象编码后，在md5对象中进行更新 -> s.update(string.encode())
5、最后通过md5对象，生成加密密文  -> sign = s.hexdigest()

------------------------------------------------------------------

Fiddler抓包工具
* 配置Fiddler

### 添加证书信任

1、Tools - Options - HTTPS
	勾选 Decrypt Https Traffic 后弹出窗口，一路确认
	

### 设置只抓取浏览器的数据包
2、...from browsers only

### 设置监听端口(默认为8888)
3、Tools - Options - Connections

### 配置完成后重启Fiddler(重要)
4、关闭Fiddler，再打开Fiddler

* 配置浏览器代理
1、安装Proxy SwitchOmega插件
2、浏览器右上角:SwitchOmega -> 选项 -> 新建情景模式 -> AID1901(名字) -> 创建
	输入 : HTTP:// 127.0.0.1 8888
	点击 : 应用选项
3、点击右上角SwitchyOmega可切换代理
------------------------------------------------------------------
* Fiddler常用菜单
	1、Inspector : 查看数据包详细内容
	整体分为请求和响应两部分

2、常用菜单
	Headers : 请求头信息
	WebForms : POST请求Form表单数据 : <body>
	GET请求查询参数 : <QueryString>
	Raw
	将整个请求显示为纯文本
	
移动端app数据抓取
方法1 - 手机 + Fiddler
	设置方法见文件夹 - 移动端抓包配置
	
方法2 - F12浏览器工具
	有道翻译手机版破解案例
	

------------------------------------------------------------------

爬虫总结

常见反爬策略
1、Headers : 最基本的反爬手段，一般被关注的变量是UserAgent和Referer，可以考虑使用浏览器;
2、UA : 建立User-Agent池，每次访问页面随机切换;
3、拉黑高频访问IP:数据量大用代理IP池伪装成多个访问者，也可控制爬取速度;
4、Cookies : 建立有效的cookie池，每次访问随机切换 ;
5、验证码 : 
	验证码数量较少可人工填写
	图形验证码可使用tesseract识别
	其他情况只能在线打码、人工打码和训练机器学习模型
6、动态生成
	一般由js动态生成的数据都是向特定的地址发get请求得到的，返回的一般是json
7、签名及js加密
	一般为本地js加密 ，查找本地js文件、分析 ，或者使用execjs模块执行js代码
8、js调整页面结构
9、js在响应中指向新的地址

分布式爬虫的原理 -> 多台主机共享一个爬取队列

-----------------------------------------------------------------------------------------------------------------------

Python学习之cookies及session用法
	当想利用Python在网页上发表评论时，需要帐号密码登录信息，这个时候用requests.get请求的话，帐号和密码 会全部显示在网址上，非常不科学！
	这个时候需要用post请求，可以这样理解，get是明文显示，post是非明文显示。
	

	通常，get请求会应用于获取网页数据，比如我们之前学习的requests.get()。
	post请求则应用于向网页提交数据，比如提交表单类型数据(像帐号密码就是网页表单数据)。
	在post请求里，我们使用data来传递参数，其用法和params非常相像。
	
	当用到post请求时，需要了解两个参数，cookies和session。
	
	1、cookies及其用法
		当登录一个网站，登录页面会有一个可勾选的选项"记住我"，如果你勾选了，以后你再打开这个网站就会自动登录，这就是cookie在起作用。
		我们想要发表评论，首先得登录，其次得提取和调用登录的cookies，然后还需要评论的参数，才能发起评论的请求。
			———— 提取cookies方法: 调用requests对象的cookies属性获得登录的cookies，并赋值给变量cookies，最后带着 cookies去请求发表评论。
		   eg:	login_in = requests.post(url,headers=headers,data=data)
				# 用requests.post发起请求，放入参数:请求登录的网址、请求头和登录参数，然后赋值给login_in;
				cookies = login_in.cookies
				# 提取cookies的方法: 调用requests对象(login_in)的cookies属性获得登录的cookies，并复制给变量cookies
				
	2、session及其用法
		session是会话过程中，服务器用来记录特定用户会话的信息。session和cookies关系密切————cookies中存储着session的编码信息，session中又存储了cookies的信息。

python中cookie和session的区别:
区别:
1、cookie数据存储在客户浏览器上，session在服务器上;
2、cookie不安全，session较安全; -> 他人可以分析保管在当地的cookie，欺骗cookie，考虑到安全应该使用session;
3、访问增加选cookie; -> session在 一定时间内保存在服务器上。访问增加时，考虑到服务器的性能减轻，必须使用cookie;
4、cookie保存不超过4k; -> 单个cookie保存的数据不得超过4k。许多浏览器限制了一个网站 最多保存20个cookie;
建议: 将登录信息等重要信息存储在SEESION的其他信息中，可以存储在cookie中。

session的一种用法思路:
1、实例化 session对象
self.session = requests.session()

2、先post，把cookie保存在session对象中 - 会话保持
self.session.post(url=self.post_url,data=data)

3、再get，正常抓取数据
html = self.session.get(url=self.get_url).text
		
-----------------------------------------------------------------------------------------------------------------------

requests.session()发送请求和使用requests直接发送请求的区别:
一、Session
在requests里，session对象是一个非常常用的对象，这个对象代表一次用户对会话:从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开;
会话能够让我们在跨请求的时候保持某些参数，比如在同一个session实例发出的所有请求之间保持cookie信息。
1、创建session对象
session = requests.session() -> 得到session对象后，就可以调用该对象中的方法来发送请求了;
response1 = session.get(url,params,headers)
response2 = session.post(url,data,json,headers)
通过session来发送get、post、delete、put等请求并获取响应;

二、requests
requests是Python的一个第三方库，主要用于发送网络请求，比如get、post等请求已达到获取网络响应的目的

import requests
response1 = requests.get(url,params,headers,cookies)
response2 = requests.post(url,data,json,headers,cookies)
### put、delete等请求方法类似

三、session对象和requests两种方法发送的请求的区别:
1、场景
	->登录某商城
	->查询我的订单数据 
	
2、业务代码分析
	->首先这里涉及到两个接口，一个"登录接口",另外一个是"查询订单"接口。
	->常规操作是我们调用登录接口来获取响应的cookie信息 。
	->然后拿这个cookie信息作为下一次请求的参数(cookie带有当前登录人信息)来请求查询订单接口。
	
常规代码如下:
import requests
#登录接口
response1 = requests.get(url_login,params,headers)
#获取cookie信息
cookies = response1.cookies
#得到cookies是一个字典类型
cookie = cookies.get('cookies的key')
#请求查询接口 
response2 = requests.get(search_url,params,headers,cookies = cookie)
#查看响应的结果
response2.json()

使用session代码如下:
import requests

#获取session对象
session = requests.session()
#登录 接口
response1 = session.get(url_login,params,headers)
#请求 查询接口
response2 = session.get(search_url,params,headers)
#查看响应的结果 
response2.json()

区别:
	1、通过代码对比可以发现使用session对象效果会更好，不用每次都把cookie信息放到请求内容中了;
	2、session对象能够自动获取到cookie，并且可以在下次的请求中自动带上所得的cookie信息，不用人为地去填写;

-----------------------------------------------------------------------------------------------------------------------

云打码，截取验证码图片，并实现验证码信息获取，步骤:
1、定位验证码图片节点 - x y坐标(左上角)
	location = self.browser.find_element(By.XPATH,xpath_bds).location
	
2、获取宽度和高度 
	size = self.browser.find_element(By.XPATH,xpath_bds).size
	
3、左上角x y 坐标
    left = location['x']
    top = location['y']
    
4、右下角x y 坐标
    right = left + size['width']
    bottom = top + size['height']
    
5、截取验证码图片(crop((元组:四个参数))) : 对图片进行剪切
	self.browser.get(self.url)
    self.browser.save_screenshot('index.png')

    img = Image.open('index.png').crop((left,top,right,bottom))
    img.save('yzm.png')

6、在线打码
    balance = self.yundama.get_balance()
    print('打码余额:',balance)

    result = self.yundama.get_code_result('yzm.png')
    print(result)

-----------------------------------------------------------------------------------------------------------------------

字典数据类型自带的update()方法，可以用来快速更新字典的数据！(重要)

-----------------------------------------------------------------------------------------------------------------------

Linux命令:
netstat -tulpn  -> 显示当前操作系统中运行的进程的PID/Program name

-----------------------------------------------------------------------------------------------------------------------

tips:

1、有一个官方网站，可以将cURL(bash),直接转换成requests.get()的相关代码 -> 猿人学

2、在爬取需要进行loginID和password登录的网页时，可以通过尝试输入loginID和password，通过F12开发者工具，来查看登录请求url的请求方式、参数加密方式、请求头数据等等;

3、如何寻找登录网页时的参数加密信息？-> 通过在JS文件加入断点，在点击登录按钮时，看断点是否被使用，如果程序到了断点处停住了，证明该段JS代码在登录网页时被执行了。

4、如果发现，response返回200，但是response.text或者response.content返回空。这个时候，需要添加完善headers头部信息。

5、在使用execjs()方法进行js代码逆向的时候，如果发现有些参数需要调用，可以在响应页面中进行匹配，查看服务器是否将参数给到前端页面了。  特别地:如果发现诸如window.xxx.xxx，大多都是可以在响应页面中查到的。

6、每次F12中抓完包里面，看到有动态的参数，第一反应要先看源代码中是否有加载，第二步才是去js中找对应程序。

7、如果网站屏蔽了右键查看源代码，可以在抓包工具里点击网络包后，进行response查看。



#### 关于字体反爬:

1、待爬取数据的页面中，一般会伴有字体库的返回 -> 可能是跟着网页返回的，也可能是返回一个链接URL；

​	  可以在网页中搜索: ttf,woff,woff2

2、需要导入字体库from fontTools.ttLib import TTFont；

3、注意最好保存一份html网页信息文件到本地，防止网络服务器封锁IP；
4、字体库文件.ttf文件的内容，一般保存在html网页信息中，且是编码过后的信息，需要在Python脚本中重新解码，并保存为.ttf文件到本地；

5、base64的解码指令为 :base64.b64decode(ttf) -> 得到二进制ttf字体库解码信息，保存到本地.ttf文件中；

6、调用TTFont('.ttf文件保存路径')，实例化字体库对象；

7、BestCmap = font.getBestCmap() -> unicode与图形编号的对应关系

​	  GlyphMap = font.getReverseGlyphMap() -> 具体的值和图形编号的关系

8、最后开始根据map中的对应关系，得到反爬价格对应的真实价格数据；

----------------------------------------------------------------------------------------------------------------------------------------------------------

如果是.woff2的字体库文件 ，在使用字体库文件时，需要进行指纹构建。

```python
from fontTools.ttLib import TTFont
font = TTFont('gz.woff2')
print(font.getGlyphNames())
names = font.getGlyphNames()[3:-2]
names.remove('uniE4D9')
for name in names:
    # 获取glyf节TTGlyph字体x、y坐标信息
    print(name)
    aa = font['glyf'][name].coordinates
    print(aa)
    bb = font['glyf'][name].flags  # flags是指纹
    print(bb)
    print()
```

-----

### 使用mitmproxy的注意事项：

1、要加载mitmproxy的证书：

linux系统环境下,pip install mitmproxy后，在终端运行mitmdump后，在浏览器网页输入mitm.it，下载证书；

mitm.it上有教程，指导证书的保存位置。

证书还需要加载到Chrome浏览器中(重要)。

2、要打开本地设备的人工代理设置。http、https都需要设置。

----

### Scrapy框架使用流程:

一、创建项目:
	创建项目的两种方式: scrapy startproject db

​										scrapy startproject inner_folder outer_folder

二、进入到项目中，创建爬虫文件:scrapy genspider db250 movie.douban.com

三、修改start_urls访问的url为:['https://movie.douban.com/top250']

四、settings.py文件设置

​	1、不遵守robots协议：

​			ROBOTSTXT_OBEY = False

​	2、设置请求头：

​			DEFAULT_REQUEST_HEADERS = {

​				这里具体内容省略，按照网站上的请求头信息进行更新即可

}

五、修改parse方法：

​	1、parse方法中的response是请求上面url返回的html内容；

​	2、使用xpath解析html中的数据内容，解析方法和lxml中的解析类似，多一个get()方法；

​	3、导入items.py文件中的DbItem类，进行实例化这个类对象，用来存储提交给管道pipelines.py数据，类似于

​			from ..items import DbItem

​			def parse(self,response):

​					dbitem = DbItem()

​					dbitem['movie_name'] = movie_name

​					dbitem['d_name'] = d_name

​					dbitem['price'] = price

​					yield dbitem

​				

​	4、tiems构造：字段名要和前面传递时的一样

​		class DbItem(scrapy.Item):

​				movie_name = scrapy.Field()

​				d_name = scrapy.Field()

​				price = scrapy.Field()



六、pipeline修改

​	1、激活管道：

​			在settings中找到如下内容，取消注释：

​					ITEM_PIPELINES = {

​							'db.pipelines.DbPipeline':300,

}

​	2、修改DbPipeline类中的三个方法 ，方法名都是固定的，文件保存的使用方式看pipelines.py文件

​			# 爬虫开始的时候执行   一般用来打开文件，链接数据库  

​			def open_spider(self,spider):

​					pass

​			 # 接收爬虫文件传递过来的数据(item是数据)，他不是一个字典，需要强转为字典(dict(item))，然后

​			def process_item(self,item,spider):

​					return item

​             # 爬虫结束的时候执行，一般用来关闭文件，关闭数据库

​			def close_spider(self,spider):

​					pass



七、启动爬虫

命令行输入： scrapy crawl douban1

八、翻页

多页抓取

进行比较多个页面的url不同之处：分别是 0 -> 25 -> 50，说明每页是25的数隔

https://movie.douban.com/top250?start=0&filter=

https://movie.douban.com/top250?start=25&filter=

https://movie.douban.com/top250?start=50&filter=



多页构造法一：直接构造其他页面的url

start_urls = [f'https://movie.douban.com/top250?start={page*25}&filter=' for page in range(3)]  # 设置3页

这里需要注意：用方法一进行url请求，由于Scrapy是一个异步的框架，所有start_urls中的url谁先加载完，则谁先保存！(重要！)



多页构造法二：重写start_requests方法

def start_requests(self):

​		for page in range(3):   # 设置3页
​				page_url = f'https://movie.douban.com/top250?start={page*25}&filter='

​				yield scrapy.Request(page_url,callback=self.parse)



多页构造法三：

self.page_num += 1

page_url = f'https://movie.douban.com/top250?start={self.page_num*25}&filter='

yield scrapy.Request(page_url)



# Scrapy框架使用注意:

1、使用scrapy框架，如果要使用自定义cookies，需要将settings.py中的enable_cookies置为True;

2、中间件的设置与开启在Settings模块中，以字典的形式表现，key为中间件模块的导入路径(同import路径)，value为一个整数，表示该中间件的权重。对于下载中间件来说，权重越小，离引擎越近；权重越大，越靠近下载器。在处理Request和Response的时候都是经过顺序依次进行。

​		下载中间件是Scrapy框架中非常灵活的部分，可以高度自由地定制框架处理请求和响应的过程，但是用起来稍有些复杂，我们来看一下中间件中的方法: process_request、process_response和process_exception三个方法。

- process_request在请求经过时被调用，它接受两个参数：request和spider，在引擎调用的时候会默认传入，分别为待处理的request对象和产生该请求的spider对象，在这个方法中可以对request对象进行加工，增加其属性或在META字典中增加字段来传递信息。这个方法允许返回request对象或返回一个IgnoreRequest异常或者无返回(即返回None)。在返回Request对象时，这个对象不会再传递给接下来的中间件，而是重新进入调度器 队列中等待引擎调度。返回异常时，该异常会作为中间件process_exception方法的参数传入，若无process_exception方法，则会交给该请求err_back绑定的方法处理。若无返回则将request对象交给下一个中间件处理。
- process_response在响应被返回经过时调用，接受3个参数，分别为request对象，response对象和spider对象。spider对象同上，response对象为下载器返回的响应，而request对象则表示产生该响应的请求，与spider中的response不同，此处的response对象中没有request属性，而是同作为参数传入。在这个方法中可以对下载器返回的响应进行处理，包括响应的过滤、校验，以及与process_request中耦合的操作，如Cookie池和代理池的操作等。该方法允许3种返回：request对象、response对象和IgnoreRequest异常。当返回request对象时同上一方法，当返回response对象时，该response会交由下一个中间件继续处理，而返回异常则直接交给该请求err_back绑定的方法处理。
- process_exception方法在下载器或process_request返回异常时被调用，接受3个参数:request对象，exception对象和spider对象，其中request对象为产生该异常的请求。它有3种返回分别为request对象、response对象和无返回。当无返回时，该异常将被后续的中间件处理；当返回request对象和response对象时，均不会再调用后续的process_exception方法，前者将会交给调度器加入队列，后者将会交由process_response处理。可以看出，中间件就是一个钩子，可以拦截并加工甚至替换请求和响应，可以按照我们的意愿来控制下载器接受和返回的对象。而由于爬虫工作的过程主要是处理各种请求和响应，所以下载中间件可以极大地控制 爬虫的运行。
- Pipelines数据管道是Scrapy中处理数据的组件。当Spider中的方法yield一个字典或scrapy.item类及其子类时，引擎会将其交给pipelines处理。Piplines和中间件非常类似，数据条目将以此通过pipeline进行处理，pipeline的权重越小，则越早被调用。一个pipieline需要实现process_item方法，接受item，spider两个参数，其中item即为所处理的数据。该方法可返回item(字典或scrapy.item类及其子类)或DropItem异常或Twisted Deferred对象。返回的item会交由下一个pipeline继续处理，而返回的是DropItem异常时，则不会再向后传递item。此外，一些费时的操作(例如插入数据库)可通过返回Deferred对象实现异步操作。
- 上述组件均可实现open_spider，close_spider和from_crawler等方法，用于在流程中的开始和结束时，以及初始化时进行自定义设置或资源初始化和回收操作等，使整个流程更"Gracefully"。
- 小结:Scrapy是一个优秀的框架，有着 友善的文档和活跃的社区。其实抛开文档，scrapy源码就是最好的文档，从阅读代码中可以收获不少scrapy使用和框架设计的技巧。爬虫是一件有意思的事情，从异步到并发，从cookie登录到JS加密，总能发现惊喜。希望大家在获取数据的同时，也能收获一份乐趣。





​			





















































​	