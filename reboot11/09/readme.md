# 复习 [30 分钟]  9:30 - 10:00
# 作业 [10 分钟]  10:00 - 10:10

#新课程

1. flask-package [10分钟 + 10分钟] 10:30 - 10:50
改写package, views, models
启动程序manage.py

休息10分钟

2. 开发流程 [5分钟] 11:00 - 11:05
a.需求收集
b.设计 db, 代码
c.开发
d.测试
e.上线

2. 需求收集 [15分钟] 11:05 - 11:20
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
  a. 数据获取model [10分钟+15分钟] 11:20 - 11:45
  b. assets.html  [5分钟+15分钟] 11:45 - 12:05
  ajax请求数据

4. 新建   [15分钟 + 25分钟] 13:30 - 14:10
  title, btn, content
  form

5. slider [5分钟  + 20分钟] 14:10 - 14:35
6. datetimepicker [5分钟  + 20分钟] 14:35 - 15:00

休息10分钟

7. 提交数据
  jquery.serializeArray() [5分钟 + 10分钟] 15:00 - 15:15

8. 接收数据, 检查, 存储数据库 [10分钟 + 20分钟] 15:15 - 15:45

9. 错误回显
  sweetalert [5分钟 + 10分钟]  15:45 - 16:00
  ajax刷新table

休息10分钟

10. 编辑
    编辑框 [10 + 20分钟] 16:10 - 16:40
    编辑框数据回显 [10 + 20分钟] 16:40 - 17:10

休息 10分钟

11. 删除
  sweetalert + ajax + 逻辑删除 10分钟 + 20分钟  17:20 - 17:50
  ajax刷新table


12. 异常 [10 + 20] 17:50 - 18:20
      try except finally
      rasie BaseException('Error')

13. 上传文件 [20分钟] 18:20 - 16:40
      enctype=multipart/form-data
      request.files.get()
      filename,save
