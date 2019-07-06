"""
万事万物皆为对象.
对象是通过类来创建的
类:归类.
对象:是通过类来创建的一个具体的实例

class 类名(父类1, 父类2, 父类3...):
    pass

class Person:
    def __init__(self, name, age):
        '''初始化操作'''
        self.name = name
        self.age = age

    def chi(self):
        pass

    def he(self):
        pass

p = Person("alex", 28)

print(p.name)
print(p.age)

p.name = "wusir"
p.chi();

chi();


封装:
    1. 对属性的封装
        对象. 属性 = 值
    2. 对功能的封装
        在类中写入一些方法

发送消息
    发送消息到短信
    发送消息到邮件
    发送消息到app推送

class MsgUtil:
    @staticmethod
    def chat(msg):
        pass
    @staticmethod
    def email(msg):
        pass
    @staticmethod
    def app(msg):
        pass

继承:
    对代码可以进行扩展
    可以通过一些手段对子类进行约束

    python支持多继承. 采用MRO, C3算法来查找方法
    先找亲爹, 后找干爹

    class F1:
        def m(self):
            pass

    class F2(F1):
        def m(self):
            pass

    class F3(F2):
        pass

    f = F3()
    f.m()


多态
    鸭子模型
    会嘎嘎叫的就是好鸭子

    def func(d):
        d.gagajiao()

    class Duck:
        def gagajiao(self):
            pass
    class Monkey:
        def gagajiao(self):
            pass


    #  动态数据类型绑定
    a = 10
    a = "哈哈哈"

成员:
    1. 变量
        类变量
        实例变量 -> 对象
    2. 方法
        类方法  @classmethod
        实例方法  给对象使用的. self
        静态方法 @staticmethod
    3. 属性
        @property
        把一个方法变成一个属性
        @属性.setter

    4. 私有
        __开头

    5. 特殊成员
        __xxx__
        __init__
        __new__
        __call__
        __getitem__ lst[i]
        __setitem__ lst[i] = 123
        __eq__


    依赖关系
        方法的参数传递一个对象
        class Person:
            def play(self, computer):
                pass
            def chi(self):
                pass


    关联关系(组合, 聚合)
    继承关系(实现关系)

    约束(父类对子类)
        1. 抛出异常
            raise NotImplementedError
        2. 写抽象类
            from abc import ABCMeta, abstractmethod
            class cls(metaclass = ABCMeta):
                @abstractmethod
                def m(self): pass


    反射
        hasattr()
        getattr()
        setattr()
        delattr()

    super()调用父类中重名的方法

"""

# class Person():
#
#     def __init__(self, age):
#         self.age = age
#
#     @property
#     def abc(self):
#         return self.age
#
#     @abc.setter
#     def abc(self, age):
#         self.age = age
#
#
# p = Person(188)
# print(p.abc)
#
# p.abc = 18
#
# print(p.age)

class Person:

    def __init__(self, age):
        self.age = age

    #  ==
    def __eq__(self, other):
        print("哈哈哈")
        return True
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass

    def __add__(self, other):
        pass
    # with
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __len__(self):
        pass

    __hash__ = None


p = Person(18)
print(p == 123)


