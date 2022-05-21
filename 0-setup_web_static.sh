#!/usr/bin/env bash
#:::::::::::::::

sudo mkdir -p /data/web_static/shared/

sudo mkdir -p /data/web_static/releases/test/

sudo chown -R ubuntu:ubuntu /data/

echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

