import mysql.connector
mysql=mysql.connector.connect(host="local host",username="root",password="")
mysql=mysql.cursor()
mysql.execute("create database mysql")
result=mysql.execute("show databases")
for x in result
    print(x)
#result=mysql.execute("show tables")
sql="Insert into user(name,password") values(%s,%s,%s)
val=("mahender",)
