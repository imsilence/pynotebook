## 上课内容 ##

0. 百度/google/自己积累
1. pip install
2. import
3. help, dir, 官方手册
4. 使用

hashlib                                [5分钟 + 10分钟] 11:45 - 12:00
    hashlib.md5()
    md5.update()
    mkd.hexdigest()

os                                     [10分钟 + 15分钟] 12:00 - 12:25
    os.mkdir
    os.makedirs
    os.unlink
    os.getuid
    os.getgid
    os.getpid
    os.getppid
    os.listdir
    os.walk
    os.stat

    os.path.*
    os.path.exists
    os.path.dirname
    os.path.basename
    os.path.isfile/isdir/islink
    os.path.join
    os.path.abspath
    os.path.normpth


    os.system => rt
    os.popen => output (file) read/readlines/readline/foreach close

sys                                     [5分钟 + 10分钟] 13:30 - 13:45
    sys.args
    sys.exit
    sys.exit(n)
    c int => 4个字节
    n2 => 512
    n << 8 => 512
    512 >> 8 => n

argparse                                   [15分钟] 13:45 - 14:00 
    parser = argparse.ArgumentParser()    
    parser.add_argument('-H', '--host', help='host', type=str, default='str')
    parser.add_argument('-P', '--port', help='port', type=int)
    parser.add_argument('-u', '--user', help='user', type=str)
    parser.add_argument('-p', '--pwd', help='pwd', type=str)
    parser.add_argument('-c', '--cmd', help='cmd', type=str, nargs='+')

    # 解析参数
    args = parser.parse_args()

    # 默认参数
    port = args.port or 22

getpass
    


time                                     [10分钟 + 15分钟] 13:45 - 14:10
    time.time unix
    time.localtime unix => stuct
    time.mktime struct => unix
    time.strptime str=>time
    time.strftime time=>str


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


threading                                  [15分钟] 14:00 - 14:15
    threading.Thread
    s.setDaemon()
    s.start()

    thread.Lock
    l.acquire()
    l.release()


redis

key: del, ttl, expire, type
string: set, get, strlen, mget, set, incr, decr
list: lpush, lpop, rpush, rpop, lrange, llen
     队列，栈
hash: hset, hget, hmset, hmget, hgetall, hdel
set: sadd, srem, SMEMBERS, scard, sdiff, sunion, SINTER, SPOP
zset: zadd, zrange, zrem, ZREVRANGE

作业
1. 资产管理
    sn,ip,hostname, mac, addr, admin, use

    增、删、改、查
    执行命令dialog => username, password, commands => 显示执行结果