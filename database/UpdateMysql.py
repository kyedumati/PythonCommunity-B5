import mysql.connector

import DbUtil

# connect to database
db_conn = DbUtil.get_db_conn()
print("Database is connected")
cursor_obj = db_conn.cursor()
update_query = "update python_community3.emp_info set mobileno=1234 where name='test'";
cursor_obj.execute(update_query)
print("Query is executed successfully")
db_conn.commit()
db_conn.close()
print("Tasks is completed, database connection is closed successfully, Congratualations!!!!")