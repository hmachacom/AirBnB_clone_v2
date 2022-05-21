#!/usr/bin/env bash
#Prepare your web servers

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/shared/

mkdir -p /data/web_static/releases/test/

sudo chown -hR ubuntu:ubuntu /data

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

sudo service nginx restart

