import mysql.connector
import DbUtil

database_connection = DbUtil.get_db_conn()
cursor_obj = database_conn.cursor()
# insert_query = "insert into emp_info(name,mobileno) values('kasi','6302193992')" # static query
# inserting single record
'''
insert_query = "insert into python_community3.emp_info(name,mobileno) values(%s,%s)" # dynamic query
val = ('kasi','6302193992')
'''
# inserting multiple records
insert_query = "insert into python_community3.emp_info(name,mobileno) values(%s,%s)" # dynamic query
val = [('naga','8072555596'),('test','8072555596')]
# val = ('kasi')
# cursor_obj.execute(insert_query,val)
cursor_obj.executemany(insert_query,val)
database_conn.commit()  # this step is required if the query is DML query
database_conn.close()