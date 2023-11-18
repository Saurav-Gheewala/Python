import mysql.connector
db = mysql.connector.connect(user='root',password='',host='localhost',database='student')
def create_table():
    my_cursor = db.cursor()
    Query = "CREATE TABLE student_details(name VARCHAR(255), roll INT(10), class INT(10))"
    my_cursor.execute(Query)
def insert_data(name,roll,class_name):    
    my_cursor = db.cursor()
    Query = "INSERT INTO student_details(name,roll,class) VALUES(%s,%s,%s)"
    value = (name,roll,class_name)
    my_cursor.execute(Query,value)
    db.commit()
def read_data_featchone():
    my_cursor = db.cursor()
    Query = "SELECT * FROM student_details"
    my_cursor.execute(Query)
    db_read_featchone = my_cursor.fetchone()
    for x in db_read_featchone:
        print(x)
def read_data_featchall():
    my_cursor = db.cursor()
    Query = "SELECT * FROM student_details"
    my_cursor.execute(Query)
    db_read_featchall = my_cursor.fetchall()
    for i in db_read_featchall:
        print(i)
def delete_data():
    my_cursor = db.cursor()
    Query = "DELETE FROM student_details WHERE name= 'Saurav'"
    my_cursor.execute(Query)
def update_data(roll,name):
    my_cursor = db.cursor()
    Query = "UPDATE student_details SET name = %s WHERE roll = %s"
    data = (name,roll)
    my_cursor.execute(Query,data)
    db.commit()
def delete_data(roll):
    my_cursor = db.cursor()
    Query = "DELETE FROM student_details WHERE roll = %s"
    data = (roll,)
    my_cursor.execute(Query,data)
    db.commit()
while True:
    print("1. Create")
    print("2. raed")
    print("3. Update")
    print("4. Dalete")
    print("5. Exit")
    number  = int(input("Enter Your Choice: "))       
    if(number == 1):
        no = int(input("How Many Data You Want To Insert: "))
        while no > 0:
            name = input("Enter Name: ")
            roll_num = int(input("Enter Your Roll No: "))
            class_no = int(input("Enter Your Class: "))
            insert_data(name,roll_num,class_no)
            no = no - 1
    elif number == 2:
        read_data_featchall()  
    elif number == 3:
            roll = (int(input("At Which Roll Number You Want To Change The Name: ")))
            name = input("Enter New Name: ")
            update_data(roll,name)
    elif number == 4:
        no = (int(input("At Whiich Number You Want To Delete The Entry: ")))
        delete_data(no)
    elif number == 5:
        print("See You Later")
        break
