## django

web框架 socket服务端

功能:

1.收发消息

2.根据不同的路径返回不同的内容

3.动态页面 -  字符串的替换(模板的渲染-jinja2)

### http协议

#### 格式

请求(request)   浏览器发送给服务器的消息

"请求方式 URL路径 协议版本\r\n

k1:v1\r\n

k2:v2\r\n

\r\n

请求体"        ——》 get没有请求体

响应（response）     服务器回给浏览器的消息

"HTTP/1.1 状态码 状态描述\r\n

k1:v1\r\n

k2:v2\r\n

\r\n

响应体（HTML文本）"

#### 请求方式

8种   GET  POST PUT DELETE HEAD OPTIONS TRACE CONNECT

#### 头信息

host   user-agent  content-type  cookie  set-cookie  Location

#### 状态码

1xx   

2xx  200 

3xx   重定向  301  302 

4xx  请求的错误  404    403   402

5xx   服务器的错误   500  502

在浏览器上输入地址后会发生哪些事情?

### 路由

urlconf

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('web.urls')),   # 1.11   2.0   path   re_path
    url(r'^rbac/', include('rbac.urls', namespace='rbac')),
    # url(r'^indx/', index),
]
```

正则表达式

r   ^   $   \d    [0-9]    [a-z]  \w  +  ?  *  {5}

分组和命名分组

从url上捕获参数    ——》 字符串

```python
  url(r'^(uesr)_list/',uesr_list ),            # 捕获参数按照位置传参传递给视图函数
```

```python
  url(r'^(?P<name>uesr)_list/',uesr_list ),    # 捕获参数按照关键字传参传递给视图函数
```

路由分发

include

```Python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('web.urls')),   # 1.11   2.0   path   re_path
    url(r'^rbac/', include('rbac.urls', namespace='rbac')),
]
```

url的命名和反向解析

静态路由

```python 
  url(r'^(uesr)_list/',uesr_list,name='user_list' ),   
```

模板:

{% url 'user_list' %}    _> ' /app01/user_list/'

py文件:

from django.urls import reverse

reverse('user_list')     _> ' /user_list/'

 分组

```python 
  url(r'^edit_uesr/(\d+)/',edit_uesr,name='edit_uesr' ),   
```

模板:

{% url 'edit_uesr'  6  %}    _> ' /app01/edit_uesr/6/'

py文件:

from django.urls import reverse

reverse('edit_uesr',args=(9,))       _> ' /app01/edit_uesr/9/'

 命令分组

```python 
  url(r'^edit_uesr/(?P<pk>\d+)/',edit_uesr,name='edit_uesr' ),   
```

模板:

{% url 'edit_uesr'  6  %}    _> ' /app01/edit_uesr/6/'     #  按照位置传参

{% url 'edit_uesr'  pk=6  %}    _> ' /app01/edit_uesr/6/'     #  按照关键字传参

py文件:

from django.urls import reverse

reverse('edit_uesr',args=(9,))       _> ' /app01/edit_uesr/9/'

reverse('edit_uesr',kwargs={'pk':9})        _> ' /app01/edit_uesr/9/'

namespace

 url(r'^rbac/', include('rbac.urls', namespace='rbac')),

{% url 'rbac:edit_uesr'  6  %}   

reverse('rbac:edit_uesr',args=(9,))     

namespace1:namespace2:name

### 视图 view

MVC 

​	M: model  

​	V: view  视图  HTML文本

​	C: controller  控制器

MTV

​	M: model  ORM

​	T: template  模板 HTML文本

​	V: view 视图  业务逻辑 FBV CBV 

逻辑  接收一个请求返回一个响应

FBV CBV 

请求 request

```Python
request.method  请求方式  8种   GET POST 
request.GET   url上携带的参数
request.POST  POST发送的数据   name=alex&id=2   "{k1:v1}"
request.body  请求数据 请求体 
request.FILES  上传的文件   enctype="multipart/form-data" 
request.META   请求头的信息  HTTP_ 全大写  - _> _
request.path_info  路径信息   不包含IP和端口  不包含参数
request.COOKIES  cookie
request.session  session

