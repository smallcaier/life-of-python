"""
python2
python3

python解释器
CPython，IPython

解释型编程语言

python源代码 -> pyc字节码  ->  机器码

# 文件存储底层就是字节.
# 网络

print(*args, sep="", end="\n") # 打印

print("周润发", "周杰伦", sep="*", end="____")
print("哈哈哈")

input()  -> str

基本数据类型
    int
        整数
    str
        字符串 -> string -> varchar
        索引和切片
        s[start:end:step]
            start: 起始
            end:结束
            step: 步长

            常用操作:
                strip()  默认去掉空白
                split() 字符串切割
                join()  拼接
                replace()  替换
                upper()  转换成大写
                lower()  小写
                startswith()  判断以xxx开头
                endswith() xxxx结尾
                find()  查找   -1
                index() 查找   报错
                isdigit() 判断是否是数字
                isUpper() xxxxxx大写

            迭代
            for c in s:
                遍历字符串中的每一个字符

    bool
        用来条件判断
        and  并且, 两端同时为真, 结果才能是真  -> 与运算
        or   或者, 两端有一个镇. 结果就是真  -> 或运算
        not  非, 非真既假, 非假既真.  - >  非运算

    list
        索引切片
        增
            append() 追加
            insert() 插入
            extend() 迭代添加
        删
            pop(index)
            remove(el)
            del

        改
            lst[index] = 值
        查
            lst[index]
        for item in lst:

        range(10)
        for i in range(len(lst)):
            lst[i]

        lst = [[],[],[]]

        append
        for

        1. 数据从哪儿来
        2. 数据往哪儿去

    tuple
        只读列表, 元组

    dict
        特点 :
            key:value存储数据的
            key: 必须是可哈希的  -> 不可变

        没有索引切片: 没有顺序

        增
            dic[key] = value
            dic.setdefault() 最后查询

        删
            pop(key)
        改
            dic[key]= value
        查
            dic.get(key)
            dic[key]

            keys()  => 所有key
            items()  => 所有的key, value
            values()  => 所有的value

            for k in dict:

            for k, v in dict.items():


            fromkeys(["abc","def"], ["cpu","内存"])

    set
        去重复. 内容必须可哈希

    frozenset
         不可变的set集合
    float
        浮点数

    while循环
    while 条件 :
        循环体

    break: 跳出本层循环
    continue: 停止当前本次循环, 继续执行下一次循环

    if判断

    文件操作
        open(路径, mode, encoding="utf-8")
        mode: r, w, a, rb, wb
        f.readline()
        for line in f:

        f.seek(0)
        f.seek(0,2)

    深浅拷贝
        1. = 赋值操作
        2. 浅拷贝, 只拷贝第一层内容 .
        3. 深拷贝, 全部都拷贝


    is和 ==
        is :比较内存地址
        == : 比较的值

    格式化输出
    %s   字符串
    %d   整数
    %f   小数

    f'{变量}'

"""
import copy

lst1 = ["鲲鹏", "班长", "靠窗", "干他?", [1,2,3]]
# lst2 = lst1 # 没有创建新对象
# lst2 = lst1.copy() # 创建了新对象, 两个变量指向的是不同的两个内存地址
lst2 = copy.deepcopy(lst1) # 深拷贝.
lst1.append("哈哈哈")
print(lst1)
print(lst2)

print(id(lst1[4]), id(lst2[4]))

print(id(lst1), id(lst2))



