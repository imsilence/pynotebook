# 复习                 [45分钟]          9:30 - 10:15

# 用户列表显示          [5分钟 + 15分钟]  10:15 - 10:35
# 用户添加              [10分钟 + 40分钟] 10:35 - 11:25

休息10分钟

# 用户修改              [10分钟 + 40分钟] 11: 35 - 12:25
# 用户删除

# 数据库                [5分钟] 13:30 - 13:35

库 database
表 table

sql

库:                      [5 + 15] 13:35 - 13:55
mysql -uroot -p          
show databases;                                        
create database name;                                  
show create database name;
use name;
drop database name;

表                       [5 + 15] 13:55 - 14:15

create table name (                                    
    id int primary key auto_increment,
    name varchar(20),
    password varchar(32),
    age int,
    telephone varchar(11)
) engine=myisam[innodb] default charset=utf8;

show create table name;
desc name;
[5 + 10] 14:15 - 14:30
[5 + 10] 14:30 - 14:45

增                       [5 + 15] 14:15 - 14:30
insert into name values();
insert into name(columns) values()

查询                     [5 + 15] 14:30 - 14:50
select * from name;
select * from name where name='';
select * from name where name='' and password = '';
select id,name,age,telephone from name;

## 休息10分钟 ##
改                       [5 + 15] 15:00 - 15:20

update name                         
set age = '';

update name
set password=md5(1)
where name='';

update name
set name = '',
age = '',
telephone = ''
where id=;

删                       [5 + 10] 15:20 - 15:35
delete from name;
truncate table name;

delete from name where id=1;

drop table name;

##　休息10分钟 ##

## py操作mysql ##

py3rd
pip install MySQL-python [1 + 5] 15:45 - 15:50

使用
import MySQLdb           [5 + 20] 15:50 - 16:15
conn = MySQLdb.connect(host=host,port=port,user=username,passwd=pwd,db=db, char
set=charset)

cur = conn.cursor()
cur.execute(sql, args)

cur.fetchone()
cur.fetchall()
cur.close()
conn.commit()
conn.close()

## 休息 10 分钟 ##

1. 登录功能修改              [5 + 25]    16:25 - 16:45

2. 用户列表展示              [5 + 25]    16:45 - 17:20

3. 更改用户信息              [10 + 35]   17:20 - 18:05

休息10分钟
4. 用户删除
