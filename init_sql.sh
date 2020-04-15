sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'sasha'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'sasha'@'localhost' = PASSWORD('sasha')"
mysql -uroot -e "CREATE DATABASE dbname"
mysql -uroot -e "GRANT ALL ON dbname.* TO 'sasha'@'localhost'"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate