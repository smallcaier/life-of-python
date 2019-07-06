# MySQL数据库

## 一 安装配置

参考:<https://www.cnblogs.com/clschao/articles/9907529.html#part_3>

### 找mysql所有配置:

```mysql
show variables like "%";
```



### mysql中查看用户信息:

```mysql
use mysql
select user,host,authentication_string from user;   5.6  password
```



### 修改密码

```mysql
方式1:
	格式：mysql> set password for 用户名@localhost = password('新密码'); 
	例子：mysql> set password for root@localhost = password('123'); 
方式2:
	格式：mysqladmin -u用户名 -p旧密码 password 新密码 
	例子：mysqladmin -uroot -p123456 password 123 
方式3:
	mysql> use mysql; 
	mysql> update user set password=password('123') where user='root' and host='localhost';   5.6 password--5.7 authentication_string
	mysql> flush privileges; 

```

### 忘记密码的措施:

```
1. 关闭正在运行的MySQL服务，net stop mysql（这个mysql是你添加的mysqld到系统服务时的服务名）。 
2. 打开DOS窗口，转到mysql\bin目录。 
3. 输入mysqld --skip-grant-tables 回车。
4. 连接mysql,修改密码
```

### 字符集编码:

```mysql
windows下安装目录下,也就是和bin一个层级,创建一个my.ini文件,unix下是my.cnf,写上下面的配置
[mysqld]
character_set_server=utf8
collation-server=utf8_general_ci 
[client]
default-character-set=utf8
[mysql]
user=root
password=666
default-character-set=utf8

永久生效就重启服务
重启mysql服务，让配置文件生效
```

### 完整连接指令

```mysql
mysql -h 192.168.1.20 -P 3306 -u root -p 密码
```



## 二 数据库操作

库---文件夹

表---文件(t1.frm,  t1.idb)

行---t1.idb里面的数据



### 库常用操作

```mysql
CREATE DATABASE 数据库名 charset utf8;
1 查看数据库
show databases;
show create database db1;
select database();

2 选择数据库
USE 数据库名

3 删除数据库
DROP DATABASE 数据库名;

4 修改数据库
alter database db1 charset utf8;
```

查看当前登录用户

```mysql
select user();
```



### 表操作

#### 存储引擎

​	innodb和myisam  inndb行级锁   myisam表锁

​	innodb支持事务

#### 	事务的四大特性

```
事务的四大特性：
        1.原子性(Atomicity)
            事务是一个不可分割的单位，事务中的所有SQL等操作要么都发生，要么都不发生。
        2.一致性(Consistency)
            事务发生前和发生后，数据的完整性必须保持一致。
        3.隔离性(Isolation)
            当并发访问数据库时，一个正在执行的事务在执行完毕前，对于其他的会话是不可见的，多个并发事务之间的数据是相互隔离的。也就是其他人的操作在这个事务的执行过程中是看不到这个事务的执行结果的，也就是他们拿到的是这个事务执行之前的内容，等这个事务执行完才能拿到新的数据。
        4.持久性(Durability)
            一个事务一旦被提交，它对数据库中的数据改变就是永久性的。如果出了错误，事务也不允撤销，只能通过'补偿性事务'。
```



#### 常用操作

```
创建表
create table 表名(
	字段名1 类型[(宽度) 约束条件],  #name char(10) not null default...
	字段名2 类型[(宽度) 约束条件],
	字段名3 类型[(宽度) 约束条件]
);
查看表
show tables;
mysql> describe t1;  简写desc t1;
+-------+-----------------------+------+-----+---------+-------+
| Field | Type                  | Null | Key | Default | Extra |
+-------+-----------------------+------+-----+---------+-------+
| id    | int(11)               | YES  |     | NULL    |       |
| name  | varchar(50)           | YES  |     | NULL    |       |
| sex   | enum('male','female') | YES  |     | NULL    |       |
| age   | int(3)                | YES  |     | NULL    |       |
+-------+-----------------------+------+-----+---------+-------+

mysql> show create table t1\G; #查看表详细结构，可加\G
mysql> show create table app01_book\G;
*************************** 1. row ***************************
       Table: app01_book
Create Table: CREATE TABLE `app01_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `price` decimal(16,2) NOT NULL,
  `pub_time` date NOT NULL,
  `publish` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_book_title_0826a773_uniq` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

```

#### 修改表

