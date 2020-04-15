sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'sasha'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'sasha'@'localhost' = PASSWORD('sasha')"
mysql -uroot -e "CREATE DATABASE dbname"
mysql -uroot -e "GRANT ALL ON dbname.* TO 'sasha'@'localhost'"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate