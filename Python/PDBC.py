import mysql.connector
con=mysql.connector.connect(user='root',password='Manu@1999',host='localhost',database='booksdb')
print(con)
c=con.cursor()
#wapp to create new database BOOKSDB
'''sql='create database booksdb'
c.execute(sql)'''
#wapp to create new table into the database booksdb1
'''c.execute('create table booksdetails(name varchar(20),price decimal)')'''
#wapp to insert into booksdb
'''c.execute('insert into booksdetails values("Java programming",578.40)')
con.commit()'''
#wapp to update name as python for booksdb
'''c.execute('update booksdetails set name="python" where price=561')
con.commit()'''

'''c.execute('update booksdetails set price=600 where name="python" ')
con.commit()'''
#wapp to delete the record from bookbd
c.execute('delete from booksdetails where price=600')
con.commit()
#wapp to select all the rows of table
rows=c.execute('select * from booksdetails')
rows=c.fetchall()
print(rows)

