1. 模板继承
    解决的问题: template模板的代码复用
                python script.py =>
                        相同代码抽象成函数, 过程(函数体)和数据(函数参数)

                html1, html2, html3 大量代码和页面结构相同
                    解释一:
                        规范(模板)  ==> 函数体
                        block块     ==> 函数参数

                        调用
                            {% extends tpl %}
                            {% block %}{% endblock %}

                    解释二:
                        str.format =>格式化的
                        nginx.tpl => ngxin.conf

                        'i am {name}'.format(name='kk')

    解析引擎
        {{ var }}
        {% tag %}
        {{ var|filter }}

        tag, filter => python 函数
        flask => jinja2
        django => djangotemplate


    需要调整功能(加功能)， 改一份 改多份(考虑放成一份， 代码复用)
        高内聚，低耦合


2. template url name
    name  => url

    urls.py 为每一条url映射 name='' namespace(project urls):name(app urls)唯一的
    name app template: project namespace

    urlpatterns =

    [a, 'a']
    [b, 'b']

    {key: value} {'a' : a, 'b' : b} => url


    A => urls.py
        urlpatterns = [
            'urla' => 'a'
            'urlb' => 'b'
        ]
    B => urls.py
        urlpatterns = [
            'urla' => 'a'
            'urlb' => 'b'
        ]
    django
        urlpatterns = [
            urla' => 'A:a'
            'urlb' => 'A:b'
            urla' => 'B:a'
            'urlb' => 'B:b'
        ]

        urlmaps = {
            'A:a' => 'urla'
            'A:b' => 'urlb'

            'B:a' => 'urla'
            'B:a' => 'urla'
        }

        def url(name):
            return urlmpas.get(name, '')

3. jQuery
    选择器
        document.getElementById()
        .click =
        .addListener
        ajax => ActiveXObject
                XMLHttpRequest
    ajax: get post
        异步的js和xml
        async javascript xml
        浏览器 地址栏, form, a
            提交数据响应的结果影响页面一部分内容
            1. 响应结果太多，网络带宽太小
            2. 等整个页面刷新完成, 才能干别的

        浏览器实现异步方式, 提供js api

    图表替换  => js/jquery img src
                           class jQuey addClass/removeClass

4. django form
    as_table, as_ul, as_p
    面向过程 => request.GET.get('')
               request.POST.get('')
    <form >
        <input name
        textare
        input checkbox
    </form>

    类FORM
        属性 => str

    展示：
        Form.as_p =>字符串
        object => as_dict {}


    提交数据
        name => value
        get, post

    __str__
    print

5. django views代码
    Views

6. class
    封装 => 隐藏信息，提供有权限访问的接口访问数据
    继承 => 代码复用 (多继承)
    组合 => 代码复用
        Door
        Wheel
        Car
            door = []
            wheel =

    has a => 组合
    is a => 继承

7. django admin
    用户端(前端)
    管理端(后端) admin
        1. 是否展示
        2. 显示成什么样子
        3. 能进行哪些操作
            增、删、改、查（验证）
        4. 用户，权限(auth)
            3A, 4A
            认证，授权，审计,（用户）
            授权
                纵(功能, 操作): RBAC 你能进行什么操作(框架)
                    用户=》增，删除，修改，查看
                    角色
                横(数据): 哪些数据


python <=> Django(用python写的) 框架（程序集，python写的一堆函数）
框架 => 提供了代码结构，功能框架，约束内部自定义的实现

js <=> jQuery(用js写的) 库(程序集，js写的一堆函数)
库 => 由库写功能，你想实现什么功能，组合库


60% => 以前学的东西组合
20% => 新知识
20% => 业务逻辑


swal("title", "subject")
swal("title", "subject", "type")
swal({})

on(, function(event/?) {

})


1. 要什么参数就传什么参数
function test(a, b, c) {
    console.log(arguments);
    console.log(a);
    console.log(b);
    console.log(c);
}

2. js 函数是不能设置默认值
undefined

function test(a, b, c) {
    if(type(a) == 'undefined') {
        a = 1;
    }
    //三目表达式
    a ? b : c
    console.log(a);
    console.log(b);
    console.log(c);
}


function test(a) {
    console.log(a ? a : 1);
}

function test(a) {
    console.log(a || 1);
}

c = a && b
    true  return b
    false

c = a || b
    true
    false return b


订单状态转换
已下单
已发货
取消
已收货


<table>
    <tr>1, name, desc, price ...</tr>
    <tr>2, </tr>
    <tr>3, </tr>
</table>
电脑
衣服
食品


扩展表
<tr>1, key, value, 1/0</tr>

<tr>1, 厂商, DELL, 1/0</tr>
<tr>1, 毛重, 10, 1/0</tr>
<tr>1, 毛重1, 10, 1/0</tr>


1. 自定义
2. django
    匹配程度 => 一样 用
               不一样 用 扩展(如何扩展)
    如果想扩展User类
        继承
        1. AbstructUser MyUser
        2. 验证体系
            User
        3. settings配置
            AUTH_USER_MODEL='app.models.MyUser'

        组合
        UserExt id
            User id 1对1


        A
            1, kk, 29

        B
            1, 北京， 185***8

        1. A B
            1, N    ==> 1对多     分类  商品
            1, 1    ==> 1对1     用户   用户扩展表
            M, N    ==> 多对多     书   作者


创建用户:
    m = Model()
    m.attr = value
    m.save()

    Model.objects.create()

    User.objects.create_user()

    from django.contrib.auth.models import User

    u = User.objects.create_user('kk', '786725806@qq.com', '123456')


    class UserExt(models.Model):
        user = models.OneToOneField(User)
        realname = models.CharField(max_length=64)
        birthday = models.DateField()
        nickname = models.CharField(max_length=64)
        avatar = models.CharField(max_length=256)
        telephone = models.CharField(max_length=32)
        score = models.IntegerField(default=0)
        logintime = models.DateTimeField()
        validkey = models.CharField(max_length=256)
        status = models.IntegerField(default=0)

    validkey 随机生成
        os.urandom(32)
        md5()

import datetime
birday = datetime.date(1988, 10, 19)
from django.utils import timezone

uext = UserExt.object.create(user=u, realname='kk', birthday=birday, nickname='kk', avatar='kk', telephone='185', logintime=timezone.now(), validkey=validkey)



1. 用户注册
    Dialog+ajax+sweetalert + (自己尝试)Form
        验证成功，请登录注册邮箱进行账号激活
        验证失败，error 提示

    status:int, errors:{key: [], key: []}, result: {}
    200 正确
    401 未登录
    400 请求错误

2. 整理6 django-> 现在学习的内容
