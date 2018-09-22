''' Lab Question is as follows:
Create a database in your script folder. In this database create a table called ‘words’ having columns : word, count.
Now read a sentence from the keyboard. From this sentence get all the words and save the words along with their count in this table.

Query the table and display all the words along with their counts in sorted order of frequency.

'''

import sqlite3

conn = sqlite3.connect('mydbs.db')

def create_table():
    conn.execute("create table words(word text not null,count int not null);")

def insert_into_table(table_name,word,count):
    conn.execute("insert into words values(\"{}\",{});".format(word,int(count)))
    conn.commit()

def query_into_table(table_name):
    cursor = conn.execute("select * from {};".format(table_name)) # returns a tuple
    l=list()
    for row in cursor:
        l.append(row)
    fuck =(sorted(l,key=lambda x:x[1]))
    for rows in fuck:
        print(rows)

# Main Program Proceeds
table_name = "words"
'''
create_table()
s = input("Enter the string:\n")
l = s.split()
for a in set(l):
    word = a
    count = l.count(a)
    insert_into_table(table_name,word,count)
'''

query_into_table(table_name)

conn.close()