```mysql
1. 修改表名
      ALTER TABLE 表名 
                          RENAME 新表名;

2. 增加字段
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…], #注意这里可以通过逗号来分割，一下添加多个约束条件
                          ADD 字段名  数据类型 [完整性约束条件…];
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…]  FIRST; #添加这个字段的时候，把它放到第一个字段位置去。
      ALTER TABLE 表名
                          ADD 字段名  数据类型 [完整性约束条件…]  AFTER 字段名;#after是放到后的这个字段的后面去了，我们通过一个first和一个after就可以将新添加的字段放到表的任意字段位置了。
                            
3. 删除字段
      ALTER TABLE 表名 
                          DROP 字段名;

4. 修改字段
      ALTER TABLE 表名 
                          MODIFY  字段名 数据类型 [完整性约束条件…];
      ALTER TABLE 表名 
                          CHANGE 旧字段名 新字段名 旧数据类型 [完整性约束条件…];  #change比modify还多了个改名字的功能，这一句是只改了一个字段名
      ALTER TABLE 表名 
                          CHANGE 旧字段名 新字段名 新数据类型 [完整性约束条件…];#这一句除了改了字段名，还改了数据类型、完整性约束等等的内容
                          
                          
                          
测试实例
1. 修改存储引擎
mysql> alter table service 
    -> engine=innodb;

2. 添加字段
mysql> alter table student10
    -> add name varchar(20) not null,
    -> add age int(3) not null default 22;
    
mysql> alter table student10
    -> add stu_num varchar(10) not null after name;                //添加name字段之后

mysql> alter table student10                        
    -> add sex enum('male','female') default 'male' first;          //添加到最前面

3. 删除字段
mysql> alter table student10
    -> drop sex;

mysql> alter table service
    -> drop mac;

4. 修改字段类型modify
mysql> alter table student10
    -> modify age int(3);
mysql> alter table student10
    -> modify id int(11) not null primary key auto_increment;    //修改为主键

5. 增加约束（针对已有的主键增加auto_increment）
mysql> alter table student10 modify id int(11) not null primary key auto_increment;
ERROR 1068 (42000): Multiple primary key defined

mysql> alter table student10 modify id int(11) not null auto_increment;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

6. 对已经存在的表增加复合主键
mysql> alter table service2
    -> add primary key(host_ip,port);        

7. 增加主键
mysql> alter table student1
    -> modify name varchar(10) not null primary key;

8. 增加主键和自动增长
mysql> alter table student1
    -> modify id int not null primary key auto_increment;

9. 删除主键
a. 删除自增约束
mysql> alter table student10 modify id int(11) not null; 

b. 删除主键
mysql> alter table student10                                 
    -> drop primary key;
```



#### 数据类型

数值类型  参考博客<https://www.cnblogs.com/clschao/articles/9959559.html#_label2>

##### 	整数类型

​		 int  bigint  smallint

```
create table t1(age int unsigned);  unsigned无符号,不能为负数
```

##### 	浮点型:

​		float  double  decimal	 精度不同

```
create table t1(money float(255,30));   255:小数位数+整数位数   30:小数点后面的位数
create table t1(money double(255,30));  255:小数位数+整数位数   30:小数点后面的位数
create table t1(money decimal(65,30));   65:小数位数+整数位数   30:小数点后面的位数
```

##### 	字符串类型

char  和  varchar

```
区别:char(3)定长   varchar(3)不定长  3值得是字符  一个中文utf-8编码的代表3个字节
a00bb0ccc         1-2byte空间存数据长度    1a2bb2cc 理论上效率比char低
char--255字节      varchar--65535

```

##### 	日期类型

​	date  time  datetime

```mysql
    mysql> create table t11(d date,t time,dt datetime);
    mysql> desc t11;
    +-------+----------+------+-----+---------+-------+
    | Field | Type     | Null | Key | Default | Extra |
    +-------+----------+------+-----+---------+-------+
    | d     | date     | YES  |     | NULL    |       |
    | t     | time     | YES  |     | NULL    |       |
    | dt    | datetime | YES  |     | NULL    |       |
    +-------+----------+------+-----+---------+-------+

    mysql> insert into t11 values(now(),now(),now());
    mysql> select * from t11;
    +------------+----------+---------------------+
    | d          | t        | dt                  |
    +------------+----------+---------------------+
    | 2017-07-25 | 16:26:54 | 2017-07-25 16:26:54 |
    +------------+----------+---------------------+
```

