ansible

批量执行远程主机的脚本或者命令

saltstack

puppt ruby

ping(系统的ping ICMP ansible的是ssh)

命令格式

```shell
ansibel host-pattern opetions
-m 模块名称
-a 模块的参数
```

host-pattern 格式

- 单个的ip地址
- 多个的ip地址
- 单个组
- 多个组
  - 交集
    - 'web:&db'
  - 并集
    - web,db
    - 'web:db'
  - 差集
    - 'web:!db'   web组存在但是db不存在
- 全部   all

command  执行远程的命令,不支持特殊字符,<>|;%$&

- chdir  切换目录并执行命令
- creates 存在就不执行
- removes 存在就执行

shell 执行远程的命令或者脚本

- chdir  切换目录并执行命令
- creates 存在就不执行
- removes 存在就执行

script 执行本地的脚本

- chdir  切换目录并执行命令
- creates 判断远程机器上存在就不执行
- removes 判断远程机器上存在就执行

copy 将本地文件复制到远程机器上

- src 源文件地址,如果带/,则复制的是目录下所有文件,如果不带,则是整个目录,如果整个目录的权限被修改,则里面文件的权限也会跟着变化
- dest 目标地址
- group 属组
- mode 文件的权限
- owner 属主
- backup 备份文件
- content 直接写文件,覆盖写

file 用来在远程机器上创建文件,文件夹,软连接硬链接等

- path 
- src
  - link
  - hard
- group
- mode
- owner
- state
  - directory
  - touch
  - link
  - hard
  - absent
  - file (如果不存在,也不会创建)

fetch 拉取远程的文件,以主机名或者ip地址创建一个目录,并保存原来的目录结构

- dest
- src

yum 安装linux的软件包

- name @包组名称

  ```shell
  yum groupinstall 
  yum grouplist
  yum search
  yum makecache  用来重建缓存
  yum clear 用来清除缓存
  ```



- state
  - installed
  - removed

pip 安装python包

- name
- 文件
- 虚拟环境

service 启停服务,在命令可以通过service或者systemctl启动的服务,提供启动文件

- name 名称
- enabled 开机自启动
- state
  - started
  - stopped
  - restarted
  - reloaded 平滑重启
- user 启动的用户

cron 定时任务

- minute  分钟最好是不要用*
- hour
- day
- month
- weekday
- job 尽量写绝对路径
- name 默认的是none,name必须唯一
- user
- disabled
- state
  - absent

user 用来创建用户

- name
- uid
- home
- shell
- group
- groups
- remove 删除用户并删除用户的家目录
- system 系统用户
- state

group  创建组

- name
- gid
- system
- state

setup 用来获取系统的参数

template 用来动态的传递参数,在setup里面获取,跟copy的一样

replace 用来做替换,支持正则

Ad-hoc

playbook

yaml

- 列表 [] \-

- 字典 key: value

- 后缀名: yaml yml

  ```shell
  - hosts: web
    remote_user: root
    tasks:
    - name: name
      module: name={{item}}
      with_items:
      - 
      - 
    - name: name
      module: name={{item.name}} age={{item.age}}
      with_items:
      - {"name":alex,"age":9000}
      - 
  ```

  传参方式

  - {{  }}
  - -e key=value
  - hosts文件,ip或者主机名后面直接写
  - hosts文件里面,写[groupname:vars]
  - playbook写上vars
  - register 可以注册,取值{{ name.stdout }}

  优先级

  ​	-e > playbook > hosts文件

  tags 指定单独的任务执行

  handlers 被触发的任务

  notify 触发任务

  when 判断

  with_items 循环 {{ item }}

  嵌套循环

roles 角色

- 目录结构清晰

