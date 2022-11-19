import mysql.connector

import DbUtil

# connect to database
db_conn = DbUtil.get_db_conn()
cursor_obj = db_conn.cursor()
query= "select * from python_community3.emp_info where name='kasi'"
cursor_obj.execute(query)
emp_info = cursor_obj.fetchall()
# print(emp_info)
for i in emp_info:
    print(i)