##### 	枚举和集合类型

```mysql
          枚举类型（enum）
            An ENUM column can have a maximum of 65,535 distinct elements. (The practical limit is less than 3000.)
            示例：
                CREATE TABLE shirts (
                    name VARCHAR(40),
                    size ENUM('x-small', 'small', 'medium', 'large', 'x-large')
                );
                INSERT INTO shirts (name, size) VALUES ('dress shirt','large'), ('t-shirt','medium'),('polo shirt','small');

  

          集合类型（set）
            A SET column can have a maximum of 64 distinct members.
            示例：
                CREATE TABLE myset (col SET('a', 'b', 'c', 'd'));
                INSERT INTO myset (col) VALUES ('a,d'), ('d,a'), ('a,d,a'), ('a,d,d'), ('d,a,d');
```



#### 完整性约束

​	参考博客<https://www.cnblogs.com/clschao/articles/9968396.html#_label2>

​	not null   default 

```mysql
默认是可为空的.
create table t1(id int,name char(5) not null,age int default 10); 
没有指定字段插入数据的时候:insert into t1  values(1,'xx',18); 必须全部对应给数据
指定字段插入数据: insert into t1(name) values('saoy');  id=null,age=10

```

​	unique  唯一的,字段不能重复(加速查询的效果)

```mysql
mysql> create table t1(id int unique,name char(10));
mysql> desc t1;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | YES  | UNI | NULL    |       |
| name  | char(10) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
```

​	primary key主键  unique+not null   加速查询,innodb存储引擎组织存储这个表中数据的依据,通过这个主键字段来建立索引,聚集索引.

```mysql
mysql> create table t2(id int primary key auto_increment,name char(10));
Query OK, 0 rows affected (0.20 sec)

mysql> desc t2;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| name  | char(10) | YES  |     | NULL    |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.01 sec)

```



​	foreign key 外键  表示表关系的,表的三种关系,一对一,  一对多(多对一),  多对多

```mysql
创建:
mysql> create table t3(id int primary key,name char(10));
#一对多的写法
mysql> create table t4(id int primary key,title char(10),t3_id int, constraint t4_t3_fk foreign key(t3_id) references t3(id) on delete cascade on update cascade);
一对一:
mysql> create table t4(id int primary key,title char(10),t3_id int unique, constraint t4_t3_fk foreign key(t3_id) references t3(id) on delete cascade on update cascade);

多对多
t32t4表
id  t3_id(fk到t3表)  t4_id(fk到t4表)

查看外键名称show create table t4;
------------------------------------------------------------------------
| t4    | CREATE TABLE `t4` (
  `id` int(11) NOT NULL,
  `title` char(10) DEFAULT NULL,
  `t3_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t4_t3_fk` (`t3_id`),
  CONSTRAINT `t4_t3_fk` FOREIGN KEY (`t3_id`) REFERENCES `t3` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+-------+---------------------------------------------------------------
```

```
非级联的情况下:

​	被关联表先创建,被关联表先有数据,被关联表不能随意进行删除数据和更改本关联字段数据的操作    关联表可以删除数据  

本关联的表的那个字段,必须是唯一的.
```

### 行操作

```mysql
1. 插入完整数据（顺序插入）
    语法一：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) VALUES(值1,值2,值3…值n); #指定字段来插入数据，插入的值要和你前面的字段相匹配

    语法二：
    INSERT INTO 表名 VALUES (值1,值2,值3…值n); #不指定字段的话，就按照默认的几个字段来插入数据

2. 指定字段插入数据
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…) VALUES (值1,值2,值3…);

3. 插入多条记录
    语法：#插入多条记录用逗号来分隔
    INSERT INTO 表名 VALUES
        (值1,值2,值3…值n),
        (值1,值2,值3…值n),
        (值1,值2,值3…值n);
        
4. 插入查询结果
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) 
                    SELECT (字段1,字段2,字段3…字段n) FROM 表2
                    WHERE …; #将从表2里面查询出来的结果来插入到我们的表中，但是注意查询出来的数据要和我们前面指定的字段要对应好
                    
更新数据
语法：
    UPDATE 表名 SET 
        字段1=值1,  #注意语法，可以同时来修改多个值，用逗号分隔
        字段2=值2,
        WHERE CONDITION; #更改哪些数据，通过where条件来定位到符合条件的数据

示例：
    UPDATE mysql.user SET password=password(‘123’) 
        where user=’root’ and host=’localhost’; #这句话是对myslq这个库中的user表中的user字段为'root'并且host字段为'localhost'的这条记录的password字段的数据进行修改，将passord字段的那个数据改为password('123')这个方法对123加工后的密码数据，password()这个方法是mysql提供的密码进行加密用的方法。
        定位到某个记录，并把这个记录中的某项内容更改掉
        
删除数据
语法：
    DELETE FROM 表名 
        WHERE CONITION; #删除符合条件的一些记录
    DELETE FROM 表名；如果不加where条件，意思是将表里面所有的内容都删掉，但是清空所有的内容，一般我们用truncate ，能够将id置为零，delete不能将id置零，再插入数据的时候，会按照之前的数据记录的id数继续递增
示例：
    DELETE FROM mysql.user 
        WHERE password=’123’;

练习：
    更新MySQL root用户密码为mysql123
    删除除从本地登录的root用户以外的所有用户
    
truncate 表名; 清空表,id重置
```

