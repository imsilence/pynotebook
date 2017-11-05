1. 用户登录
    a. 打开页面/dialog
    b. 提交数据
        ajax
    c. django接收数据，验证
        User(username, password), UserExt(status)
        user = authenticate(username, password)
            user = User.objects.get(username = username)
            user.check_password(password)
        i. 成功
            user.userext.status == 1

            login(request, user)

            ???
        ii. 失败
            返回提示信息json

2. 用户退出
    /account/logout/
    get
        logout(request)
        redirect(/)



userext
validkey exprie_time 1小时/1天
1. validkey_create_time
2. valid
    a. 超过一天
       重新激活

用户登录认证
    1. username&password, email&password
    方法:
        方法一:
            a. backend
            b. settings = [ModelBackend, SelfBackend]
                ==> username&password
                ==>self email & password
        方法二:
            a. authenticate
                不调用，自己写


密码重置:
    1. 发送 validkey
        a. 打开页面，填 email username FormView Form, get form.as_table
        b. 提交表单， 验证 username email是否匹配 post form.clean status==1
        d. 跳转到首页，提示发送重置邮件，请打开邮件。进行密码重置
    2. 重置密码
        a. 打开链接 username, validkey，打开页面
        b. username(hidden), validkey(hideen), 填写新密码, 新密码确认
        c. 认证username validkey匹配 validkey != '' status==1
        d. 修改密码

        注册了，我没激活，我就是吧用户名，密码忘记了(客服)
                        只用email + 验证码



userext
validkey exprie_time 1小时/1天
用户注册、用户重置密码
1. validkey_create_time
2. valid
    a. 超过一天
       重新激活

修改密码
