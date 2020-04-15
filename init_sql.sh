sudo /etc/init.d/mysql start
mysql -uroot -e "create database dbname;"
mysql -uroot -e "grant all privileges on dbname.* to 'sasha'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate