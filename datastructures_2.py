# list
# a=[1234,"ongole",1234,523305,98.5,1234]
    # 0      1       2     3   4   5
# b=list((10,203))
# print(type(a))
# print(a[1])
# print(a[1:3])
# print(a)
# print(len(a))
# print(type(b))
# print(a)
# a[2]=2233
# print(a)
# append()  --> it will insert new value at the end of the list
# a.append("python")
# print(a)
# a.remove(1234)  # it removes only first occurance value
# print(a)


# tuple
# a=(10,20)
# a=('a','e','i','o','u')
# day=('monday','tuesday','wednesday','thursday','friday','saturday','sunday','sunday')
# print(day)
# # a[0]=30
# # a.append(30)
# print(day[2])
# print(type(day))


# range() --> used to generate sequence of nummbers
# r= range(20)
# print(type(r))
# print(r)
# for i in r:
#     print(i,end=" ")

# syntax 2: range(x,y)
# x=range(20,30)
# x=range(30,10)
# print(x)
# for i in x:
#     print(i,end=" ")
#

# syntax 3: range(startpos,endpos,incrementval)
# x=range(10,100,3)  #  start pos should always be less than ending position whenever the incrment value is positive
# # x=range(100,10,-3)  #  start pos should always be greater than ending position whenever the incrment value is negative
# for i in x:
#     print(i,end=" ")


# set
# student_info={1234,"kasi",98.3,200,300,300,"kasi"}
# print(student_info)
# student_info.add("SSN")
# print(student_info)
# student_info.remove(200)
# print(student_info)
# print(type(student_info))

# s={1234,"kasi",98.3,200,300,300,"kasi"}
# print(s)
# l=list(s)
# print(l)

# 0-255  --> 256

#frozenset --> it is exactly same as set but it doesnt allow to modify
# s={10,20,30,40,50,50}
# print(type(s))
# fs=frozenset(s)  # to create frozentset
# print(type(fs))
# # fs.add(100)
# s.add(100)
# print(fs)
# print(s)

# dict
# student_info={1:'Catherine',2:'Chinna',3:'Narasimha'}
# The below variable is used to store contact information of all employees
contact_info={9986332875:'Varun',9876543210:'Neelima',6302193992:'Pavan',9986332875:'Varun Kumar'}
# print(student_info)
# print(type(student_info))
# print(student_info[4])

"""
contact_info[6302193992]='Pavan Kadiyam'  # to change or update value
print(contact_info)
print(contact_info[6302193992])
print
9986332875,9876543210,6302193992
Neelima, Pavan, Varun Kumar
print(contact_info.keys())
print(contact_info.values())
"""
# def m1():
#     a=10
   # return a

# print(m1())

# comments in python