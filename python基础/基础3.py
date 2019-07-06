"""
time
    time.time()  时间戳. 数字. 从1970-01-01 00:00:00
    time.strftime("%Y-%m-%d %H:%M:%S", struct_time) 格式化时间
    time.strptime(str, "%Y-%m-%d %H:%M:%S")
os
    文件操作
    os.mkdir()
    os.makedirs()
    os.rmdir()
    os.removedirs()
    os.rename()
    os.remove()
    os.listdir() 列出文件夹内所有的文件名

    os.path.join() 拼接路径
    os.path.


random
    随机数
    random.random()  0-1
    random.randint()
re
    正则表达式
    元字符
        .
        \w  数字, 字母, 下划线
        \d  数字
        \s  空白
        ^ 开始
        $ 结束
        [abc] 字符组
        [^abc] 非xxx
        \W
        \D
        \S
        ( ) 分组
        | 或者

    量词:
        *  零次或多次
        +  一次或多次
        ?  零次或1次
        {n} n次
        {n,} n次或多次
        {n,m}  n次到m次

    贪婪匹配
        *, +, ?

    惰性匹配
        .*?x  找到最近的x

    re模块
    findall
    finditer
    search  找到一个就结束
    match   找到一个就结束, 从头开始查找  ^

    group(name)
    分组: (?P<name>正则)



json
    dumps
    loads
pickle
    dumps
    loads
    dump
    load
sys
    sys.path
    sys.argv
traceback

logging
hashlib

    import 模块
    from xxx import xxxx

    包:
        __init__.py 文件

        import xxx.py
        import 包(文件夹)

        相对导入和绝对导入

collections
    Iterator
    Iterable
    deque
    Counter

functools


"""
# import os

# ret = os.popen("dir")
# print(ret.read())

# import sys

# ['D:/sylar/串讲/第三部分.py']
# 命令行参数
# print("argv=", sys.argv)
# import traceback
# try:
#     print("哈哈")
#     print(1/0)
#     print("呵呵")
# except Exception as e:
#     print("报错了")
#     print(traceback.format_exc())

# import logging
# import traceback
#
# logging.basicConfig(filename='x1.txt',
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=40)
#
# # logging.critical("1") # 50
# # logging.error("2") # 40
# # logging.warn("3") # 30
# # logging.warning("3") # 30
# # logging.info("3") # 20
# # logging.debug("3") # 10
# # logging.log(9999,"fdsafa")
#
#
# def login():
#     try:
#         print("登录验证")
#         print(1/0)
#     except Exception as e:
#        logging.error(traceback.format_exc())
#
# login()
#
#
# import hashlib
#
# obj = hashlib.md5(b'kfljalskjfklasdjfkladsjfkladsjfkldasjflkadsjfld')
# obj.update("123".encode("utf-8"))
#
# code = obj.hexdigest()
# print(code)

from collections import Counter, Iterator, Iterable, deque

# c = Counter("周杰伦喜欢杰伦")
# print(c)
#
# isinstance(xxx, Iterable)
# isinstance(xxx, Iterator)

# import queue
# q = queue.Queue()
# q.put("alex")
# q.put("wusir")
# q.put("太白")
#
# print(q.get())
# print(q.get())
# print(q.get())
# 舒服了 不要钱 你 折磨 哈哈 呵呵 吼吼
# qq = deque()
# qq.append("哈哈")
# qq.append("呵呵")
# qq.append("吼吼")
#
# qq.appendleft("折磨")
# qq.appendleft("你")
# qq.appendleft("不要钱")
# qq.appendleft("舒服了")
#
# print(qq.pop())
# print(qq.pop())
# print(qq.pop())
# print(qq.pop())
# print(qq.popleft())
# print(qq.popleft())
# print(qq.popleft())

# lst = []
# lst.append("张开")
# lst.append("小波波")
# lst.append("MJJ")
#
# print(lst.pop())


from functools import wraps, reduce, partial

# def wrapper(fn):
#     @wraps(fn) # 还原被装饰的函数的相关信息
#     def inner(*args, **kwargs):
#         """
#         我是inner
#         :param args:
#         :param kwargs:
#         :return:
#         """
#
#         ret = fn(*args, **kwargs)
#
#         return ret
#
#     return inner
#
# @wrapper
# def target():
#     """我是target"""
#     pass
#
# print(target.__name__)
# print(target.__doc__)


# r = reduce(lambda x, y: x + y , map(lambda x: x *2, [1,2,3,4,5]))
# print(r)

# # 偏函数
# def func(a, b):
#     print(a, b)
#
# fnn = partial(func, b=2)
#
# fnn(3)
# fnn(4)
# fnn(5)

# import re
#
# it = re.finditer(r'(?P<age>\d+)', "alex18岁吃了15个药丸, 死了.享年36岁")
# for i in it:
#     print(123)
#     print(i.group("age"))