#### 行记录的查询

```
SELECT distinct 字段1,字段2... FROM 库名.表名 #from后面是说从库的某个表中去找数据，mysql会去找到这个库对应的文件夹下去找到你表名对应的那个数据文件，找不到就直接报错了，找到了就继续后面的操作
                  WHERE 条件       #从表中找符合条件的数据记录，where后面跟的是你的查询条件
                  GROUP BY field（字段）   #分组
                  HAVING 筛选      #过滤，过滤之后执行select后面的字段筛选，就是说我要确定一下需要哪个字段的数据，你查询的字段数据进行去重，然后在进行下面的操作
                  ORDER BY field（字段）   #将结果按照后面的字段进行排序
                  LIMIT 限制条数    #将最后的结果加一个限制条数，就是说我要过滤或者说限制查询出来的数据记录的条数

```

关键字的优先级

单表查询:博客<https://www.cnblogs.com/clschao/articles/9995531.html>****

多表查询博客:<https://www.cnblogs.com/clschao/articles/9995815.html>

### 连表操作

查询技术部门所有的员工的姓名.

##### 第一种:笛卡尔积

```mysql
1 连查两张表
mysql> select * from dep,emp; 将dep和emp中所有的数据都统一的进行一次对应.
2 找到关联关系数据
mysql> select * from dep,emp where dep.id = emp.dep_id;
3 通过关联关系数据找到对应的记录
mysql> select * from dep,emp where dep.id = emp.dep_id and dep.name ='技术';
4 获取对应字段数据
mysql> select emp.name from dep,emp where dep.id = emp.dep_id and dep.name ='技术';
+-----------+
| name      |
+-----------+
| egon      |
| liwenzhou |
+-----------+
2 rows in set (0.00 sec)

```



##### 第二种  连表操作  join

哪个表在前,哪个表在后,都没问题.

inner join

```

mysql> select emp.name from dep inner join emp on dep.id = emp.dep_id where dep.name='技术';
+-----------+
| name      |
+-----------+
| egon      |
| liwenzhou |
+-----------+
2 rows in set (0.00 sec)

```

left join   以左边的表为主表,右边的表为辅表,主表中有的数据,必须全部显示,辅表对应不上的,用null来补充

```mysql
mysql> select * from dep left join emp on dep.id = emp.dep_id;
+------+--------------+------+-----------+--------+------+--------+
| id   | name         | id   | name      | sex    | age  | dep_id |
+------+--------------+------+-----------+--------+------+--------+
|  200 | 技术         |    1 | egon      | male   |   18 |    200 |
|  201 | 人力资源     |    2 | alex      | female |   48 |    201 |
|  201 | 人力资源     |    3 | wupeiqi   | male   |   38 |    201 |
|  202 | 销售         |    4 | yuanhao   | female |   28 |    202 |
|  200 | 技术         |    5 | liwenzhou | male   |   18 |    200 |
|  203 | 运营         | NULL | NULL      | NULL   | NULL |   NULL |
+------+--------------+------+-----------+--------+------+--------+
6 rows in set (0.00 sec)

```

right join 和left join相反

