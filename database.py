#SQLite is ligt 
import sqlite3
import random
import datetime

#Define SQL commands for creating the tablrd

#Descriptive name and data types to create tables
#CREATING TABLES
sales_table = '''   CREATE TABLE sales (
                    sales_id INTEGER PRIMARY KEY,
                    sale_date DATE,
                    customer_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER,
                    unit_price DECIMAL(10,2),
                    total_price DECIMAL(10,2),
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY (product_id) REFERENCES products(product_id)
                )'''

products_table = '''   CREATE TABLE products (
                        product_id INTEGER PRIMARY KEY,
                        product_name TEXT,
                        unit_cost DECIMAL(10,2)
                        )'''                

customer_table = '''    CREATE TABLE customer  (
                        customer_id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        email TEXT,
                        phone TEXT
                        )'''

#Define SQL commands for inserting sample data int the table
#INSERT DATA
sales_data = '''    INSERT INTO sales(  sale_date,
                                        customer_id,
                                        product_id,
                                        quantity,
                                        unit_price ,
                                        total_price)
                    VALUES( ?,?,?,?,?,?)'''

products_data = '''  INSERT INTO products (  product_name, 
                                            unit_cost)
                    VALUES (?,?)
'''
customer_data = ''' INSERT INTO customer(   first_name,
                                            last_name,
                                            email,
                                            phone)
                    VALUES(?,?,?,?)'''

#Define sample datafor the products and customer table
products = [('Product 1', 50.00),       
            ('Product 2', 25.00),
            ('Product 3', 75.00),
            ('Product 4', 100.00),
            ('Product 5', 125.00)]

customers = [
    ('Zwanele', 'Afikile', 'zafikile@emails.com', '012 345 6789'),
    ('Andelwe', 'Zazik', 'azazikona@emails.com', '023 567 8901'),
    ('Philafuthy', 'ZOnkeizizwe', 'pzonkizizwe.email.com', '034 532 3995'),
    ('Nomthandazo', 'Mbali', 'nmbali@email.com', '045 678 9012'),
    ('Sipho', 'Nkosi', 'snkosi@email.com', '056 789 0123'),
    ('Noluthando', 'Dlamini', 'ndlamini@email.com', '067 890 1234'),
    ('Thabo', 'Molefe', 'tmolefe@email.com', '078 901 2345'),
    ('Lungile', 'Mthembu', 'lmthembu@email.com', '089 012 3456'),
    ('Khanyisile', 'Nkabinde', 'knkabinde@email.com', '090 123 4567'),
    ('Mandla', 'Mkhize', 'mmkhize@email.com', '091 234 5678')
]

#Define the start and end dates for geennrated sales data
start_date = datetime.date(2023,1,1)
end_date = datetime.date(2023, 12, 31)

#COnnect to the database and create the tables
with sqlite3.connect('sales.db') as conn:
    #create sales customer products table
    conn.execute(sales_table)
    conn.execute(products_table)
    conn.execute(customer_table)

    #insert sample data info into the sales table
    for i in range(1000):
        sale_date = start_date + datetime.timedelta(days=random.randint(0, 365))
        customer_id = random.randint(1, len(customers))
        product_id = random.randint(1, len(customers))
        quantity = 10.00  #random.randint(1, 10)
        unit_price = 10.00
        total_price =  quantity * unit_price
        conn.execute(sales_data,(sale_date, customer_id, product_id, quantity, unit_price, total_price))

    for product in products:
        conn.execute(products_data, product)

    for customer in customers:
        conn.execute(customer_data, customer)

#commit the changes
    conn.commit()

    print("Database successfully created")

                



                    
