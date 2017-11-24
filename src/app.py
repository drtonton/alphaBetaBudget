import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


alpha_static_total = raw_input('What is alpha static total?')
beta_static_total = raw_input('What is beta static total?')
pay_per_period = raw_input('What is pay per period?')
