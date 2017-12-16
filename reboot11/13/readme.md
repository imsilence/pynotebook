#复习               [30分钟] 9:30 - 10:00
#作业               [30分钟] 10:00 - 10:30

休息 10分钟

#新课程
最近一天的日志统计图

1. 准备数据
  时间/lgt/lat        [5分钟] 10:40 - 10:45

  a. maxmind          [10分钟 + 15分钟] 10:45 - 11:10
    georeader = geoip2.database.Reader('/home/woniu/07/11/user/db/GeoLite2-City.mmdb')
    geo = georeader.city(ip)
    geo.country.name
    geo.city.names.get('zh-CN', '')
    geo.location.latitude
    geo.location.longitude

  b. 日志导入       [10分钟 + 20分钟] 11:10 - 11:40  
    time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(line_list[3][1:], '%d/%b/%Y:%H:%M:%S'))
    时间, ip, url, code, status, lat, lgt

  echarts 介绍      [10分钟] 11:40 - 11:50

2.  饼状图
  a. template     [10分钟 + 15分钟] 11:50 - 12:15
  b. views        [5分钟 + 10分钟] 13:30 - 13:45
  c. models       [10分钟 + 25分钟] 13:45 - 14:20

3. 层叠柱状图
  a. template     [10分钟 + 15分钟] 14:20 - 14:45
  b. views        [5分钟 + 10分钟] 14:45 - 14:55

休息10分钟

  c. models       [10分钟 + 25分钟] 15:05 - 15:40

4. 地图
  a. template     [10分钟 + 15分钟] 15:40 - 16:05
  b. views        [5分钟 + 10分钟] 16:05 - 16:20
  c. models       [15分钟 + 30分钟] 16:20 - 17:05

休息10分钟

5. 部署
nginx+uwsgi+flask         [10分钟 + 20分钟] 17:15 - 17:45

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
