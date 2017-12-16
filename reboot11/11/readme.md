# 复习 [60分钟] 9:30 - 10:30
# 作业 [30分钟] 10:30 - 11:00

休息10 分钟

## 上课内容 ##

定时刷新                                [10分钟 + 25分钟] 11:10 - 11:45
setInterval
clearInterval
dialog close


hashlib                                [5分钟 + 10分钟] 11:45 - 12:00
    hashlib.md5()
    md5.update()
    mkd.hexdigest()

os                                     [10分钟 + 15分钟] 12:00 - 12:25
    os.system
    os.popen
    os.listdir
    os.mkdir
    os.makedirs
    os.path.***

sys                                     [5分钟 + 10分钟] 13:30 - 13:45
    sys.args
    sys.exit

time                                     [10分钟 + 15分钟] 13:45 - 14:10
    time.time unix
    time.localtime unix => stuct
    time.mktime struct => unix
    time.strptime str=>time
    time.strftime time=>str

异常 [5分钟]
  try except finally
  rasie BaseException('Error')

logging+traceback                         [10分钟 + 20分钟] 14:10 - 14:40
    logging.basicConfig(level=logging.DEBUG, filemode="a", format='%(asctime)s - %(name)s - %(levelname)s:%(message)s', filename="e:/t.txt")
    logging.debug
    logging.info
    llogging.error
    traceback.format_exc()

paramiko/fabic                             [10分钟 + 15分钟] 14:40 - 15:05
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

getpass                                    [5分钟+5分钟] 15:05 - 15:15

休息10分钟

# cpu, 内存, 磁盘监控告警

5分钟内出现3次利用率大于>80%则告警

设计                                     [5 分钟] 15:25 - 15:30

create table alert(
id bigint primary key auto_increment,
ip varchar(128),
type int,
message text,
status int,
admin varchar(64),
ctime datetime not null,
) engine = innodb default charset=utf8;


统计                                      [10分钟 + 15分钟] 15:30 - 15:55

告警判断                                  [10分钟 + 15分钟]15:55 - 16:20

告警存储                                  [5分钟 + 10分钟] 16:20- 16:35

发送邮件                                  [10分钟+20分钟] 16:35 - 17:05

休息10分钟

告警展示                                   [20分钟 + 10分钟 + 10分钟] 17:15 - 18:00

# 上传文件                                 [10分钟 + 20分钟] 18:00 - 18:30
      enctype=multipart/form-data
      request.files.get()
      filename,save
