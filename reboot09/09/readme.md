# 复习 30 分钟  9:30 - 10:00
# 作业 10 分钟  10:00 - 10:10

#新课程


1. flask-package 10分钟 + 10分钟 10:30 - 10:50
 改写package, views, models
 启动程序manage.py

休息10分钟

2. 开发流程 5分钟 11:00 - 11:05
a.需求收集
b.设计 db, 代码
c.开发
d.测试
e.上线

2. 需求收集 15分钟 11:05 - 11:20
create table machine_room (
    id int primary key auto_increment,
    name varchar(50),
    status int default 0
);

create table asset (
id int primary key auto_increment comment '主键',
sn varchar(50) not null unique key comment 'sn编号',
machine_room_id int comment '机房',
purchase_date datetime comment '购买日期',
warranty_period int comment '保修时间',
vendor varchar(50) comment '生产厂商',
model varchar(50) comment '型号',
cpu int comment 'cpu核数',
ram int comment '内存大小G',
disk int comment '磁盘大小G',
os varchar(50) comment '操作系统',
ip varchar(128) comment 'ip地址',
hostname varchar(50) comment '主机名',
status int default 0 comment '状态,1删除,0正常,2维护'
);

3. 列表展示
  a. 数据获取model 10分钟+15分钟 11:20 - 11:45
  b. 模板继承  10分钟+15分钟  11:45-12:10

  c. layout   5分钟 + 10分钟  13:30 - 13:45
  d. assets.html  5分钟+15分钟 13:45 - 14:05

5. 新建
  title, btn, content
  form
  jquery.find             10 + 10分钟 14:15 - 14:35
  jquery.get+jquery.html  5 + 5 分钟 14:35 - 14:45       
  jquery.load             5分钟 14:45 - 14:50

休息10分钟

  html页面                10分钟 + 15分钟 15:00 - 15:25
  slider                  5分钟  + 10分钟 15:25 - 15:40
  datetimepicker          5分钟  + 10分钟 15:40 - 15:55

  提交数据
  jquery.serializeArray() 5分钟 + 15分钟 15:55 - 16:15

  休息10分钟

  接收数据, 检查, 存储数据库 5分钟 + 10分钟 * 2  16:25 - 16:55

  错误回显
  sweetalert               5分钟 + 10分钟  16:55 - 17:10

休息10分钟

6. 删除
  sweetalert + ajax + 逻辑删除     10分钟 + 10分钟 * 2 17:20 - 18:00
