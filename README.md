# BusBookingApp

PYTHON MODULES USED:
flask(pip install flask)
mysql-connect-python(pip install mysql-connect-python)

TO RUN THE PYTHON PROGRAM:
python3 busapp.py

mysql Database name - busApp

mysql> show tables;
+------------------+
| Tables_in_busapp |
+------------------+
| buses            |
| login            |
+------------------+
2 rows in set (0.01 sec)

mysql> desc buses;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| source      | varchar(50) | YES  |     | NULL    |       |
| destination | varchar(50) | YES  |     | NULL    |       |
| avail       | int         | YES  |     | NULL    |       |
| price       | float       | YES  |     | NULL    |       |
| date        | date        | YES  |     | NULL    |       |
| busid       | int         | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> select * from buses;
+-----------+-------------+-------+-------+------------+-------+
| source    | destination | avail | price | date       | busid |
+-----------+-------------+-------+-------+------------+-------+
| Chennai   | Hyderabad   |     5 |  2000 | 2022-03-14 |     1 |
| Chennai   | Bengaluru   |     5 |  2000 | 2022-04-17 |     2 |
| Hyderabad | Bengaluru   |     5 |  2000 | 2022-04-17 |     3 |
+-----------+-------------+-------+-------+------------+-------+
3 rows in set (0.00 sec)


mysql> desc login;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| email    | varchar(50) | YES  |     | NULL    |       |
| password | varchar(50) | YES  |     | NULL    |       |
| name     | varchar(50) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)


mysql> select * from login;
+--------------+----------+--------+
| email        | password | name   |
+--------------+----------+--------+
| user@gm.com  | pass     | Harika |
| user1@gm.com | pass     | Hannah |
+--------------+----------+--------+
2 rows in set (0.00 sec)

