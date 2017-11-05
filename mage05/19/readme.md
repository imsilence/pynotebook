1. 问题
    黄豆
        a. 目前知识太零散
            原因:
                python: 5 节课
                        聚焦 ==> python基本语法

                web: 从 6 节课开始
                        mysql
                        django -> mvc
                        html
                        css
                        js
                        面向对象
                    (流程开发 MVC)
                        m => Model => ORM
                        urls.py
                        v => View/ListView/FormView/CreateView/DetailView/DetailView/UpdateView/DeleteView
                        form => Form/ModelForm
                        t => if for {{}} extends load staticfiles

                        admin

            结论（解决方法）
                1. 后面只是不是像前5节课学习python专注，更多以流程驱动
                2. web知识多，整理
                3. 流程的练习（看、想、写）


        b. 继承问题
            面向过程 ==> 面向对象
            View代码继承问题
                熟练(知道<->不知道)
                1.整理: mm A->B(func)
                         -> func
                2.View/FormView/ListView
                    原理 ==> Python知识


    小智
        a. django权限控制没讲，还有其他的内容没讲
            (知道<->不知道)
            ==> django
            好处 => 快速学会，用起来
                    深度,         用(只能用在上课联系项目
                                    后续自己的功能不知道怎么开发
                                    给一个新的知识点、技术 ==> 自己的钻研
                                        )
            RABC ==>
            授课 ==> 自学

            碰到问题：
                1. 解决问题的能力
                    a. 问题搞清楚
                        报错
                    b. 百度、google、bing搜索
                    c. 请教其他人（讨论）

        b. 不能灵活运用
            1. 知识点用途的理解(知识点==>解决的问题)
            2. 写的少
                自主

    程龙
        a. 复制、粘贴 ==> 慢一些

from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('before')
        rt = func(*args, **kwargs)
        print('after')
        return rt
    return wrapper

def test(n):
    print(n)
    return n * 2


test_wrapper = login_required(test)
test_wrapper(2)


@login_required
def test1(n):
    print(n)
    return n * 2


def timeing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        rt = func(*args, **kwargs)
        total = time.time() - s
        print(total)
        return rt
    return wrapper


class A(object):
    attr_a = 'A'
    attr_comm = 'attr_comm_a'
    def func_a(self):
        print('func_a')
    def func_comm(self):
        print('func_comm_a')

class B(object):
    attr_b = 'B'
    attr_comm = 'attr_comm_b'
    def func_b(self):
        print('func_b')
    def func_comm(self):
        print('func_comm_b')

class E(A):
    def func_a(self):
        super().func_a()
        print('func_a_c')

c = E();
c.attr_a, c.attr_comm => A, attr_comm_a
c.func_a(), c.func_comm => func_a_c, func_comm_a

class C(A):
    pass

c = C();
c.attr_a, c.attr_comm => A, attr_comm_a
c.func_a(), c.func_comm => func_a, func_comm_a

class D(B, A):
c.attr_a, c.attr_comm(B), c.attr_b
c.func_a(), c.func_comm()(B), c.func_b() 

B super().func_comm() A


类扩展已有的类

Mixin 
不进行实例化

A(Mixin, Base)
Mixin.func => Base.func
Mixin.func 
    super().func()   ==> Base.func


用户收获地址

打开收获地址页面
1. url
2. view
    View ==> ListView
        属性:
            model
            template_name
            context_object_name
        方法:
            get_context_data


    models ==> ORM
        UserAddress
            User ==> 1: N
            name
            addr
            telephone
            fixedphone
            email
            status 

3. template

新增:
FormView
CreateView

1. 点击新增按钮 ==> 打开form页面
    GET
    urls.py
    views.py
        form_class
    
2. 点击保存按钮
    POST
    urls.py
    views.py
        form_class()
        form.valid()
            obj = form.save(commit=False)
            obj.save()

    form

删除:
DeleteView
model
1. 确认删除吗？
    confirm/sweetalert

    GET useraddress/delete/1/
        pk = 1

        pk => object  ==> get_object()

        html => 确认删除xxx
                object

        <form method="post" action="useraddress/delete/1/">
        确认

2. 发起请求
    urls.py
        pk = 1
    view.py
        id
        models.object.get(pk=id)            get_object()

        obj.status = 1
        obj.save()
        跳转到用户收获地址页面


3. 更新
    a. 发起请求获取表单页面(填值)
        get pk=>
        object = get_object()
        form = form(data={}, instance=object)
        object, form

    b. 点击保存按钮
    POST
    urls.py
    views.py
        get pk=>
        form_class()
        form.valid()
            obj = form.save(commit=False)
            obj.save()



2017年8月12日作业:
1. 整理今天上课内容完成
     createview/listview/updateview/deleteview
2. 用户数据权限
    listview/updateview/deleteview
    filter(user=request.user)/  object.user == request.user
3. 上课代码写完

4. 【加分】
    ajax, sweetalert, datatable, bootstrap-modal 
    ajax提交数据
    datatable局部刷新
    添加，修改用bootstrap-modal
    提示用sweetalert