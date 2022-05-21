#!/usr/bin/env bash
#Prepare your web servers

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/

sudo mkdir -p /data/web_static/releases/test/

sudo chown -R ubuntu:ubuntu /data/

sudo echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

