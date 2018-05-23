'''
Create a database which includes books, CDs, and small kitchen appliances. All
of the products have the following information associated with them:
a) Product name
b) Short description
c) SKU (stock keeping unit)
d) Product dimensions
e) Shipping weight
f) Average customer review score
g) Standard price to customer
h) Cost of product from supplier

Populate your database with data as much as you can and answer the following
questions:
1. What is the average number of products bought by each customer?
2. What is the range of number of products purchased by customers (that is, the
lowest number to the highest number of products purchased)?
3. What are the top 20 most popular products by customer state?
4. What is the average value of sales by customer state (that is, Standard price to
customer – Cost of product from supplier)?
5. How many of each type of product were sold in the last 30 days?
Create a GUI based application which should have provision to insert your data into
database and show the results of your queries.
'''

import tkinter as tk

window = tk.Tk()

window.title("Advanced Database Assignment 2")

window.geometry("700x700")

# Labels
title = tk.Label(text="Hello World. Welcome to Advanced Databases: Assignment 2!", font=("Times New Roman",16))
title.grid(column=0,row=0)

activity1 = tk.Label(text="Insert into Database", font=("Times New Roman",20))
activity1.grid(column=0,row=1)

# Pair-wise for label and field
# field 1
insert_1 = tk.Label(text = "Product Name: ")
insert_1.grid(column=0, row = 2)

entry_field1 = tk.Entry()
entry_field1.grid(column=1,row=2)

# field 2
insert_2 = tk.Label(text = "Short Description: ")
insert_2.grid(column=0, row = 3)

entry_field2 = tk.Entry()
entry_field2.grid(column=1,row=3)

# field 3
insert_3 = tk.Label(text = "Stock keeping Unit: ")
insert_3.grid(column=0, row = 4)

entry_field3 = tk.Entry()
entry_field3.grid(column=1,row=4)

# field 4
insert_4 = tk.Label(text = "Product Dimension: ")
insert_4.grid(column=0, row = 5)

entry_field4 = tk.Entry()
entry_field4.grid(column=1,row=5)

#field 5
insert_5 = tk.Label(text = "Shipping Weight: ")
insert_5.grid(column=0, row = 6)

entry_field5 = tk.Entry()
entry_field5.grid(column=1,row=6)

#field 6
insert_6 = tk.Label(text = "Average Customer Review Score: ")
insert_6.grid(column=0, row = 7)

entry_field6 = tk.Entry()
entry_field6.grid(column=1,row=7)

#field 7
insert_7 = tk.Label(text = "Standard Price to Customer: ")
insert_7.grid(column=0, row = 8)

entry_field7 = tk.Entry()
entry_field7.grid(column=1,row=8)

#field 8
insert_8 = tk.Label(text = "Cost of Product from supplier: ")
insert_8.grid(column=0, row = 9)

entry_field8= tk.Entry()
entry_field8.grid(column=1,row=9)

# Button for Inserting data to DB
insert_button = tk.Button(text="\nInsert into DB!\n")
insert_button.grid()

# Labels
activity2 = tk.Label(text="Query from Database", font=("Times New Roman",20))
activity2.grid(column=0,row=11)

label = tk.Label(text="Enter to query from MongoDB: ")
label.grid(column = 0, row = 12)

entry_field3 = tk.Entry()
entry_field3.grid(column=1,row=12)

# Button for Querying data from DB
query_button = tk.Button(text="\nQuery from DB!\n")
query_button.grid()

label1 = tk.Label(text="Result for the above query is...")
label1.grid(column = 0, row = 15)

text_field = tk.Text(master=window, height=10, width=30)
text_field.grid(column = 0, row=16)




# Continuous loop
window.mainloop()