request.get_full_path()    路径信息   不包含IP和端口  包含参数
request.is_ajax()      是否是ajax请求
request.is_secure()    http false   https 
```

响应 response

```python 
HttpResponse('字符串')   _>  '字符串'    content-type:'text/html'    
render(request,'模板的文件名',{k1:v1})      返回一个完整的HTML页面
redirect('地址')     重定向   Location:地址
JsonResponse({})     content-type:'application/json'
TemplateResponse(request,'模板的文件名',{k1:v1})
```

CBV

定义:

```python
from django.views import View

class AddPublisher(View):
      	
     def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch( request, *args, **kwargs)
        return ret
    
    def get(self,request,*args,**kwargs):
        # 处理get请求的逻辑
        self.request
        return reponse
    
    def post(self,request,*args,**kwargs):
        # 处理post请求的逻辑
        return reponse
```

使用:

```python
url(r'add_publisher',AddPublisher.as_view())
url(r'add_publisher',view)
```

加装饰器

```
from django.utils.decorators import method_decorator
```

1.加在方法上

```python
@method_decorator(timer)
def get(self,request,*args,**kwargs):
```

2.加在dispatch方法上

```python
@method_decorator(timer)
def dispatch(self, request, *args, **kwargs):
    ret = super().dispatch( request, *args, **kwargs)
    return ret

@method_decorator(timer,name='dispatch')
class AddPublisher(View):
```

3.加在类上

```python
@method_decorator(timer,name='post')
@method_decorator(timer,name='get')
class AddPublisher(View):
```

注意点:

```
from django.views.decorators.csrf import csrf_exempt,csrf_protect
```

csrf_exempt只能加在dispatch上才能生效

### 模板

{{  }}   变量   {%  %}  tag  逻辑相关 

render(request,'模板的文件名',{k1:v1})     

{{  k1  }}    {{  request  }}   

. 索引  key  属性 方法                 key >  属性 方法 > 索引    

过滤器

{{ 变量|过滤器  }}  {{ 变量|过滤器:参数  }}   {{ 变量|过滤器:参数|过滤器  }}

default:'nothing'    date:'Y-m-d H:i:s'( Y-m-d H:M:S  )  safe  

join   add  + 

标签 tag 

{%  for i in list %}

​	{{  i }}    {{ forloop.counter }}     parentloop单前循环的外层循环

{% endfor %}

{% if 条件 %}    不支持算数运算   if  1|add:1 >=2     不支持连续判断    if  10 > 5 > 1 

​	xxx

{% elif 条件 %}

{% else %}

{% endif %}



{% csrf_token %}   一个隐藏的input标签   name='csrfmiddlewaretoken'    值 是64长度    csrftoken cookie

静态文件

```
STATIC_URL = '/static/'
```

{% load static %}

{% static  '静态文件的相对路径' %}

{% get_static_prefix %}   _>  '/static/'

母板和继承

母板:

1. 提取多个页面的公共部分 _>  html文件中  base.html
2. 在HTML中定义 block块

继承:

	1. {% extends 'base.html' %}
 	2. 重写block块

注意点:

	1. {% extends 'base.html' %} 写在第一行  上面不要有内容
 	2. {% extends 'base.html' %}    'base.html'   带引号  base.html 当做变量   {% extends  name  %}
 	3.  要显示的内容写在block块中
 	4.  多定义 block块     css  js 

组件  include

一小段HTML代码段  _>  nav.html

{%  include 'nav.html' %}

3个自定义的方法:

filter  simple_tag   inclusion_tag

步骤:

1. 在已注册app下创建一个名为templatetags的Python包

2. 在Python包下创建py文件   ->   my_tags.py

3. 在py文件中写代码:

   ```python
   from django.template import Library
   register = Library()
   
   
   from django import template
   register = template.Library()
   ```

4. 写函数  + 加装饰器

   ```Python
   @register.filter
   def addxx(value,arg):  # 过滤器最多有两个参数
       return 任意值
   
