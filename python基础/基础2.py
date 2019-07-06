"""
函数:
    定义: 对功能或者动作的封装
    f(x) = x + 1

    语法:
        def 函数名(形参):
            函数体(return)

        函数名(实参)

        形参:  函数声明的时候的变量
            分类:
                1. 位置参数
                2. 默认值参数
                3. 动态传参
                    *args 位置参数的动态  接收到的是元组
                    **kwargs 关键字参数的动态  接收到的是字典

                    在实参: *和**表示的打散

                顺序:
                    位置, *args, 默认值, **kwargs

        实参:  在函数调用的时候给函数传递的信息
                1. 位置
                2. 关键字
                3. 混合(先位置, 后关键字)

        返回值:
            1. 如果函数没写return, 没有返回值. 默认返回None
            2. 只写return. 返回None. 可以中断函数的执行
            3. return 值. 只有一个返回值
            4. return 值1, 值2, 值3..... 多个返回值. 返回的是元组


        名称空间
            1. 内置
            2. 全局
            3. 局部
        作用域
            全局  py文件
            局部  函数内部, 方法内部, 类内部. 对象

            global  在局部引入全局变量. 可以在局部创建全局变量
            nonlocal 在局部,  内层函数对外层函数的变量的引入

            globals() 查看全局作用域
            locals()  查看当前作用域

        函数嵌套
        闭包
            内层函数对外层函数的变量的调用

            def outer():
                content = "123"
                def inner():
                    return content
                return inner

            fn = outer()
            fn()
            fn()

        装饰器
            通用装饰器写法
            def wrapper(fn):
                def inner(*args, **kwargs): # 接收到的数据原封不动的传递出去
                    '''之前'''
                    ret = fn(*args, **kwargs)
                    '''之后'''
                    return ret
                return inner

            @wrapper  => target = wrapper(target)
            def target():
                pass


            带参数的装饰器
            def log(fileName):
                def wrapper(fn):
                    def inner(*args, **kwargs):
                        ret = fn(*args, **kwargs)
                        #  需要获取到日志写入的文件名
                        print("记录日志%s" % fileName)
                        return ret
                    return inner
                return wrapper

            # 执行流程:先执行后面的函数调用. 函数的返回值和前面的@组合成原来的装饰器
            @log("login.txt")
            def login():
                print("登录")

            @log("reg.txt")
            def reg():
                print("注册")

            @log("index.txt")
            def index():
                print("首页")

            login()
            reg()
            index()

            同一个函数被多个装饰器装饰
            @warpper1
            @warpper2
            @warpper3
            def target():
                pass

            target()

        迭代器
            迭代器       __iter__ __next__
            可迭代对象:  __iter__

            特点:
                1. 惰性
                2. 只能向前
                3. 生内存

            for循环机制
            lst = ["哈哈", "不开心", "很不开心"]
            it = lst.__iter__()
            while True:
                try:
                    print(it.__next__())
                except StopIteration :
                    print("没数据了")
                    break


        生成器 -> 考点
            本质就是迭代器
            1. 通过生成器函数
                def func():
                    yield

                gen = func() 生成器. 此时这个函数并没有被执行
                __next__() 让生成器执行到下一个yield


                def func():
                    print(22222)
                    yield 1

                gen = func()

                gen.__next__()
                gen.__next__() # 生成器如果没有数据了. 报错StopIteration

                send() 可以给上一个yield位置传值


                坑: 惰性机制

            2. 生成器表达式
                列表推导式
                [结果 for if]
                {key:value for if}
                {key for if}

                (结果 for if)  创建生成器


        内置函数
        bin()  二进制
        hex()  十六进制
        oct()  八进制
        next()
        iter()  获取迭代器  __iter__
        format() 格式化
        filter()  筛选
        map() 映射
        sorted() 排序
        zip()  拉链
        id()  内存地址
        dir()  内部结构
        str()  字符串
        repr()  字符串
        enumerate() 枚举
        range() 数数
        chr()
        ord()
        hash() 获取到哈希值
        callable() 判断xxx是否是可调用
        compile() 预编译
        exec() 执行一段字符串代码
        eval() 执行一段字符串代码. 带有返回值

        sorted() 排序
        map() 映射
        filter() 筛选过滤


        递归
            自己调用自己
            递归深度: 1000

"""

# def add(a, b):
#     return a + b
#
# def gen(): # 0,1,2,3
#     for i in range(4):
#         yield i
#
# g = gen()
#
# for n in [2,10]:
#     g = (add(n, i) for i in g)
#
# print(list(g))


# print(format(53, "018b"))
#
# print(str("他说\n哈哈"))
# print(repr("他说\n哈哈"))
# print(r'他说\n 哈哈')



# lst = ["alex", "wusir", "太白", "吴超", "于超", "孙建超", "golang"]
# s = sorted(lst, key=lambda s: len(s))
#
# print(s)
# print(lst)


# lst = ["alex", "wusir", "太白", "吴超", "于超", "孙建超", "golang"]
# m = map(lambda s: s+"_sb" , lst)
# print(list(m))

lst = ["alex", "wusir", "太白", "吴超", "于超", "孙建超", "golang"]
f = filter(lambda x: len(x) > 3, lst)
print(list(f))
