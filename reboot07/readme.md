# 复习 #

1. 封装                               [10分钟] 9:30 - 9:40
属性, 方法
类属性, 对象的属性
私有, 共有


类的方法, 对象的方法, 静态方法

2. 继承                               [10分钟] 9:40 - 9:50
重写父类函数
子类调用父类函数
super(XXX, cls/self).XXX()

3. js控件                             [10分钟] 9:50 - 10:00              
sweetalert
datatables
bootstrapvalidator

## 上课内容 ##

os                                     [15分钟] 10:00 - 10:15
    os.system
    os.listdir
    os.mkdir
    os.makedirs
    os.path.***

sys                                     [15分钟] 10:10 - 10:30
    sys.stdout
    sys.stdin
    sys.stderr
    sys.args
    sys.exit

time                                     [15分钟] 10:30 - 10:45
    time.time unix
    time.localtime unix => stuct
    time.mktime struct => unix
    time.strptime str=>time
    time.strftime time=>str

logging+traceback                         [15分钟] 10:45 - 11:00
    logging.basicConfig(level=logging.DEBUG, filemode="a", format='%(asctime)s - %(name)s - %(levelname)s:%(message)s', filename="e:/t.txt")
    logging.debug
    logging.info
    llogging.error
    traceback.format_exc()


hashlib                                     [15分钟] 11:00 - 11:15
    hashlib.md5()
    md5.update()
    mkd.hexdigest()

paramiko/fabic                             [15分钟] 11:15 - 11:30
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("某IP地址",22,"用户名", "口令")
stdin, stdout, stderr = ssh.exec_command("你的命令")
print stdout.readlines()
ssh.close()

ssh = paramiko.SSHClient()
pkey=ssh.RSAKey.from_private_key_file(filename, pwd)
ssh.load_system_host_keys()
ssh.connect("某IP地址",22,"用户名", pkey=pkey)
stdin, stdout, stderr = ssh.exec_command("你的命令")
print stdout.readlines()
ssh.close()

http://www.cnblogs.com/xia520pi/p/3805043.html


argparse                                   [15分钟] 11:30 - 11:45
    parser = argparse.ArgumentParser()    
    parser.add_argument('-H', '--host', help='host', type=str)
    parser.add_argument('-P', '--port', help='port', type=int)
    parser.add_argument('-u', '--user', help='user', type=str)
    parser.add_argument('-p', '--pwd', help='pwd', type=str)
    parser.add_argument('-c', '--cmd', help='cmd', type=str, nargs='+')

    # 解析参数
    args = parser.parse_args()

    # 默认参数
    port = args.port or 22

getpass

# cpu, 内存, 磁盘监控

1. 设计                                     [15 分钟] 13:30 - 13:45

create table monitor(
id bigint primary key auto_increment,
cpu int not null,
mem int not null,
ctime datetime not null,
) engine = innodb default charset=utf8;

2. restapi                                 [10] 13:45 - 14:55
3. 服务端提供接口存储                        [10 + 20] 13:55 - 14:25

休息10分钟

4. 监控脚本                                 [20 + 30] 13:35 - 15:25

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
s = requests.post('http://localhost:9002/3a/api/users/', data = {'uid' : 111, 'name' : 'xxx'})

休息 10 分钟

5. web展示                                  [30 + 60] 15:10  - 18:00
highcharts

爬虫                                        [20 + 45] 18:00 - 19:00
#pyquery