```mysql

mysql> select * from dep right join emp on dep.id = emp.dep_id;
+------+--------------+----+------------+--------+------+--------+
| id   | name         | id | name       | sex    | age  | dep_id |
+------+--------------+----+------------+--------+------+--------+
|  200 | 技术         |  1 | egon       | male   |   18 |    200 |
|  200 | 技术         |  5 | liwenzhou  | male   |   18 |    200 |
|  201 | 人力资源     |  2 | alex       | female |   48 |    201 |
|  201 | 人力资源     |  3 | wupeiqi    | male   |   38 |    201 |
|  202 | 销售         |  4 | yuanhao    | female |   28 |    202 |
| NULL | NULL         |  6 | jingliyang | female |   18 |    204 |
+------+--------------+----+------------+--------+------+--------+
6 rows in set (0.00 sec)
```



union

```mysql
mysql> select * from dep left join emp on dep.id = emp.dep_id
    -> union
    -> select * from dep right join emp on dep.id = emp.dep_id;
+------+--------------+------+------------+--------+------+--------+
| id   | name         | id   | name       | sex    | age  | dep_id |
+------+--------------+------+------------+--------+------+--------+
|  200 | 技术         |    1 | egon       | male   |   18 |    200 |
|  201 | 人力资源     |    2 | alex       | female |   48 |    201 |
|  201 | 人力资源     |    3 | wupeiqi    | male   |   38 |    201 |
|  202 | 销售         |    4 | yuanhao    | female |   28 |    202 |
|  200 | 技术         |    5 | liwenzhou  | male   |   18 |    200 |
|  203 | 运营         | NULL | NULL       | NULL   | NULL |   NULL |
| NULL | NULL         |    6 | jingliyang | female |   18 |    204 |
+------+--------------+------+------------+--------+------+--------+
7 rows in set (0.00 sec)
    
```



##### 第三种:子查询

```mysql

mysql> select name from emp where dep_id = (select id from dep where name = '技术');
+-----------+
| name      |
+-----------+
| egon      |
| liwenzhou |
+-----------+
2 rows in set (0.00 sec)
所有过滤条件
子查询：
#1：子查询是将一个查询语句嵌套在另一个查询语句中。
#2：内层查询语句的查询结果，可以为外层查询语句提供查询条件。
#3：子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字
#4：还可以包含比较运算符：= 、 !=、> 、<等
exists实例  
mysql> select * from emp where exists (select * from dep where id=1);
Empty set (0.00 sec)

mysql> select * from emp where exists (select * from dep where id=200);
+----+------------+--------+------+--------+
| id | name       | sex    | age  | dep_id |
+----+------------+--------+------+--------+
|  1 | egon       | male   |   18 |    200 |
|  2 | alex       | female |   48 |    201 |
|  3 | wupeiqi    | male   |   38 |    201 |
|  4 | yuanhao    | female |   28 |    202 |
|  5 | liwenzhou  | male   |   18 |    200 |
|  6 | jingliyang | female |   18 |    204 |
+----+------------+--------+------+--------+
6 rows in set (0.00 sec)

```



pymysql使用

