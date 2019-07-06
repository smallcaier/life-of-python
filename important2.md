## 重要知识点

1. 自我介绍 ( 剧本 )

   ```
   - 学习能力(不满于现状开始自学)
   	- ES/vue/linux,自学一些技术.
   	- 书籍,学习;(流畅的python/源码剖析).
   - 项目 > 职责
   - 技术正在研究(前置)
   ```

2. 你都了解哪些编程语言?

   ```
   C/java,大学学过,但基本上都还给老师.
   Python/Go语言(3天). 
   ```

3. 运算符

   ```
   value = 1 or 2 and 0 or 9 
   ```

4. 列举常用数据类型的方法

   ```
   - 字符串
   - 列表
   - 字典
   - 元组
   - 集合(交并差)
   ```

5.  is 和 == 的区别?

6. python深浅拷贝?

   ```
   针对可变类型而言,浅拷贝只是拷贝"第一层",深拷贝就是拷贝所有层级中的可变类型.
   ```

7. (1,2,3) 和 (1) 区别?

   ```
   ((1),(2),(3),)
   ```

8. def func(a=[]):pass 

9.  *args和**kwargs 的作用?

10.  pass 的作用?

11.  函数的参数传递的是什么?  值/应用.

12. 装饰器(重点)

    ```
    - 普通
    - 带参数的装饰器
    ```

    ```
    # 写装饰器
    
    def func(..):
    	pass 
    	
    @func(5)
    def index():
    	print(123)
    	
    index()
    ```

13. 常用的内置函数?

    ```
    range/print/str/.... 
    map/reduce/filter/zip
    ```

14. 生成器

    ```\
    yield 
    ```

15. py2和py3的区别?

    ```
    - 默认解释器编码
    - 字符串和字节不同
    	py2:   name=u"alex"(用unicode进行编码)			name='alex'(utf-8/gbk/ascii)   
    				unicode										str
    	py3:   name='alex'(用unicode进行编码)     	    name=b'alex'(utf-8/gbk/ascii) 
    				str											bytes
    
    ```

16. 常用的模块?

    ```
    内置
    第三方(加分)
    ```

17. 遍历一个目录下所有的文件.

    ```
    os.listdir
    os.walk
    
    import os
    
    
    result = os.walk('rbac')
    for a,b,c in result:
        for file_name in c:
            print(os.path.join(a,file_name))
    ```

18. search和match的区别?

19. 贪婪匹配?

20. 邮箱/手机号/身份证/IP

21. 面向对象的三大特性

    ```
    - 继承:drf/cbf
    - 封装:request.POST/request.method
    - 多态:鸭子模型
    ```

22. 什么是鸭子模型(多态)?

    ```
    def func(arg):
    	arg.pop(123)
    ```

23. 特殊方法

    ```
    __init__
    __new__
    __call__
    __iter__
    __next__
    __setitem__
    __getitem__
    __delitem__    reqest.session['ax'] = 123
    __enter__
    __exit__
    ```

24. 单例模式

    ```
    # 多例模式
    class Foo(object):
    	pass
    	
    obj1 = Foo()
    obj2 = Foo()
    
    # 单例模式
    class Singleton(object):
        instance = None
    
        def __init__(self):
            self.age = 19
    
        def __new__(cls, *args, **kwargs):
            if not cls.instance:
                obj = object.__new__(cls)
                cls.instance = obj
            return cls.instance
    
    # 再创建对象时,全部用的都是第一次创建的对象.
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1,obj2)
    
    # 最终版:单例模式
    import time
    import threading
    
    class Singleton(object):
        instance = None
        lock = threading.RLock()
    
        def __init__(self):
            self.age = 19
    
        def __new__(cls, *args, **kwargs):
            if cls.instance:
                return cls.instance
            with cls.lock:
                if not cls.instance:
                    obj = object.__new__(cls)
                    time.sleep(0.5)
                    cls.instance = obj
                return cls.instance
    
    def task(i):
        obj = Singleton()
        print(i,obj)
    
    for i in range(10):
        t = threading.Thread(target=task,args=(i,))
        t.start()
        
    time.sleep(100)
    
    obj = Singleton()
    conn = obj.get_conn()
    
    # 扩展:数据库连接 & 数据库连接池(DBUtils)
    ```

25. 上下文管理 (补充)

    ```
    class Context:
        def do_something(self):
            pass
        
        def __enter__(self):
            return self
    
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
    
    
    with Context() as ctx:
        ctx.do_something()
    ```

26. 两个对象如何实现相加(补充)

    ```
    class Foo:
    
        def __init__(self,num):
            self.num = num
    
        def __add__(self, other):
            return Foo(self.num + other.num)
    
    
    obj1 = Foo(1)
    obj2 = Foo(2)
    obj3 = obj1 + obj2 # obj1.__add__(obj2)
    ```

27. OSI7层模型 ?

28. TCP三次握手四次挥手 ?

    ```
    # 服务端
    server = socket.socket()
    server.bind(('127.0.0.1',8001))
    server.listen(5)
    
    conn,addr = server.accept() # 阻塞
    ....
    
    # 客户端
    client = socket.socket()
    client.connect('127.0.0.1',8001)
    
    client.send(b'xxx')
    
    ```

