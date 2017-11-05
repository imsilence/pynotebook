 1. django.forms.Form
    定义了form的属性
        var = IntegerField
        var_b = CharField
    定义了form的方法
        clean, clean_var

    页面打开(create/update)
        view: render(request, template, {form = Form()})
        template: {% form.as_table %} python(django template)
                    var => html
                    as_dict
                        object => dict{key:value}

    填写数据提交
        view: form = Form(request.POST)
              form.is_valid()
                    form.cleaned_data
              else:
                    render(request, template, {form = form})

    功能:
        1. as_table/as_ul/as_p => 生成html代码
        2. 验证

    用途:
        1. form.as_table
        2. <form action>
            <input name="" value="{{form.var.value}}"
        3. ajax <form action>
                <input name="" value=""/>

                jQuery('#input').val(value)



1. 修改密码流程(登陆以后访问的)
    a. 点击修改密码链接/按钮，打开密码表单页面/dialog
        bootstrap modal
        form
        ajax
    b. 提交表单(old_password, password, password2[确认密码])
        ChangePasswordForm
            a
            b
            c
            user 
            clean xxxxx

    c. 接收数据，验证，存储
        Form(request.POST, user=request.user)

        i. old_password(明文)
            当前登陆用户
            request.user(密文)
            request.user.password==old_password 不对
            request.user.check_password(old_password)

            password + password2

        ii. 修改密码
            request.user.set_password(password)
            request.user.save()


GET/POST/DELETE/PUT
入口 验证

dispath
get/post/delete/put
form
form.is_valid


form_valid



def test():
    return 'test'

print(test())

在test函数执行之前和之后运行一块代码
print('before')
print('after')


def test():
    print('before')
    rt = 'test'
    print('after')
    return rt

print(test())


def test_wrapper(func):
    print('before')
    rt = func()
    print('after')
    return rt

rt = test_wrapper(test)

func = test_wrapper(test)

func(a, b)
test2(a, b, c)
test3(a, b, c, d)

def test_wrapper(func):
    def wrapper(*args, **kwargs):
        print('before')
        rt = func(*args, **kwargs)
        print('after')
        return rt
    return wrapper

def test2(a, b)
    print(a, b)
    return a + b




test
View.as_view()

def login_required(func):
    def wrapper(*args, **kwargs):
        if 登陆成功:
            rt = func()
            return rt
        else:
            return HttpReponse("未登陆")

    return wrapper()



所有调用的地方
func = test_wrapper(test)
func()


1. 记录日志
    before
    after

2. 记录执行时间
    stime.
    time.time() - stime

def logging(func):
    def wrapper(*args, **kwargs):
        print('before')
        rt = func(*args, *kwargs)
        print('after')
        return rt

    return wrapper


def timing(func):
    def wrapper(*args, **kwargs):
        print('before')
        rt = func(*args, *kwargs)
        print('after')
        return rt

    return wrapper

@logging
def test():
    time.sleep(2)

@timing
def test2():
    time.sleep(4)


提交请求
browser/a/form
    HttpResponseRedirect('/login/')
ajax
    JsonResponse({
    status : 401
    })


Form(request.POST/GET)
Form(initial=model.as_dict())
Form(request.POST, initial=model.as_dict())
A           A=A1                 A=A2           A=A1
B           B=B1                 B=B2           B=B1
C                                C=C2           C=C2

ModelForm(request.POST, instance=model)



1. 自动保存
    文件保存到哪里去了
2. 手动保存

1. 上传文件
    form enctype="multipart/form-data"
2. 获取文件
    request.FILES

    form()

css/js => static (cdn)
上传的文件 => media(django) 本地

django debug = True
    /static/ => static

    media 不会处理
    nginx/apache

django debug = False
    static
    media 
    都不会处理
    nginx/apahe


1. 用户基本修改做完
2. form formmodel, 上传文件, mixin, 装饰器
3. 收获地址(尝试做下 View)