```
import pymysql
user=input('用户名: ').strip()
pwd=input('密码: ').strip()

#链接，指定ip地址和端口，本机上测试时ip地址可以写localhost或者自己的ip地址或者127.0.0.1，然后你操作数据库的时候的用户名，密码，要指定你操作的是哪个数据库，指定库名，还要指定字符集。不然会出现乱码
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123',database='student',charset='utf8') #指定编码为utf8的时候，注意没有-，别写utf-8，数据库为
#得到conn这个连接对象
#游标
cursor=conn.cursor() #这就想到于mysql自带的那个客户端的游标mysql> 在这后面输入指令，回车执行
#cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) #获取字典数据类型表示的结果：{'sid': 1, 'gender': '男', 'class_id': 1, 'sname': '理解'} {'字段名':值}


#然后给游标输入sql语句并执行sql语句execute
sql='select * from userinfo where name="%s" and password="%s"' %(user,pwd) #注意%s需要加引号，执行这句sql的前提是医药有个userinfo表，里面有name和password两个字段，还有一些数据，自己添加数据昂
print(sql)
res=cursor.execute(sql) #执行sql语句，返回sql查询成功的记录数目，是个数字，是受sql语句影响到的记录行数，其实除了受影响的记录的条数之外，这些记录的数据也都返回了给游标,这个就相当于我们subprocess模块里面的管道PIPE，乘放着返回的数据
#all_data=cursor.fetchall()  #获取返回的所有数据，注意凡是取数据，取过的数据就没有了，结果都是元祖格式的
#many_data=cursor.fetchmany(3) #一下取出3条数据，
#one_data=cursor.fetchone()  #按照数据的顺序，一次只拿一个数据，下次再去就从第二个取了，因为第一个被取出去了，取一次就没有了，结果也都是元祖格式的
  fetchone：(1, '男', 1, '理解')
  fetchone：(2, '女', 1, '钢蛋')
  fetchall：((3, '男', 1, '张三'), (4, '男', 1, '张一')）

#上面fetch的结果都是元祖格式的，没法看出哪个数据是对应的哪个字段，这样是不是不太好看，想一想，我们可以通过python的哪一种数据类型，能把字段和对应的数据表示出来最清晰，当然是字典{'字段名':值}
#我们可以再创建游标的时候，在cursor里面加上一个参数：cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)获取的结果就是字典格式的，fetchall或者fetchmany取出的结果是列表套字典的数据形式

上面我们说，我们的数据取一次是不是就没有了啊，实际上不是的，这个取数据的操作就像读取文件内容一样，每次read之后，光标就移动到了对应的位置，我们可以通过seek来移动光标
同样，我们可以移动游标的位置，继续取我们前面的数据,通过cursor.scroll(数字，模式)，第一个参数就是一个int类型的数字，表示往后移动的记录条数，第二个参数为移动的模式，有两个值：absolute：绝对移动，relative：相对移动
#绝对移动：它是相对于所有数据的起始位置开始往后面移动的
#相对移动：他是相对于游标的当前位置开始往后移动的

#绝对移动的演示
#print(cursor.fetchall())
#cursor.scroll(3,'absolute') #从初始位置往后移动三条，那么下次取出的数据为第四条数据
#print(cursor.fetchone())

#相对移动的演示
#print(cursor.fetchone())
#cursor.scroll(1,'relative') #通过上面取了一次数据，游标的位置在第二条的开头，我现在相对移动了1个记录，那么下次再取，取出的是第三条，我相对于上一条，往下移动了一条
#print(cursor.fetchone())

print(res) #一个数字

cursor.close() #关闭游标
conn.close()   #关闭连接

if res:
    print('登录成功')
else:
    print('登录失败')
```



视图

```mysql
#注意,修改视图虚拟表的数据,会改动真实表的数据
创建:create view teacher_view(视图名) as select tid from teacher where tname='李平老师';
查询:
mysql> select * from teacher_view;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
修改:
语法：ALTER VIEW 视图名称 AS SQL语句，这基本就和删掉视图重新创建一个视图的过程是一样的，修改视图没什么好讲的，这里就简单提一下，就不讲啦~~，还不如我们直接删掉，再重新创建呢
mysql> alter view teacher_view as select * from course where cid>3;
Query OK, 0 rows affected (0.04 sec)

mysql> select * from teacher_view;
+-----+-------+------------+
| cid | cname | teacher_id |
+-----+-------+------------+
|   4 | xxx   |          2 |
|   5 | yyy   |          2 |
+-----+-------+------------+
2 rows in set (0.00 sec)
删除视图:
语法：DROP VIEW 视图名称
DROP VIEW teacher_view

```



触发器

```msyql
# 插入前
CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
BEGIN #begin和end里面写触发器要做的sql事情，注意里面的代码缩进，并且给触发器起名字的时候，名字的格式最好这样写，有表示意义，一看名字就知道要做什么，是给哪个表设置的触发器
    ...
END

# 插入后
CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除前
CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除后
CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新前
CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新后
CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END

删除触发器
drop trigger tri_after_insert_cmd;
```



sql_mode sql语句模式

严格模式  set global sql_mode='strict_trans_tables';

参考博客:<https://www.cnblogs.com/clschao/articles/9962347.html>

事务:

```
开启事务:
start transaction;或者begin;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='chao'; #中介拿走10元
update user set balance=1090 where name='ysb'; #卖家拿到90元

rollback;

commit;  #只要不进行commit操作，就没有保存下来，没有刷到硬盘上

结合触发器:
delimiter //
create PROCEDURE p5()
BEGIN 
DECLARE exit handler for sqlexception   -- 捕获sql语句的异常
BEGIN 
rollback; 
END;

START TRANSACTION; 
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='chao'; #中介拿走10元
#update user2 set balance=1090 where name='ysb'; #卖家拿到90元
update user set balance=1090 where name='ysb'; #卖家拿到90元
COMMIT;

END //
delimiter ;
```



存储过程

