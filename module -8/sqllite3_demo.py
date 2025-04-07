import sqlite3

try:
    dbcon=sqlite3.connect("student_db.db")
    print("database is created successfully.")
except Exception as  E :
    print(E)


try  :
    create_tab="create table info_stud(roll no int primary key,name text, course text)"
    dbcon.execute(create_tab)
    print("table is created successfully ")
except Exception as E :
    print(E)  


try :
    ins_data ="insert into info_stud values (101 ,'megha','python')"   
    dbcon.execute(ins_data)
    dbcon.commit()
    print("record is inserted successfully .")
except Exception as  E:
    print(E)    



