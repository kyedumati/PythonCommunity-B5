# I want to print student information
# static inputs/ static data, hardcoding the values
# name="vijay"
# address="ongole"
# roll_no=1234
# print(name)
# print(address)
# print(roll_no)

# i want to perform sum of two values
# a=3000  # static data/ hardcoded values
# b=2000  # static data/ hardcoded values
# a=input("Please enter a value: ")  # "12"
# b=input("Please enter b value: ")  # "13"
# print(type(a))
# print(type(b))
# print("value of a is ",a)
# print("value of b is ",b)
# print(int(a)+int(b))


# Print values of student
# roll_no=input("Please enter rollno: ")
# name=input("Please enter name: ")
# address=input("Please enter your address :")
# print(roll_no)
# print(name)
# print(address)

# To read multiple values at a time to a single variable
# i want to print names of all students
# names = input("Enter names of students").split(',')
# print(type(names))
# print(names)
# # names = names.split(',')  # it will saperate give values using space
# print(len(names))

# roll_no=input("Please enter rollno: ")
# name=input("Please enter name: ")
# address=input("Please enter your address :")
# print(roll_no)
# print(name)
# print(address)
# name,roll_no,address = input("Enter student info: ").split(',') # ['kasi','1234','india']
# student_info = input("Enter student info: ").split(',')  # ['kasi','1234','india']
# print(student_info[0])
# print(student_info[1])
# print(student_info[2])

# a=10+20/3 # 10+6.66 = 16.6666
# print(a)
# a=input("Enter one mathematics expression: ")   # 10+20/3
# print(int(a))
# print(a)
# print("output is ",eval(a))
# roll_numbers=input("Enter rollnumbers list: ")
# print(type(roll_numbers))
# roll_numbers=eval(roll_numbers)
# print(type(roll_numbers))
# print(roll_numbers)

# commanline arguments
#
# from sys import argv
# print(type(argv))
# print(argv)
# print(argv[0])
# a=argv[1]   # 20
# b=argv[2]   # 30
# print(int(a)+int(b))  # 50
# print(argv[1])
# print(argv[2])
#list(), set()


# output statements
# we can use print() function to display output or print anything from python program
# Form-1 : print() without any arguments
# print("first line")
# print()  # it just prints new line
# print("third line")
# Form 2: print(arg) with any arguments
# print("Hello \nworld")
# print("Hello \tworld")
# print("Hello"+"10")
# print("Hello"*10)
#print("Hello"*"10")

#Form-3 : print() with multiple arguments
# a=10
# b=20
# c=30
# print("abc values are ",a,b,c)
# print(a,b,c)  # default seperator is space only
# print(a,b,c,sep='kasi')
# print(a,b,c,sep=':')

# Form-4 : print() with end attribute
# print(end='\n')
# print("kasi",end=' python ')
# print("yedumati")
# print("java developer")

# Note: the default of end attribute is \n   default value of sep attritbute is ' '
#Form 5: print(formatted string)
#Syntax: print("formatted string"%(varible list))
a=20
b=30
c=a+b
#  %i  --> int
#  %d  --> int
#  %f  --> float
#  %s  --> string
# print("sum of a and b is ",c)
# print("sum of",a," and",b," is ",c) # sum of 20 and 30 is 50
# print("a value is ",a)
# print("a value is %d" %a)
# print("sum of %d and %d is %d"%(a,b,c))
# name="dhoni"
# print("my favourite cricketer is %s"%name)

# Form-6 print() with replacement operator {}
name="Yuvraj"
address="india"
dob=12

# My favourite cricketer is Yuvraj and he plays for india and his dob is 12
print("My favourite cricketer is %s and he palys for %s and his dob is %d"%(name,address,dob)) # we need to know type and order also
print("My favourite cricketer is {0} and he plays for {1} and his dob is {2}".format(name,address,dob)) # we dont want type but order should be there
print("My favourite cricketer is {x} and he plays for {y} and his dob is {z}".format(y=address,z=dob,x=name)) # we dont want to maintain order and no need of type
print("My favourite cricketer is {name} and he plays for {address} and his dob is {dob}".format(address=address,dob=dob,name=name))