user  {user};
worker_processes  {worker_processes};

error_log  {error_log};

pid        {pid};


events {{
    worker_connections  {worker_connections};
}}


http {{
    include       mime.types;
    default_type  text/html;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  {access_log}  main;

    sendfile        on;
    keepalive_timeout  65;

    gzip  on;

    server {{
        listen       {listen};
        server_name  {server_name};

        charset utf-8;

        location / {{
            root   html;
            index  index.html index.htm;
            proxy_pass   {proxy_pass};
        }}

    }}
}}