@register.simple_tag
   def join_str(*args,**kwargs):  # 过滤器最多有两个参数
       return 任意值
   
   @register.inclusion_tag('模板的文件名')
   def show_li(num):
       return {'num':range(1,num+1)}
   	
   ```
   
   写模板
   
   ```html
   {% for i in num %}
   	{{ i }}
   {% endfor%}
   ```
   
5. 使用

   ```html
   {% load my_tags %}
   {{ 'xx'|addxx:'111' }}   _>  任意值     if 变量|addxx
   
   {% join_str 'xx' '11' k1=v1 k2=v2  %}
   
   
   {% show_li  3 %}  1 2 3 
   ```

### ORM

对象和关系型数据库的一种映射

对应关系:

类   _ >   表

对象  _>  数据行(记录)

属性 _>  字段



参数:

null    数据库可以为空  

blank   form表单填写可以为空

verbose_name   中文提示

default  默认值

unique   唯一

choices=((1,'xxx'),())

命令

python manage.py  makemigrations 

python manage.py  migrate 

必知必会13条

返回queryset

all 

filter  

exclude 

values()    [{}]

values_list()    [()]

order_by()    -   

reverse()    

distinct()  

返回对象

get()

first()

last()

返回布尔值

exists  

返回数字

count

单表的双下划线

__gt

__lt 

__gte

__lte

__in = []

__range= [1,10]

__contains   like 

__icontains

__startswith 

__endswith

__isnull =Ture

外键的操作

```Python 

class Publisher(models.Model):
    name = models.CharField(max_length=32)

    
class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher')    # pub_id
```

基于对象的查询

正向查询

book_obj.pub    _>  出版社的对象

反向查询

pub_obj.book_set ( 类名小写_set)

pub_obj.book_set.all()

指定related_name='books'

pub_obj.books.all()

基于字段

Book.objects.filter(pub__name='xxxxx')



Publisher.objects.filter(book__title='xxxx')

指定related_name='books'

Publisher.objects.filter(books__title='xxxx')

多对多的操作

```Python
class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)  # pub_id


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')
```

author_obj.books

book_obj.author_set

方法

all

add(1,2,3,4)  add(对象,对象)

remove(id)   remove(对象)

clear()

set([id,id])  set([对象,对象])    设置多对多的关系

author_obj.books.create()

book_obj.author_set.create()

聚合和分组

```
from django.db.models import Max,Min,Avg,Sum,Count

Author.objects.aggregate(max=Max('age'))   ——》  {‘max':86}

Author.objects.annotate(Count('books'))
Book.objects.values('author').annotate(count=Count('id')).values('author','count')
```

F和Q

filter(pinglun__gt=F('shoucang'))

update(pinglun=F('pinglun')+2)

|    &   ~

Q(pinglun__gt=1)  

Q(('pinglun__gt',1)   

q = Q()

q.connector  = 'OR' 

q.children.append(Q(('pinglun__gt',1)  )

q.children.append(Q(('pinglun__lt',2)  )

事务:

```Python
from django.db import transaction


with transaction.atomic():
    
    # 一系列操作

    Author.objects.create()
```

行级锁 + 事务:

```
from django.db import transaction


with transaction.atomic():

    # 一系列操作

    Author.objects.filter().select_for_update()  # 加上行级锁
    
```

### 中间件

在django全局范围内处理django的请求和响应的钩子

5 种 4个特征

1执行时间 2 参数  3 执行顺序 4 返回值

```python 
from django.utils.deprecation import MiddlewareMixin
class xx(MiddlewareMixin):
    
    def process_request(self,request)
    
    def process_view(self,request,view_func,args,kwargs)
    
    def process_response(self,request,response)
    
    def process_exception(self,request,exception):
        
    def process_template_response(self,request,response)
   
```

### cookie session

django中操作cookie

设置:

​	response.set_cookie(key,value,max-age=5)

   response.set_signed_cookie(key,value,max-age=5,salt='xxx')

获取

​	request.COOKIES.get()

​    request.get_signed_cookie(key,salt='xxx',default=None)

删除

​	response.delete_cookie(key)



request.session[key] =v 

request.session[key]   request.session.get()

### ajax

$.ajax({

​	url :

   headers {' x-csrftoken  '}

​	type:

​	processData:false

​    content-type:false

​	data: 

​	success:

​	error:

})

### form  modelform modelformset

```
{{ form.non_field_errors }}   __all__的错误
```

 

