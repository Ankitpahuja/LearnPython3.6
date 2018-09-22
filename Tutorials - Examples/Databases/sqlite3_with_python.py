# This is a sample program that will help get connected to a sqlite database and let you understand queries. 



# That is how you import sqlite module that is in-built with python3.6
import sqlite3

conn = sqlite3.connect('mydb.db') #mydb is the name of your database

# The next line is one time, so we can avoid making a function for it.
def create_table(table_name):
    conn.execute('''Create table {}(RollNo int not null,Name text not null,Age int not null);'''.format(table_name))

def insert_into_table(roll,Name,Age):
    conn.execute("insert into student values({},\"{}\",{});".format(int(roll),Name,int(Age)))
    conn.commit()

def query_in_table(query):
    cursor = conn.execute(query) #returns a tuple
    for row in cursor:
        print(row)

def update_table():
    conn.execute("update student set Age=21 where Age=22;")
    conn.commit()

def delete_from_table():
    conn.execute("delete from student where Age=20;")
    conn.commit()

def drop_table():
    conn.execute("drop table student;")
    conn.commit()

# Main program Proceeds

#create_table("student")
insert_into_table(3,"Archit",22)
query_in_table("select * from student;")
#update_table()
#delete_from_table()
#drop_table()

conn.close()
