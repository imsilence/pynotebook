用户管理

1. 用户登录
    用户登录页面显示
    用户登录信息提交
2. 用户列表展示
3. 用户的添加
    用户表单显示
        /user/create_user
        render(request, tpl)

    用户信息提交存储
        /user/save_user/
            1. 检查
               检查成功以后，存储， 跳转到用户列表
               检查失败，render(request, tpl, {user, error})

4. 用户修改
    用户信息显示 /user/view_user/?name=kk
        models->name获取用户的信息
        render(request, 'user/edit.html', {user : user})
        <input type="hidden" name="name" value={{user.name}},
        <input type="password" name="password" value=""
        <input type="text" name="age" />
        <input type="text" name="tel" />
        <input type="submit" value=""/>
    用户信息提交存储
        /user/modify/
5. 用户删除

代码编写
1. 创建app
2. 用户登录页面显示
    /user/reqirelogin/
    a. views.py
        requirelogin
        打开登录页面 render()
    b. login.html
    c. urls.py
3. 用户数据提交
    /user/login/
    a 登录失败



4. 用户列表展示
    /user/list/
    models->用户信息
    user/list.html

create table message1(
    username varchar(256),
    title varchar(512),
    content text,
    publish_date datetime   
) engine=innodb default charset=utf8;

create table message2(
    username varchar(256) NOT NULL DEFAULT 'kk',
    title varchar(512) NOT NULL DEFAULT '',
    content text,
    publish_date datetime   
) engine=innodb default charset=utf8;

create table message3(
    id int primary key auto_increment,
    username varchar(256) NOT NULL DEFAULT 'kk',
    title varchar(512) NOT NULL DEFAULT '',
    content text,
    publish_date datetime   
) engine=innodb default charset=utf8;



create table accesslog(
    id int primary key auto_increment,
    log_date datetime,
    ip varchar(256),
    url text,
    status int
) engine=innodb default charset=utf8;

insert into accesslog (log_date, ip, url, status) values('2016-10-11 12:00:00', '5.5.5.5', '/index.html', 200);
insert into accesslog (log_date, ip, url, status) values('2016-10-11 12:00:00', '5.5.5.5', '/index.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.5.5', '/index.html', 500)
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.7.5', '/index.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.5.5', '/index.html', 500);
insert into accesslog (log_date, ip, url, status) values('2017-05-11 12:00:00', '5.7.5.5', '/index1.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-06-11 12:00:00', '5.7.5.5', '/index.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-09-11 12:00:00', '5.7.5.5', '/index.html', 400);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.7.5', '/index2.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.5.75', '/index.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.57.5', '/index2.html', 400);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.7.5', '/index2.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.5.5', '/index3.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.7.5.5', '/index2.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-08-11 12:00:00', '5.5.7.5', '/index1.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-09-11 12:00:00', '5.5.7.5', '/index.html', 400);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.7.5', '/index4.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-12-11 12:00:00', '7.5.5.5', '/index3.html', 200);
insert into accesslog (log_date, ip, url, status) values('2017-11-11 12:00:00', '5.5.5.5', '/index2.html', 400);
insert into accesslog (log_date, ip, url, status) values('2017-10-11 12:00:00', '5.5.5.5', '/index1.html', 400);
