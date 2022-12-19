
from db_con import *
import mysql.connector


def main_menu():

    men_in = input("\nPlease choose a number from the menu:"
                   "\n 1- Add a new employee. \n"
                   " 2- Update employee information. \n"
                   " 3- Manage the employees’ payroll (deduct and increase the salary). \n"
                   " 4- Delete an employee record. \n"
                   " 5- Display employee record. \n"
                   " 6- Display all records.\n"
                   " 0- Exit \n"
                   " Your choice is: ")

    try:
        if int(men_in) > 6 or int(men_in) < 0:
            print("Please Enter a Valid Input ")
            main_menu()

        if men_in == "1":
            add_employee()

        if men_in == "2":
            update_employee_record()

        if men_in == "3":
            manage_employee_payroll()

        if men_in == "4":
            delete_employee_record()

        if men_in == "5":
            display_employee_record()

        if men_in == "6":
            display_all_records()

        if men_in == "0":
            exit()

    except ValueError:
        print("Please Enter a Valid Input ")
        main_menu()



def add_employee(): #raghad
    import mysql.connector
    print("**************************** Add Employee **************************** ")
    First_name = input("Enter the employee's First Name : ")
    Last_name = input("Enter the employee's Last Name : ")
    Id = int(input("Enter the employee's ID : "))
    salary = int(input("Enter the employee's Salary : "))
    email = input("Enter the employee's Email : ")
    mycursor.execute("USE payrollsyste")
    sql = "INSERT INTO employee (id, fname,lname,email,salary) VALUES (%s, %s,%s, %s, %s)"
    val = (Id,First_name,Last_name,email,salary)
    mycursor.execute(sql,val)
    mydb.commit()

    main_menu()



def update_employee_record():
    print("**************************** Update Employee Record **************************** ")
    id_update = int(input("Please enter the id of the employee that you want to update: "))
    First_name = input("Enter the updated employee's First Name : ")
    Last_name = input("Enter the updated employee's Last Name : ")
    Id = int(input("Enter the updated employee's ID : "))
    salary = int(input("Enter updated the employee's Salary : "))
    email = input("Enter the updated employee's Email : ")
    mycursor.execute("""
    UPDATE employee
    SET id=%s, fname=%s,lname=%s,email=%s,salary=%s
     WHERE id = %s
     """,(Id, First_name,Last_name,email,salary,id_update))
    mydb.commit()

    main_menu()

def manage_employee_payroll(): #samirah
    print("**************************** Manage Employee Payroll **************************** ")
    import manage_employee_payroll as m
    m.update_salary()
    main_menu()

def delete_employee_record(): #reema
    print("**************************** Delete Employee Record  **************************** ")
    id_del = int(input("Please enter the id of the employee that you want to delete: "))
    sql_del = "DELETE FROM employee WHERE id = %s"
    mycursor.execute(sql_del,(id_del,))
    mydb.commit()

    main_menu()

def display_employee_record(): #raghad
    print("**************************** Display Employee Record  **************************** ")
    employee_ID= input("Please enter the ID: ")
    mycursor.execute("USE payrollsyste")
    mycursor.execute("SELECT * FROM employee WHERE id = %s",(employee_ID,) )
    results = mycursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("Record is not exist...")

    main_menu()


def display_all_records(): #samirah
    print("**************************** Display Employee Records  **************************** ")
    mycursor.execute("SELECT * FROM employee where id =%s")
    result = mycursor.fetchall()
    for row in result:
        print(row)

    main_menu()
