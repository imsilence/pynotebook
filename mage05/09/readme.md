import traceback
try

    return
except BaseException as e:
    print(e)
    print(traceback.format_exc())

except

finally


if

elif

elif


else


在登录以后，如果访问用户登录页面或者登录url，自动跳转到用户列表页面

浏览器 -> 服务端(Views.py => Models.py => Templates)


render(request, tpl, {key:value})

key => str/int
{{key}}

key = {'a' : '', 'b':''}

{{key.a}}


key = ['a', 'b']

{{key.0}

request.sesion.user = {'username' : ''}
request.session.user.username

request.sesion.user = 'xxxx'
request.sesion.user


MySQLConnection

__init__(host, port, uesr, password, db)

实例的私有的属性, host, port, user, password, db, charset
conn, cur

创建连接的方法, 私有的方法
    如果已经创建连接，就不再创建

关闭连接的方法，公有方法

execute_fetch(self, sql,args=None, one=False)
execute_commit(self, sql, args=None)
    创建链接
    执行
    返回结果

增、删、改、差 => 类中的方法

构造函数将table row => class对象
sql => 类的属性

__init__(self, table columns):
    self.colnum_name
    self.column_name_2


增   save() ==> 实例的函数
    __init__ => object
    object.save()
    insert

删   delete() => 实例的方法
    id => find => object
    object.delete()

改   modify() => 实例的函数
    id => find => object
    object.column = value
    object.modify()
    update

    id =>

查
    find_by_id(id) => object => 类的方法
    find_all() = [] object => 类的方法


User(username='a', age=29, tel='xxxx')

line = {'username' : 'a', 'age':29, 'tel' : 'xxx'}

User(username=line['username'], xxxxx)
User(**line)
