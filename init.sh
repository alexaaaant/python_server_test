sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo gunicorn --bind='0.0.0.0:8080' hello:app
sudo /etc/init.d/nginx restart