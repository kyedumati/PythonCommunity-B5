import mysql.connector
import DbUtil

def add_employee():
    try:
        emp_name = input("Enter emp name:")
        emp_mobileno = input("Enter mobileno:")
        db_conn = DbUtil.get_db_conn()
        cursor_obj = db_conn.cursor()
        #query = "insert into python_community3.emp_info(name,mobileno) values(%s,%s)"
        query = "insert into python_community3.emp_info(empid,name,mobileno) select max(empid)+1,%s,%s from python_community3.emp_info"
        val = (emp_name,emp_mobileno)
        cursor_obj.execute(query,val)
        db_conn.commit()
        print("New employee is added succesfully")
    except Exception as e:
        print("We are experiencing technical issue in adding employee, please try after sometime",e)
    finally:
        db_conn.close()

def update_employee():
    try:
        emp_id = input("Enter empid:")
        emp_name = input("Enter emp name:")
        emp_mobileno = input("Enter mobileno:")
        db_conn = DbUtil.get_db_conn()
        cursor_obj = db_conn.cursor()
        query = "update python_community3.emp_info set name=%s,mobileno=%s where empid=%s"
        val = (emp_name,emp_mobileno,emp_id)
        cursor_obj.execute(query,val)
        db_conn.commit()
        print("Updated employee succesfully")
    except:
        print("We are experiencing technical issue in adding employee, please try after sometime")
    finally:
        db_conn.close()

def delete_employee():
    try:
        emp_id = int(input("Enter empid:"))
        db_conn = DbUtil.get_db_conn()
        cursor_obj = db_conn.cursor()
        #query = "delete from python_community3.emp_info where empid="+str(emp_id)+""
        query = "delete from python_community3.emp_info where empid=%s"
        val = (emp_id,)
        cursor_obj.execute(query,val)
        db_conn.commit()
        print("Employee deleted succesfully")
    except Exception as e:
        print("We are experiencing technical issue in adding employee, please try after sometime",e)
    finally:
        db_conn.close()

def get_employees():
    try:
        db_conn = DbUtil.get_db_conn()
        cursor_obj = db_conn.cursor()
        query = "select * from python_community3.emp_info"
        cursor_obj.execute(query)
        emp_info = cursor_obj.fetchall()
        for emp in emp_info:
            print(emp)
        print("Employees fetched succesfully")
    except Exception as e:
        print("We are experiencing technical issue in adding employee, please try after sometime",e)
    finally:
        db_conn.close()


if __name__ == '__main__':
    print("******Welcome to Employee Management Tool*******")
    print("Please select anyone of the following operations")
    print("1. New Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. List Employees")
    selected_option = ''
    try:
        selected_option = int(input("Please Select "))
    except:
        print("Please enter valid input")
    if selected_option not in [1,2,3,4]:
        print("You have selected wrong option")
    else:
        if selected_option==1:
            add_employee()
        elif selected_option==2:
            update_employee()
        elif selected_option==4:
            get_employees()
        else:
            delete_employee()



