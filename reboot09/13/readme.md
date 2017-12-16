#复习               [30分钟] 9:30 - 10:00
#作业               [10分钟] 10:00 - 10:10
#新课程

1. 准备数据
  时间/lgt/lat        [10分钟] 10:10 - 10:20
  a. maxmind          [10分钟 + 15分钟] 10:20 - 10:45
    georeader = geoip2.database.Reader('/home/woniu/07/11/user/db/GeoLite2-City.mmdb')
    geo = georeader.city(ip)
    geo.country.name
    geo.city.names.get('zh-CN', '')
    geo.location.latitude
    geo.location.longitude

休息 10分钟

  b. 日志导入       [30分钟] 10:55 - 11:25  
    time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(line_list[3][1:], '%d/%b/%Y:%H:%M:%S'))
    时间, ip, url, code, status, lat, lgt

  echarts 介绍      [10分钟] 11:25 - 11:35

2.  饼状图
  a. template     [10分钟 + 15分钟] 11:35 - 12:00
  b. views        [5分钟 + 5分钟] 13:30 - 13:40
  c. models       [10分钟 + 15分钟] 13:40 - 14:10

3. 层叠柱状图
  a. template     [10分钟 + 15分钟] 14:10 - 14:35
  b. views        [5分钟 + 5分钟] 14:35 - 14:45

休息10分钟

  c. models       [10分钟 + 20分钟] 14:55 - 15:25

4. 地图
  a. template     [10分钟 + 15分钟] 15:35 - 15:45
  b. views        [5分钟 + 5分钟] 15:45 - 15:55
  c. models       [15分钟 + 25分钟] 15:55 - 16:35

休息10分钟

5. 部署
nginx+uwsgi+flask         [10分钟 + 20分钟] 16:45 - 17:15

安装nginx
安装uwsgi

server {
    listen       9998 default_server;
    server_name  _;

    access_log  logs/cmdb.access.log  main;
    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        include uwsgi_params;
        uwsgi_pass unix:/tmp/cmdb.sock;
        #uwsgi_pass 127.0.0.1:9999;
    }   
}

uwsgi -s 0.0.0.0:9999 -w views:app
uwsgi -s /tmp/cmdb.sock -w views:app --chmod

6. blueprint            [20分钟 + 40分钟] 17:15 - 18:15
