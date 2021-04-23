#Nick Jones
#DSC 450 Mideterm
#Problem 4

import sqlite3  
#Generating my 3 tables  
Student = ''' 
    CREATE TABLE Student 
    ( 
     StudentID  NUMBER(20) NOT NULL, 
      Name VARCHAR2(25), 
      Address VARCHAR2(25), 
      GradYear  NUMBER(4), 
     
        PRIMARY KEY(StudentID) 
    );
    '''  
      
Course = ''' 
    CREATE TABLE Course 
    ( 
     CName  VARCHAR(20) NOT NULL, 
     Department VARCHAR2(25), 
        Credits  NUMBER(2), 
     
          PRIMARY KEY(CName) 
    );
    '''  
      
Grade = ''' 
    CREATE TABLE Grade 
    ( 
        CName  VARCHAR(20) NOT NULL, 
        StudentID  NUMBER(20) NOT NULL, 
        CGrade NUMBER(5,2), 
     
        PRIMARY KEY(CName, StudentID), 
     
        FOREIGN KEY(StudentID) 
         REFERENCES Stduent(StudentID), 
        FOREIGN KEY(CName) 
         REFERENCES Course(CName) 
          
    ); 
    '''  
#Creating connection and executing the tables
conn = sqlite3.connect('dsc450_midterm.db')  
cursor = conn.cursor()  
cursor.execute('DROP TABLE IF EXISTS Student')  
cursor.execute('DROP TABLE IF EXISTS Course')  
cursor.execute('DROP TABLE IF EXISTS Grade')  
#create 3 tables by 3 different cursors   
cursor.execute(Student)
cursor.execute(Course)  
cursor.execute(Grade)  
#Inserts from Student, Course, and Grade Tables
insert1 = ["INSERT INTO Student VALUES(123, 'Bobby Muriel Boucher','Baton Rouge, LA',2010);",  
               "INSERT INTO Student VALUES(124, 'Happy Muriel Gilmore','New York, NY',2011);",  
               "INSERT INTO Student VALUES(125, 'William Nicholas Jones','Evansville, IN',2012);",  
               "INSERT INTO Student VALUES(126,'Tom Edward Brady','San Mateo, CA',2013);",  
               "INSERT INTO Student VALUES(127,'Billy Bob Thornton','Los Angeles, CA',2014);",  
               "INSERT INTO Student VALUES(128, 'David Grandpa Ross','Chicago, IL',2015);"]  
      
insert2 =["INSERT INTO Course VALUES('Machine Learning', 'Computer Science',4);",  
               "INSERT INTO Course VALUES('Database Management', 'Data Science',4);",  
               "INSERT INTO Course VALUES('Calculus I', 'Mathematics',3);",  
               "INSERT INTO Course VALUES('Calculus II', 'Mathematics',3);",  
               "INSERT INTO Course VALUES('Accounting Analysis', 'Business',3);"]  
      
insert3 =["INSERT  INTO Grade VALUES('Accounting Analysis', 126,3.5);",  
               "INSERT  INTO Grade VALUES('Database Management',128,4.0);",  
               "INSERT  INTO Grade VALUES('Database Management', 125,3.7);",  
               "INSERT  INTO Grade VALUES('Database Management', 123,3.8);",  
               "INSERT  INTO Grade VALUES('Calculus I', 126,3.0);",   
               "INSERT  INTO Grade VALUES('Calculus I', 127,2.7);",  
               "INSERT  INTO Grade VALUES('Accounting Analysis', 123,4.0);",  
               "INSERT  INTO Grade VALUES('Accounting Analysis', 124,3.9);",  
               "INSERT  INTO Grade VALUES('Calculus II', 125,3.6);",  
               "INSERT  INTO Grade VALUES('Calculus II', 128,3.2);",  
               "INSERT  INTO Grade VALUES('Calculus II', 123,3.8);",  
               "INSERT  INTO Grade VALUES('Calculus II', 124,3.5);"]  
#Executing the insert      
for item in insert1:  
      cursor.execute(item)  
for item in insert2:  
      cursor.execute(item)  
for item in insert3:  
      cursor.execute(item)  
#Generating the join query to join Student, Course, and Grade      
join_query = ''' 
    select temp1.SID AS SID, temp1.Name, temp1.Address, temp1.GradYear, course.CName, TEMP1.CGrade, Course.DEPARTMENT, Course.CREDITS from  
    (SELECT s.StudentID as SID, s.Name as Name, s.Address AS Address, s.GradYear AS GradYear, g.CName AS CName, g.CGrade AS CGrade 
    FROM Student s LEFT OUTER JOIN Grade g 
    ON s.StudentID = g.StudentID) temp1 Left OUTER JOIN  
    Course ON TEMP1.cname = course.cname 
    union 
    select temp2.SID AS SID, Student.Name, Student.Address, Student.GradYear, temp2.CName, temp2.CGrade, temp2.DEPARTMENT, temp2.CREDITS from  
    (SELECT c.cname as cname, C.DEPARTMENT AS DEPARTMENT, c.credits AS Credits, g.StudentID AS SID, g.CGrade AS CGrade 
    FROM Course c LEFT OUTER JOIN Grade g 
    ON c.cname = g.cname) temp2 Left OUTER JOIN  
    Student ON temp2.SID = student.studentid; 
    '''  
#Executing query and print the joined table      
res = cursor.execute(join_query) 
conn.commit()  
r1 = res.fetchall()  
print(str(r1))

#Writing a file from the join query in Python
with open('midterm_part4.txt','wb')as outfile:  
  cursor = conn.cursor()  
  for rows in cursor.execute(join_query):  
        eachRow = ','.join([str(i) for i in rows]) + '\n'  
        outfile.write(eachRow.encode())  
outfile.close()  
#Functional dependency violations with Python
with open('midterm_part4.txt','r') as infile:  
    data = infile.readlines()  
    course = {}  
    key = []  
    for line in data:  
        val = line.split(',')  
        if val[4] == 'None':  
            pass  
        elif val[4] not in key:  
            course[val[4]] = val[-1].strip()  
            key.append(val[4])  
        elif val[4] in key:  
            if val[-1].strip() != course[val[4]]:  
                print('Functional dependency violation happend in the line: ',val)  
infile.close()
#Generate averages of department using python
with open('midterm_part4.txt','r') as infile:  
    data = infile.readlines()  
    dpt = {}  
    count = {}  
    keys = []  
    for line in data:  
        val = line.split(',')  
        if val[6] == 'None':  
            break  
        if val[5] == 'None':  
            val[5] = 0  
        if val[6] not in keys:  
            keys.append(val[6])  
            dpt[val[6]] = float(val[5])  
            count[val[6]] = 1  
        elif val[6] in key:  
            dpt[val[6]] += float(val[5])  
            count[val[6]] += 1  
    print('Department/Average Grade/Count: \n')  
    for item in dpt:  
        print(item, '/', round(dpt[item]/count[item],2), '/', count[item])                         	  
infile.close()  
