import sqlite3 

connection = sqlite3.connect("exp.db") 

crsr = connection.cursor() 


connection.commit() 


crsr.execute("SELECT * FROM emp") 

ans= crsr.fetchall() 

for i in ans: 
    print(i) 

crsr.execute("select * from emp where staff_number=20")
ans=crsr.fetchall()
print (ans)

crsr.execute("delete from emp where staff_number=20")
ans=crsr.fetchall()
print (ans)

crsr.execute("update  emp set staff_number='50',fname='RAM' where staff_number='26'")

ans= crsr.fetchall() 

for i in ans: 
    print(i) 


connection.close()
