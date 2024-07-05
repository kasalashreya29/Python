import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
#cur.execute("create table if not exists student(name varchar(50),roll_no varchar(50),section varchar(50)")
#cur.execute('insert into structure values("rajesh","101")')
#cur.execute('insert into structure values("ramesh","102")')
#cur.execute('insert into structure values("raju","103")')
cur.execute('delete from students where name="rajesh" ')
x=cur.execute('select *from students')
print(x.fetchall())
#x=cur.execute("show tables")
con.commit()
print(x)