```
#查看存储过程的一些信息：show create procedure p3; #查看视图啊、触发器啊都这么看，还可以用\G，show create procedure p3\G;\G的意思是你直接查看表结构可能横向上显示不完，\G是让表给你竖向显示，一row是一行的字段
delimiter //
create procedure p3(
    in n1 int,
    out res int
)
BEGIN
    select * from blog where id > n1;  
    set res = 1;  #我在这里设置一个res=1，如果上面的所有sql语句全部正常执行了，那么这一句肯定也就执行了，那么此时res=1，如果我最开始传入的时候，给res的值设置的是0，
#那么你想，最后我接收到的返回值如果是0，那么说明你中间肯定有一些sql语句执行失败了
#注意写法：out的那个参数，可以用set来设置，set设置之后表示这个res可以作为返回值，并且不需要像python一样写一个return，你直接set之后的值，就是这个存储过程的返回值
END //
delimiter ;

#在mysql中调用
set @res=0; #这是MySQL中定义变量名的固定写法(set @变量名=值)，可以自己规定好，0代表假（执行失败），1代表真（执行成功），如果这个被改为1了，说明存储过程中的sql语句执行成功了
call p3(3,@res);#注意：不要这样写：call p3（3，1），这样out的参数值你写死了，没法确定后面这个1是不是成功了，也就是说随后这个out的值可能改成0了，也就是失败了，但是这样你就判断不了了，你后面查看的这个res就成1了，所以这个参数应该是一个变量名昂，定义变量名就是上一句,如果你直接传一个常量数字，会报错的，写法不对。
select @res; #看一下这个结果，就知道这些sql语句是不是执行成功了，大家明白了吗~~~

#在python中基于pymysql调用，在python中只需要知道存储过程的名字就行了
cursor.callproc('p3',(3,0)) #0相当于set @res=0，为什么这里这个out参数可以写常数0啊，因为你用的pymysql,人家会帮你搞定，pymysql其实会帮你写成这样：第一个参数变量名：@_p3_0=3，第二个：@_p3_1=0，也就是pymysql会自动帮你对应上一个变量名，pymysql只是想让你写的时候更方便
#沿着网络将存储过程名和参数发给了mysql服务端，比咱们发一堆的sql语句肯定要快对了，mysql帮你调用存储过程
print(cursor.fetchall()) #查询select的查询结果

cursor.execute('select @_p3_0,@_p3_1;') #@_p3_0代表第一个参数，@_p3_1代表第二个参数，即返回值
print(cursor.fetchall())
#别忘了关掉：
cursor.close()
conn.close()
#注意昂：存储过程在哪个库里面建的，就只能在哪个库里面用
```

存储过程结合事务

```mysql
delimiter //
            create procedure p4(
                out status int
            )
            BEGIN
                1. 声明如果出现异常则执行{
                    set status = 1;
                    rollback;
                }
                   
                开始事务
                    -- 由秦兵账户减去100
                    -- 方少伟账户加90
                    -- 张根账户加10
                    commit;
                结束
                
                set status = 2;
                
                
            END //
            delimiter ;

#实现
delimiter //
create PROCEDURE p5(
    OUT p_return_code tinyint
)
BEGIN 
    DECLARE exit handler for sqlexception   #声明如果一旦出现异常则执行下面的这个begin和end里面的操作
    BEGIN 
        -- ERROR   #--是什么啊，忘了吧，是注释的意思，就告诉你后面是对错误的处理
        set p_return_code = 1;  #将out返回值改为1了，这是你自己规定的，1表示出错了
        rollback;  #回滚事务
    END; 

    DECLARE exit handler for sqlwarning  #声明了出现警告信息之后你的操作行为
    BEGIN 
        -- WARNING 
        set p_return_code = 2; 
        rollback; 
    END; 

    START TRANSACTION;  #其实咱们这个存储过程里面就是执行这个事务，并且一直检测着这个事务，一旦出错或者出现警告，就rollback
        DELETE from tb1; #事务里面的任何一条sql执行失败或者执行出现警告，都会执行上面我们声明的那些对应的操作，如果没有任何的异常，就会自动执行下面的commit，并执行后面成功的sql
        insert into blog(name,sub_time) values('yyy',now());  #拿我的代码进行测试的时候，别忘了改成你自己库里的表，还有表里面对应的字段名要有的，自己测试的时候，可以自己写一个错误的sql来试试看
    COMMIT; 

    -- SUCCESS 
    set p_return_code = 0; #0代表执行成功

END //
delimiter ;

#在mysql中调用存储过程
set @res=123;
call p5(@res);
select @res;

#在python中基于pymysql调用存储过程
cursor.callproc('p5',(123,)) #注意后面这个参数是个元祖，别忘了逗号，按照我们上面规定的，上面有三个值0，1，2：0成功、1失败、2警告也是失败。所以我们传给这个out参数的值只要不是这三个值就行了，这里给的是100
print(cursor.fetchall()) #查询select的查询结果

cursor.execute('select @_p5_0;')
print(cursor.fetchall())
#执行成功以后，查看一下结果就能看到执行后的值了

删除存储过程
drop procedure proc_name;
```

