def datea():
    x = input("enter the value of year")
    a = input("enter the value of month")
    s = input("enter the value of day")
    d =(s+"_"+a+"_"+x)
    print(d)
    import pymysql as myb
    my_b = myb.connect(host="localhost", user="root", passwd="12345", database="newschema")
    my_b_cursor = my_b.cursor()
    my_b_cursor.execute("alter table class12a add (" + d + " varchar(10) Default 'Present');")
    my_b_cursor.execute("commit;")
    my_b.close()
def absenta():
    import pymysql as myb
    my_b = myb.connect(host="localhost", user="root", passwd="12345", database="newschema")
    my_b_cursor = my_b.cursor()
    my_b_cursor.execute("show columns from class12a ;")
    data = my_b_cursor.fetchall()
    L = list()
    for i in (data):
        M = i[0]
        if M != "name" and M != "roll_no":
            L.append(M)
    print("The date records are:")
    for i in range(2,len(L)):
        print(i-1, ")", L[i])
    x = input("enter the date for marking absentees:")
    while True:
        choice = "y"
        y = input("enter the name of the student:")
        z = int(input("enter the class roll_no:"))
        my_b_cursor.execute("select Stu_Name from class12a ;")
        data1 = my_b_cursor.fetchall()
        
        l1 = list()
        for i in (data1):
            k = i[0]
            l1.append(k)
       
        my_b_cursor.execute("select RollNo from class12a ;")
        data2 = my_b_cursor.fetchall()
        
        l2 = list()
        for i in (data2):
            o = i[0]
            l2.append(o)
        
        if y in l1 and z in l2:
            print("The absentee has been marked")
            t = str(z)
            my_b_cursor.execute("update class12a set "+ x +" = 'Absent' where Rollno = "+ t +";")
            my_b_cursor.execute("commit ;")
        else:
            print("ERROR: name or roll_no is invalid")
            continue
        a = input("DO YOU WANT TO CHANGE THE ATTENDANCE FOR OTHER CHILDREN(y/n):")
        if a==choice:
            continue
        else:
            print("THANK YOU ,please rate us ")
            break
def dateb():
    x = input("enter the value of year")
    a = input("enter the value of month")
    s = input("enter the value of day")
    d =(s+"_"+a+"_"+x)
    print(d)
    import pymysql as myb
    my_b = myb.connect(host="localhost", user="root", passwd="12345", database="newschema")
    my_b_cursor = my_b.cursor()
    my_b_cursor.execute("alter table class12b add (" + d + " varchar(10) Default 'Present');")
    my_b_cursor.execute("commit;")
    my_b.close()
def absentb():
    import pymysql as myb
    my_b = myb.connect(host="localhost", user="root", passwd="12345", database="newschema")
    my_b_cursor = my_b.cursor()
    my_b_cursor.execute("show columns from class12b ;")
    data = my_b_cursor.fetchall()
    L = list()
    for i in (data):
        M = i[0]
        if M != "name" and M != "roll_no":
            L.append(M)
    print("The date records are:")
    for i in range(2,len(L)):
        print(i-1, ")", L[i])
    x = input("enter the date for marking absentees:")
    while True:
        choice = "y"
        y = input("enter the name of the student:")
        z = int(input("enter the class roll_no:"))
        my_b_cursor.execute("select Stu_Name from class12b ;")
        data1 = my_b_cursor.fetchall()
        
        l1 = list()
        for i in (data1):
            k = i[0]
            l1.append(k)
       
        my_b_cursor.execute("select RollNo from class12b ;")
        data2 = my_b_cursor.fetchall()
        
        l2 = list()
        for i in (data2):
            o = i[0]
            l2.append(o)
        
        if y in l1 and z in l2:
            print("The absentee has been marked")
            t = str(z)
            my_b_cursor.execute("update class12b set "+ x +" = 'Absent' where Rollno = "+ t +";")
            my_b_cursor.execute("commit ;")
        else:
            print("ERROR: name or roll_no is invalid")
            continue
        a = input("DO YOU WANT TO CHANGE THE ATTENDANCE FOR OTHER CHILDREN(y/n):")
        if a==choice:
            continue
        else:
            print("THANK YOU ,please rate us ")
            break
def datec():
    x = input("enter the value of year")
    a = input("enter the value of month")
    s = input("enter the value of day")
    d =(s+"_"+a+"_"+x)
    print(d)
    import pymysql as myb
    my_b = myb.connect(host="localhost", user="root", passwd="12345", database="newschema")
    my_b_cursor = my_b.cursor()
    my_b_cursor.execute("alter table class12c add (" + d + " varchar(10) Default 'Present');")
    my_b_cursor.execute("commit;")
    my_b.close()
