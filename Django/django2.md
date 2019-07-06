django-debug-toolbar

<https://www.cnblogs.com/maple-shaw/articles/7808910.html>

缓存

- 开发调试
- 内存
- 文件
- 数据库
- Memcache缓存（python-memcached模块）
- Memcache缓存（pylibmc模块）

<https://django-redis-chs.readthedocs.io/zh_CN/latest/>

作为 cache backend 

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

 将 django-redis 作为 session 储存

```
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```

信号

新增数据的数据的时候写一条日志

ORM性能

1. 能用values() 就用vallues()
2. select_related    连表查询    # 一对一  一对多
3. prefetch_related    子查询   # 多对多
4. only    defer    

多个数据库

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    },

}
```

迁移

python manage.py migrate --database db2

读写分离

手动

```
obj = models.Student.objects.using('default').get(pk=5)
models.Student.objects.using('db2').create(name='alex',classes_id=1)

obj.save(using='db2')

```

自动

settings配置

```
DATABASE_ROUTERS = ['myrouter.Router']
```

```
class Router:
    def db_for_read(self, model, **kwargs):
        return 'default'

    def db_for_write(self, model, **kwargs):
        return 'db2'
```

一主多从

```
class Router:
    """
    一主多从
    """

    def db_for_read(self, model, **kwargs):
        return random.choice(['db1', 'db2', 'db3'])

    def db_for_write(self, model, **kwargs):
        return 'default'
```

分库分表

```Python
class Router:
    """
    分库分表
    app01  default
    app02  db2
    """

    def db_for_read(self, model, **kwargs):

        if model._meta.app_label == 'app01':
            return 'default'
        elif model._meta.app_label == 'app02':
            return 'db2'

    def db_for_write(self, model, **kwargs):
        if model._meta.app_label == 'app01':
            return 'default'
        elif model._meta.app_label == 'app02':
            return 'db2'
```

crm+权限

### crm

客户关系管理系统    

销售人员增多  客户增多  提高工作效率

#### 功能

- 销售
  - 客户管理     - 公户和私户
  - 跟进记录
  - 报名表
  - 缴费管理
- 班主任
  - 班级管理
  - 课程管理
  - 学习记录管理

#### 公户和私户

避免销售抢单

3天一跟进 20天成单

私户的上限  150  200 

有没有现成的crm?    学邦   

#### 为什么不用现成?非要自己开发?

定制化程度更高  加需求要收费

权限组件

rbac  

#### 怎么实现权限的控制?

url  代表一个权限 

表结构

4个model  6个表

#### 流程

1. 中间件

   request.path_info

   request.current_menu_id  = None

   request.breadcrumb_list = [ { title:首页  url :index } ]

   白名单

   ​	re   settings 

   登录的校验

   免认证

   权限的校验

   ​	pid   id  

   ​	有pid    当前访问的是子权限

   ​		request.current_menu_id   =  pid 	

   

   ​		request.breadcrumb_list .append( {   title: permission_dict [str(pid)] [title]    }  )

   ​		request.breadcrumb_list .append( {   title: permission_dict [pname] [title]    }  )

   

   ​		request.breadcrumb_list .append( {title:i['title'],url:i[url]}  )

   ​	没有pid    当前访问的是父权限   二级菜单

   ​		request.current_menu_id   =  id 

   ​    	request.breadcrumb_list .append( {title:i['title'],url:i[url]}  )

2. 登录

   登录成功后权限信息的初识化

   ​	根据用户获取当前用户的权限信息

   ​	跨表    去空   去重

   ​	构建数据结构

   ​	权限的结构

   ​		简单的权限控制

   ​		permission_list = [ {url:   }  ]

   ​		非菜单权限的归属

   ​        permission_list = [ {url  id  pid    }  ]

   ​		路径导航

   ​		permission_dict ={

   ​						id : {url  id  pid  title  }

   ​		}

   ​	    权限控制到按钮级别

   ​		permission_dict ={

   ​						name : {url  id  pid  title  pname }

   ​		}

   

   ​	菜单的结构

   ​		一级菜单

   ​		menu_list = [   { title  url  }  ]

   ​		二级菜单

   ​		menu_dict = {

   ​					一级菜单的id : {  

   ​								name: 

   ​								icon:

   ​								children:    [   

   ​										{  title    url    }

   ​								]

   ​					  } 

   

   ​			} 

   ​		非菜单权限的归属

   ​			menu_dict = {

   ​					一级菜单的id : {  

   ​								name: 

   ​								icon:

   ​								children:    [   

   ​										{  title    url   id   }

   ​								]

   ​					  } 

   ​			} 

   ​	权限和菜单的数据结构 _> session 

3. 动态菜单

   inclusion_tag  

   一级菜单  一次循环

   class = active     

   二级菜单   二次循环

   if  request.current_menu_id   ==  id 

   ​	一级菜单的class =  hide 

   ​	二级菜单的 class = active     

4. 路径导航

   inclusion_tag  

   一次循环   request.breadcrumb_list 

5. 权限控制到按钮级别

   if   name  in  permission_dict:

   filter 

   

简单的权限控制

```Python
class Permission(models.Model):
    url = models.CharField(max_length=108)


class Role(models.Model):
    name = models.CharField(max_length=32)
    permissions = models.ManyToManyField(Permission)


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    role = models.ManyToManyField(Role)
```

```
# 动态的一级菜单
class Permission(models.Model):
    url = models.CharField(max_length=108)
    title = models.CharField(max_length=32)
    is_menu = models.BooleanField(default=False)


class Role(models.Model):
    name = models.CharField(max_length=32)
    permissions = models.ManyToManyField(Permission)


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    role = models.ManyToManyField(Role)
```

```python
# 动态的二级菜单

class Menu(models.Model):
    """一级菜单"""
    name = models.CharField(max_length=32)
    icon = models.CharField(max_length=108)


class Permission(models.Model):
    """
    有menu_id   二级菜单
    没有menu_id   普通权限
    """
    url = models.CharField(max_length=108)
    title = models.CharField(max_length=32)
    menu = models.ForeignKey(Menu,blank=True,null=True)


class Role(models.Model):
    name = models.CharField(max_length=32)
    permissions = models.ManyToManyField(Permission)


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    role = models.ManyToManyField(Role)
```

#### 权限变化之后,重新登录才能应用权限? 不重新登录就能应用新的权限?

权限变化之后去修改session中用户的权限

改表结构   用户表   + 字段  session_key

```python
from django.contrib.sessions.models import Session
# print(request.session,type(request.session))
ret = Session.objects.get(session_key='4v71np5wwpubili5cfg3si7epkz1zs25')
# print(ret.session_data)

ret = request.session.decode(ret.session_data)
# print(ret)

ret = request.session.encode(ret)
print(ret)
```

权限如何控制到行级别?

![1561463831833](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1561463831833.png)

开发中遇到了什么问题(影响深刻)?

json序列化

表结构的变化

需求的取舍

