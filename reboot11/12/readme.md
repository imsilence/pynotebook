# 复习 [60分钟] 9:30 - 10:30
# 作业 [30分钟] 10:30 - 11:00

休息10 分钟

## 上课内容 ##

1. paramiko/fabic
执行命令                             [10分钟 + 20分钟] 11:10 - 11:40
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

上传文件                             [10分钟 + 20分钟] 11:40 - 12:10

2. 面向对象

基本概念                             [5分钟] 13:30 - 13:35
封装
继承
多态=>python不支持(鸭子类型，具有鸭子特性，就认为是鸭子)

封装                                 [15 + 30分钟]  13:35 - 14:20
将一类事物的属性和方法组织起来，对外隐藏内部信息, 只对外提供可信的数据和方法
class
类的定义
对象=>类实例化
构造函数
属性 => 类的属性, 对象的属性
方法 => 类的方法, 对象的方法
#静态方法         
#私有属性和方法


+ 改写 User                              [10分钟 + 20分钟] 14:20 - 14:50
登录验证 classmethod                        

休息10分钟

获取用户列表 classmethod                 [10分钟 + 20分钟] 15:00 - 15:30
用户装载 classmethod                     [5分钟+10分钟] 15:30 - 15:45
用户验证+保存 objectmethod               [15分钟 + 30分钟] 15:40 - 16:30
用户查看 classmethod                     [10分钟 + 20分钟] 16:30 - 17:00

休息10分钟

用户验证+更新 objectmethod               [15分钟 + 30分钟] 17:10 - 17：55
用户删除 classmethod                     [5分钟+ 10分钟] 17:55 - 18:10


继承                                    [15分钟 + 20分钟] 18:10 - 18:45
super(CHILD, self).__init__()
PARENT.__init__(self)