参考博客:<https://www.cnblogs.com/clschao/articles/10034539.html#_label1>



### 索引

```
添加主键索引:
创建的时候添加:  添加索引的时候要注意,给字段里面数据大小比较小的字段添加,给字段里面的数据区分度高的字段添加.
聚集索引的添加方式
创建的是添加
Create table t1(
Id int primary key,
)
Create table t1(
Id int,
Primary key(id)     --  
)

表创建完了之后添加
Alter table 表名 add primary key(id)
删除主键索引:
Alter table 表名 drop primary key;


唯一索引:
Create table t1(
Id int unique,
)

Create table t1(
Id int,
Unique key uni_name (id)   -- Unique key uni_name (id,name,xx) 联合唯一索引
)

表创建好之后添加唯一索引:
alter table s1 add unique key  u_name(id);
删除:
Alter table s1 drop index u_name;

普通索引:
创建:
Create table t1(
Id int,
Index index_name(id) -- Index index_name(id,name) 联合索引
)
Alter table s1 add index index_name(id);
Create index index_name on s1(id);

删除:
Alter table s1 drop index u_name;
DROP INDEX 索引名 ON 表名字;

```



用户创建

```
1.创建用户:
# 指定ip：192.118.1.1的chao用户登录
create user 'chao'@'192.118.1.1' identified by '123';
# 指定ip：192.118.1.开头的chao用户登录
create user 'chao'@'192.118.1.%' identified by '123';
# 指定任何ip的chao用户登录
create user 'chao'@'%' identified by '123';

2.删除用户
drop user '用户名'@'IP地址';


3.修改用户
rename user '用户名'@'IP地址' to '新用户名'@'IP地址';

4.修改密码
set password for '用户名'@'IP地址'=Password('新密码');
```



权限分配

```
#查看权限
show grants for '用户'@'IP地址'

#授权 chao用户仅对db1.t1文件有查询、插入和更新的操作
grant select ,insert,update on db1.t1 to "chao"@'%';

# 表示有所有的权限，除了grant这个命令，这个命令是root才有的。chao用户对db1下的t1文件有任意操作
grant all privileges  on db1.t1 to "chao"@'%';
#chao用户对db1数据库中的文件执行任何操作
grant all privileges  on db1.* to "chao"@'%';
#chao用户对所有数据库中文件有任何操作
grant all privileges  on *.*  to "chao"@'%';
 
#取消权限
 
# 取消chao用户对db1的t1文件的任意操作
revoke all on db1.t1 from 'chao'@"%";  

# 取消来自远程服务器的chao用户对数据库db1的所有表的所有权限

revoke all on db1.* from 'chao'@"%";  

取消来自远程服务器的chao用户所有数据库的所有的表的权限
revoke all privileges on *.* from 'chao'@'%';
```



mysqldump备份

```
C:\WINDOWS\system32>mysqldump -h 127.0.0.1 -u root -p666 crm2 > f:\数据库备份练习\crm2.sql
还原:
	1.连接到数据库中，并创建crm2这个库
　　　　　　mysql -u root -p666
　　　　　　mysql> create database crm2;
　　　　2.退出mysql或者重新启动一个cmd窗口，然后执行
　　　　　　mysql -uroot -p 库名 < mysqldump出来的那个sql文件的路径
　　　　例如：mysql -uroot -p crm2< f:\数据库备份练习\crm2.sql
　　　　
加上-B参数备份
　　　　1.mysqldump -uroot -p -B crm2> f:\数据库备份练习\crm2.sql
	还原:
　　　　2.在cmd窗口下执行：mysql -uroot -p < f:\数据库备份练习\crm2.sql
```













​	



​	









































































