#connectionimport mysql.connectormydb = mysql.connector.connect(  host="localhost",  user="root",  passwd="root123")mycursor = mydb.cursor()mycursor.execute("show databases")lst = mycursor.fetchall()if ('payrollsyste',) in lst:  print("Database is Successfully Created")else:  mycursor.execute("CREATE DATABASE payrollsyste")  mycursor.execute("USE payrollsyste")  mycursor.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER(10), fname VARCHAR(45), lname VARCHAR(45), email VARCHAR(45), salary INTEGER(10))")  print("Database is Successfully Created")