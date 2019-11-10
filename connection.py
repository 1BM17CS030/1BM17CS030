import sqlite3 

connection = sqlite3.connect("exp.db") 

crsr = connection.cursor() 

crsr.execute("SELECT * FROM emp") 

ans= crsr.fetchall() 

for i in ans: 
	print(i) 



sql_command = """INSERT INTO emp VALUES (20, "john", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO emp VALUES (26, "sham", "Bansal", "M", "2019-03-28");"""
crsr.execute(sql_command) 
sql_command = """INSERT INTO emp VALUES (29, "jay", "Bansal", "f", "2000-03-27");"""
crsr.execute(sql_command)
