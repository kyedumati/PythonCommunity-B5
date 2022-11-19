import mysql.connector
import DbUtil

# connect to database
database_connection = DbUtil.get_db_conn()
print(database_connection)
# prepare a cursor object
cursor_object = database_connection.cursor()
# write a query
emp_info_query = "create table python_community3.emp_info(name varchar(30),mobileno varchar(20))"
# execute the query
cursor_object.execute(emp_info_query)

# close datbase connection
database_connection.close()