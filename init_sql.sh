sudo /etc/init.d/mysql start
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'sasha'@'localhost' IDENTIFIED BY 'sasha';"
mysql -u sasha -p
sasha
CREATE DATABASE dbname;