29. http协议

    ```
    基于TCP连接,无状态短连接(一次请求一次响应之后断开连接) + 数据发送格式
    
    
    # 服务端
    server = socket.socket()
    server.bind(('127.0.0.1',8001))
    server.listen(5)
    
    while True:
        conn,addr = server.accept() # 阻塞
        data = conn.recv(1024) # 阻塞等待用户发消息
        conn.send(b'响应内容')
        conn.close()
    
    
    # 客户端
    client = socket.socket()
    client.connect('127.0.0.1',8001) # 阻塞
    
    # client.send(b'GET /s?wd=alex Http1.1\r\nhost:xxxx;content-type:xxx\r\n\r\n') # 想服务端发送消息
    # client.send(b'POST /v2/api/?login Http1.1\r\nhost:xxxx;content-type:xxx\r\n\r\npassword=sdfsdf&loginType=2&phone=%2B8613512341234') # 想服务端发送消息
    data = client.recv(1024)
    
    client.close()
    ```

30. websocket

    ```
    基于TCP连接之后不断开,相互收发消息.(握手环节)
    可以实现由于服务端主动向客户端发送消息.
    扩展:轮询/长轮询
    
    server = socket.socket()
    server.bind(('127.0.0.1',8001))
    server.listen(5)
    
    conn,addr = server.accept() # 阻塞
    data = conn.recv(1024) # 接收到随机字符串
    # 对随机字符串进行加密:   base64(sha1(随机字符串 + magic string))
    conn.send(打包(base64(sha1(随机字符串 + magic string))))
    # 接收到 加密的(你好),然后进行解密(127/126/<=125)
    content = conn.recv(1024)
    
    # 客户端
    client = socket.socket()
    client.connect('127.0.0.1',8001)
    
    client.send(b'打包(一段随机字符串)')
    data = conn.recv(1024) # 加密后的随机字符串
    # 比对随机字符串是否正确,如果正确则可以进行连接.
    
    conn.send(加密(你好))
    ```

31. Https协议?

    ```
    443端口
    安全:
    	ssl
    	对称加密和非对称加密
    ```

32. TCP和UDP的区别?

33. 黏包?

34. 进程线程协程区别?

    ```
    进程是计算机资源分配的最小单元.
    线程是CPU调度的最小单元.(工作),一个进程中可以有多个线程.
    协程,"微"线程. 在计算机中不是真实存在,而是程序员通过代码制造出来的. (程序员控制代码进行切换执行)
    
    协程优势当存在IO等待时候,他会发挥作用. 协程 + IO切换.
    ```

35. 进程间数据共享

36. GIL锁

    ```
    python解释器锁,一个进程中同一时刻只能有一个线程被CPU调度. 
    
    计算密集型(用cpu多核):多进程
    IO密集型(不用cpu):多线程 (协程>多线程)
    ```

37. IO多路复用(盆)

    ```
    监听多个 "socket" 是否发生变化?
    
    - select,最多监听1024个 "socket"/ 轮询检测 
    - poll, 无个数限制 / 轮询检测
    - epoll,无个数限制 / 通知
    
    
    import socket
    import select
    
    server = socket.socket()
    server.bind(("",10))
    server.listen(5)
    
    x = [server,]
    while True:
        r,w,e = select.select(x,[],[],0.05)
        for item in r:
            if item == server:
                conn,addr = item.accept()
                x.append(conn)
            else:
                data = item.recv(1024)
                print(data)
    ```

38. 数据库引擎以及区别?

39. char和varchar的区别?

40. char(50) 中的50是什么意思?

41. 连表查询

    ```
    left join
    inner join
    right join 
    ```

42. 聚合查询条件应该放在having中.

43. 数据库查询的练习题

    ```
    ...
    ```

44. 联合索引想要命中索引遵循: 最左前缀的原则.

    ```
    id   name   password   email 
    
    联合索引(name   password   email )
    - name,password
    - name,emial
    - password,email 
    ```

45. 可能无法命中索引的情况

    ```
    - like '%xx'
        select * from tb1 where name like '%cn';
    - 使用函数
        select * from tb1 where reverse(name) = 'wupeiqi';
    - or
        select * from tb1 where nid = 1 or email = 'seven@live.com';
        特别的：当or条件中有未建立索引的列才失效，以下会走索引
                select * from tb1 where nid = 1 or name = 'seven';
                select * from tb1 where nid = 1 or email = 'seven@live.com' and name = 'alex'
    - 类型不一致
        如果列是字符串类型，传入条件是必须用引号引起来，不然...
        select * from tb1 where name = 999;
    - !=
        select * from tb1 where name != 'alex'
        特别的：如果是主键，则还是会走索引
            select * from tb1 where nid != 123
    - >
        select * from tb1 where name > 'alex'
        特别的：如果是主键或索引是整数类型，则还是会走索引
            select * from tb1 where nid > 123
            select * from tb1 where num > 123
    - order by
        select email from tb1 order by name desc;
        当根据索引排序时候，选择的映射如果不是索引，则不走索引
        特别的：如果对主键排序，则还是走索引：
            select * from tb1 order by nid desc;
     
    - 组合索引最左前缀
        如果组合索引为：(name,email)
        name and email       -- 使用索引
        name                 -- 使用索引
        email                -- 不使用索引
    ```

46. 数据库优化方案

    ```
    读写分离
    分库分表
    	- 水平分表
    	- 垂直分表
    缓存
    建索引
    少用select * 
    少连表(放在内存不要新建表,例如:django中的chices)
    固定长度的列往前放.例如:id  age  name  email 
    
    注意:命中索引(可以通过执行计划来进行检查)
    https://www.cnblogs.com/wupeiqi/articles/5716963.html
    ```

47. SQL注入

48. 设计题( 25/27题 )

    ```
    单表
    一对多
    多对多
    ```

    





## 今日作业

1. 自我介绍
2. 面向2个题目
3. 网络和并发答案
4. 项目问答



















