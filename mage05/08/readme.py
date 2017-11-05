create table tbname (
    colname_1 type_1,
    colname_2 type_2,
    ...
    colname_n type_n
) engine=innodb default charset='utf8';


1. url 点击 a
2. views.py method
3. urls.py
4. render templates
5. models

1. 点击submit按钮 url
2. views.py method
    request.GET/POST
    validate 验证
        用户 不能重复
        用户名。密码长度
        年龄
    验证成功，保存，跳转到用户列表
    验证失败，显示添加页面，回显数据
3. urls.py


编辑页面打开
1. url 点击 a ? 编辑谁
    url?username=kk

2. views.py method
    request.GET

3. models -> get user
4. render template


1. 点击submit按钮 url
2. views.py method
    request.GET/POST
    validate 验证
        用户是否存在
        用户 不能重复
        用户名。密码长度
        年龄
    验证成功，保存，跳转到用户列表
    验证失败，显示添加页面，回显数据
3. urls.py

create table user(
    id int primary key auto_increment,
    username varchar(64),
    password varchar(512),
    age int,
    tel varchar(32)
) engine=innodb default charset=utf8;


1. 用户管理 用户添加/修改基本信息（不包含密码）/修改密码（原，新） 验证

2. 用户密码 ==> sql md5
    1. 添加存储为md5
    2. 登录验证MD5
    3. 修改密码
