#5.create SQlite database and perform operations on tables.

import sqlite3
con=sqlite3.connect("bcab.db")
c=con.cursor()
try:
    c.execute("""create table student12(
    id integer,
    name text,
    course text)""")
except:
    c.execute('drop table student12')
    print('table dropped')
    c.execute("""create table student12(
        id integer,
        name text,
        course text)""")
c.execute("insert into student12 values(1,'a','bca')")
c.execute("insert into student12 values(2,'b','bca')")
c.execute("update student12 set course='bsc' where id=2 ")
c.execute("delete  from student12 where id=1")
c.execute("select *from student12")
print(c.fetchall())

con.commit()
con.close()
con.close()