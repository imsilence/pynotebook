# 复习 [60分钟] 9:30 - 10:30
# 作业 [20分钟] 10:30 - 10:50

休息10 分钟

# datapicker[10分钟+15分钟]

# sweetalert [15分钟 + 25分钟] 11:00 - 11:40
修改成功/失败后提示
删除提示

# BootstrapValidator 10分钟 + 15分钟 11:40 - 12:05

# cpu, 内存, 磁盘监控

1. 设计                                     [15 分钟] 13:30 - 13:45

create table monitor(
id bigint primary key auto_increment,
ip varchar(128),
cpu int not null,
mem int not null,
ctime datetime,
) engine = innodb default charset=utf8;

2. restapi                                 [10分钟] 13:45 - 14:55
3. 服务端提供接口存储                        [10分钟 + 20分钟] 13:55 - 14:25

休息10分钟

4. 监控脚本                                 [20分钟 + 30分钟] 13:35 - 15:25

内存/proc/meminfo
MemTotal:        1020584 kB
MemFree:          107744 kB
Buffers:          123276 kB
Cached:           424256 kB

psutil.virtual_memory()
psutil.cpu_precent()
psutil.net_if_addrs()

<ip:time:cpu,mem>

6. 调用restapi提交数据                      [5 + 10] 15:25 - 15:40
requests
s = requests.post('http://localhost:9002/monitors/', data = {'ip' : 111, 'time' : 'xxx', 'cpu' : 1, 'mem' : 1})

休息 10 分钟

7. web展示                                  [30 + 90] 15:50  - 17:50
显示数据highcharts

休息10分钟

8. flask-package [10分钟 + 20分钟] 18:00 - 18:30
改写package, views, models
启动程序manage.py

9. 异常 [5分钟 + 15分钟] 18:30 - 18:50
      try except finally
      rasie BaseException('Error')

10. 上传文件
      enctype=multipart/form-data
      request.files.get()
      filename,save