- 可以相互调用

  ```shell
  roles
  - nginx
  	- tasks
  		- main.yml
  		- copy.yml
  	- templates
  	- vars
  		- main.yml
  	- handlers
  		- main.yml
  	- files
  	- medias
  - redis
  - uwsgi
  - mysql
  - haproxy
  ```

  查找顺序

  - 先找roles目录下的对应目录
  - tasks里面查找main.yml文件,如果遇到import_task,则加载对应的任务
  - 如果遇到了template的话,则去templates目录里面查找对应的文件,
  - 如果遇到了copy的话,则去files目录里面查找对应的文件
  - 如果遇到了notify,则去handlers目录里面找main.yml文件
  - 如果遇到了变量,则去vars目录里面查找main.yml文件

  proxy_pass 

  uwsgi_pass

  - ip+端口
  - socket文件

  首选socket文件,其次是ip+端口

git 做版本控制

git init . 

git add .

git commit -m ""

git remote add origin https://url.git

git push

git pull

git clone  https://url.git

git status

git log 查看日志,当前节点之前的日志

git reflog 全部日志

git reset --head  hash值  回退到指定的版本 

git reset HEAD filename   将缓存区的文件拉取到工作区

git checkout --filename   将指定文件回退到最后一次

git diff  对于缓存区和工作区

git diff --cached  对于本地仓库和缓存去的区别

git stash 创建一个快照

git stash list 查看快照

git stash pop 取出快照并删除快照

git stash drop 删除快照

git stash apply 取出快照

git branch 查看分支

git branch name 创建分支

git branch -d name 删除分支

git checkout -b name 创建并切换分支

git checkout name 切换分支

git merge name 合并分支,在合并到的分支上合并

git tag  查看tag

git tag -a "v1.0" -m "描述信息" 创建tag

git tag -a "v0.1" -m "描述信息" hash值 对过去的某个版本做tag

git push origin --tags 上传

git tag  -d tagname 本地删除

git push origin :refs/tags/tagname 删除远程仓库的tag

git checkout tagname 

.gitignore

变基 rebase

git fetch 将远程仓库的东西拉取下来,但是不合并

git pull = git fetch + git merge

celery  用来执行异步 延时任务 周期任务

```python
from celery import Celery
c=Celery("tasks",broker="redis://",backend="redis://")#rabbitmq

@c.task
def myfun1(a,b)
	return a+b
```

```PYTHON
from c1 import myfun1,c
from celey.result import AsyncResult 
#异步任务
s=myfun1.delay(10,20)

a=AsyncResult(id=s.id,app=c)
a.get(propagate=False) #获取返回值
a.status #获取执行的状态   夯住
a.successfully() #获取状态
a.traceback

#延时任务
myfun1.apply_async((10,20),countdown=5) #生产者是立马生成任务,消费者是立马拿到之后5s之后在执行
myfun1.apply_async((10,20),eta="utc时间")
# 重试

from celery.beat import crontab
c.conf.beat_schedule={
    "name":{
        "task":"task",
        "schedule": 5,
        "args":(19,20)
    },
    "name1":{
        "task":"task",
        "schedule":crontab(),
        "args":(10,20)
    }
}

1.什么时候用celery? 什么地方用?
2.你怎么用的?
3.为什么要用? 还有别的方式可以实现吗?
4.如果避免celery重复执行任务?
 - 加锁
 - celery_one
锁
	乐观锁
    悲观锁
```

openpyxl

- 写

  ```
  from openpyxl import Workbook
  wb=Workbook()
  wb1=wb.create_sheet("name",index=0)
  wb.title="" 工作簿名称
  wb.active  当前选中的工作簿
  wb1["A3"]=3
  wb1["A4"]="=SUM()"
  wb1.cell(row=3.column=4)=4
  wb1.append([])
  wb.save("name.xlsx")
  ```

- 读

  ```python
  from openpyxl improt load_workbook
  wb=load_workbook("name.xlsx",read_only=True,data_only=True)
  wb1=wb["name"]
  wb1["A3"].value
  wb1.cell(row=3,column=4).value
  wb1.rows  #生成器 for row in,返回的是每行的数据 for c in row
  wb1.columns  #返回的是每列的数据
  wb1.max_row #返回最大的行数
  wb1.max_column #返回最大的列数
  #bug 在写的时候,如果使用了函数,则在读的时候,函数获取到的值是none?
  #避免方式是 修改之后需要手动保存
  ```

  

ip地址