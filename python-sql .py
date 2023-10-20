import sqlite3
import csv
conn= sqlite3.connect("Test_Eastvtg1.db")
c= conn.cursor()

def crt_table():
    c.execute("""create table IF NOT EXISTS sales(salesid integer not null primary key,customerid integer not null)""")
    c.execute("""create table IF NOT EXISTS Customer(age integer not null,customerid integer not null primary key)""")
    c.execute("""create table IF NOT EXISTS Orders(orderid integer not null,salesid integer not null,item_id integer not null,quantity integer )""")
    c.execute("""create table IF NOT EXISTS Item(item_id integer not null primary key,item_name varchar(50) not null)""")


    


def view_table():
    c.execute("""create  view IF NOT EXISTS myTable as select Customer.customerid as Customer,Age,item_name as Item,quantity as Quantity from Customer join sales on Customer.customerid=sales.customerid
    join Orders on Orders.salesid =  sales.salesid
    join Item on Orders.item_id=Item.item_id
    """)
    


def final_table():
    data = c.execute("""select Customer,Age, Item, sum(quantity) as Qnty from myTable
    where (age>=18 and age<=35) and quantity>0
    group by Customer, Age, Item
    order by Customer""")




    
    
crt_table()
view_table()      
final_table()


c.close()
conn.close()
    