def absentc():
    import pymysql as myb
    my_b = myb.connect(host="localhost", user="root", passwd="12345", database="newschema")
    my_b_cursor = my_b.cursor()
    my_b_cursor.execute("show columns from class12c ;")
    data = my_b_cursor.fetchall()
    L = list()
    for i in (data):
        M = i[0]
        if M != "name" and M != "roll_no":
            L.append(M)
    print("The date records are:")
    for i in range(2,len(L)):
        print(i-1, ")", L[i])
    x = input("enter the date for marking absentees:")
    while True:
        choice = "y"
        y = input("enter the name of the student:")
        z = int(input("enter the class roll_no:"))
        my_b_cursor.execute("select StuName from class12c ;")
        data1 = my_b_cursor.fetchall()
        
        l1 = list()
        for i in (data1):
            k = i[0]
            l1.append(k)
       
        my_b_cursor.execute("select RollNo from class12c ;")
        data2 = my_b_cursor.fetchall()
        
        l2 = list()
        for i in (data2):
            o = i[0]
            l2.append(o)
        
        if y in l1 and z in l2:
            print("The absentee has been marked")
            t = str(z)
            my_b_cursor.execute("update class12c set "+ x +" = 'Absent' where Rollno = "+ t +";")
            my_b_cursor.execute("commit ;")
        else:
            print("ERROR: name or roll_no is invalid")
            continue
        a = input("DO YOU WANT TO CHANGE THE ATTENDANCE FOR OTHER CHILDREN(y/n):")
        if a==choice:
            continue
        else:
            print("THANK YOU ,please rate us ")
            break

        
def class12a():
    import pymysql
    dbase=pymysql.connect(host="localhost", user="root", passwd="12345", database="newschema");
    db=dbase.cursor()
    def add_rec():
        Stu_Name=input("Enter Name of new student")
        RollNo=int(input("Enter student roll number"))
        db.execute("insert into class12a values('{}','{}')".format(RollNo, Stu_Name))
        db.execute("commit")
    def del_rec():
        RollNo=input("Enter roll no of student")
        db.execute("delete from class12a where RollNo='{}'".format(RollNo))
        db.execute("commit")
    while True:
        ans=int(input("""What do you want to perform
        1=Add record
        2=Delete record
        3=Add attendence
        4=Exit
        :"""))
        if ans==1:
            add_rec()
        elif ans==2:
            del_rec()
        elif ans==3:
            datea()
            ask=input("Do you want to mark someone absent(y/n):")
            if ask == "y":
                absenta()
            else:
                break
        else:
            break
def class12b():
    import pymysql
    dbase=pymysql.connect(host="localhost", user="root", passwd="12345", database="newschema");
    db=dbase.cursor()
    def add_rec():
        Stu_Name=input("Enter Name of new student")
        RollNo=int(input("Enter student roll number"))
        db.execute("insert into class12b values('{}','{}')".format(RollNo, Stu_Name))
        db.execute("commit")
    def del_rec():
        RollNo=input("Enter roll no of student")
        db.execute("delete from class12b where RollNo='{}'".format(RollNo))
        db.execute("commit")
    while True:
        ans=int(input("""What do you want to perform
        1=Add record
        2=Delete record
        3=Add attendence
        4=Exit
        :"""))
        if ans==1:
            add_rec()
        elif ans==2:
            del_rec()
        elif ans==3:
            dateb()
            ask=input("Do you want to mark someone absent(y/n):")
            if ask == "y":
                absentb()
            else:
                break
        else:
            break
def class12c():
    import pymysql
    dbase=pymysql.connect(host="localhost", user="root", passwd="12345", database="newschema");
    db=dbase.cursor()
    def add_rec():
        Stu_Name=input("Enter Name of new student")
        RollNo=int(input("Enter student roll number"))
        db.execute("insert into class12c values('{}','{}')".format(RollNo, StuName))
        db.execute("commit")
    def del_rec():
        RollNo=input("Enter roll no of student")
        db.execute("delete from class12c where RollNo='{}'".format(RollNo))
        db.execute("commit")
    while True:
        ans=int(input("""What do you want to perform
        1=Add record
        2=Delete record
        3=Add attendence
        4=Exit
        :"""))
        if ans==1:
            add_rec()
        elif ans==2:
            del_rec()
        elif ans==3:
            datec()
            ask=input("Do you want to mark someone absent(y/n):")
            if ask == "y":
                absentc()
            else:
                break
        else:
            break
while True:
    t=["Sunidhi", "Namrita", "Madhuri"]
    a=input("Enter Your Name:")
    b=input("Enter Your Password:")
    if a=="Sunidhi" and b=="123":
        class12a()
        break
    elif a=="Namrita" and b=="456":
        class12b()
        break
    elif a=="Madhuri" and b=="789":
        class12c()
        break
    else:
        print("Your username or password is wrong")
