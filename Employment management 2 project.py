import mysql.connector as mys

def menu():
    while True:
        print("....Menu....")
        print("1. Create Database")
        print("2. Show Databases")
        print("3. Create Table")
        print("4. Show Tables")
        print("5. Insert Record")
        print("6. Update Record")
        print("7. Delete Record")
        print("8. Search Record")
        print("9. Display Record")
        print("10. EXIT")
        choice = int(input("Enter the choice (1-10): "))
        if choice == 1:
            create_database()
        elif choice == 2:
            show_databases()
        elif choice == 3:
            create_table()
        elif choice == 4:
            show_tables()
        elif choice == 5:
            insert_record()
        elif choice == 6:
            update_record()
        elif choice == 7:
            delete_record()
        elif choice == 8:
            search_record()
        elif choice == 9:
            display_record()
        elif choice == 10:
            break
        else:
            print("Wrong Choice.")
        input("Press Enter Key to continue.....")

def create_database():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123')
        if mycon.is_connected():
            print("Successfully Connected")
            cur = mycon.cursor()
            cur.execute('CREATE DATABASE IF NOT EXISTS db2')
            print("Database Created")
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def show_databases():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123')
        if mycon.is_connected():
            cur = mycon.cursor()
            cur.execute('SHOW DATABASES')
            for db in cur:
                print(db[0])
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def create_table():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123', database='db2')
        if mycon.is_connected():
            cur = mycon.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS db2(empid INT PRIMARY KEY, ename VARCHAR(255), salary FLOAT)')
            print("Table Created -> db2")
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def show_tables():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123', database='db2')
        if mycon.is_connected():
            cur = mycon.cursor()
            cur.execute('SHOW TABLES')
            for table in cur:
                print(table[0])
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def insert_record():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123', database='db2')
        if mycon.is_connected():
            cur = mycon.cursor()
            ID = int(input("Enter Employee ID: "))
            Name = input("Enter Name of Employee: ")
            Salary = float(input("Enter Employee Salary: "))
            query = "INSERT INTO db2(empid, ename, salary) VALUES (%s, %s, %s)"
            cur.execute(query, (ID, Name, Salary))
            mycon.commit()
            print('Record Inserted')
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def update_record():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123', database='db2')
        if mycon.is_connected():
            cur = mycon.cursor()
            d = int(input("Enter Employee ID for updating record: "))
            ID = int(input("Enter New Employee ID: "))
            Name = input("Enter New Name Of Employee: ")
            Salary = float(input("Enter New salary for Employee: "))
            query = "UPDATE db2 SET empid=%s, ename=%s, salary=%s WHERE empid=%s"
            cur.execute(query, (ID, Name, Salary, d))
            mycon.commit()
            print('Record Updated')
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def delete_record():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123', database='db2')
        if mycon.is_connected():
            cur = mycon.cursor()
            d = int(input("Enter Employee ID for deleting record: "))
            query = 'DELETE FROM db2 WHERE empid=%s'
            cur.execute(query, (d,))
            mycon.commit()
            print("Record Deleted")
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def search_record():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123', database='db2')
        if mycon.is_connected():
            cur = mycon.cursor()
            print("Enter The Choice according to you want to search Record:")
            print("1. According To ID")
            print("2. According To Name")
            print("3. According To Salary")
            choice = int(input("Enter the choice (1-3): "))
            if choice == 1:
                d = int(input("Enter Employee ID which you want to search: "))
                query = "SELECT * FROM db2 WHERE empid=%s"
            elif choice == 2:
                name = input("Enter Employee Name which you want to search: ")
                query = "SELECT * FROM db2 WHERE ename=%s"
            elif choice == 3:
                sal = float(input("Enter Employee Salary which you want to search: "))
                query = "SELECT * FROM db2 WHERE salary=%s"
            else:
                print("Wrong Choice")
                return

            cur.execute(query, (d if choice == 1 else (name if choice == 2 else sal),))
            rec = cur.fetchall()
            count = cur.rowcount
            print("Total no. of records found:", count)
            for i in rec:
                print(i)
            print("Record Searched")
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

def display_record():
    try:
        mycon = mys.connect(host='localhost', user='root', passwd='9990418622@123', database='db2')
        if mycon.is_connected():
            cur = mycon.cursor()
            cur.execute('SELECT * FROM db2')
            rec = cur.fetchall()
            count = cur.rowcount
            print("Total Record is:", count)
            if count != 0:
                for i in rec:
                    print(i)
            else:
                print("NO record found")
            mycon.close()
    except mys.Error as err:
        print("Error:", err)

# -----Main-------
menu()
