# for loop
# name="kasi yedumati"
#print(len(name))
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[12])
# len_name = 0
# for i in name:
#     # len_name=len_name+1  #
#     len_name += 1 #
#     print("inside loop")
#     # print(i)
# print(len_name)

# numbers=[20,30,20,40,50]
# for value in numbers:
#     print(value)

# range() to generate sequence of numbers
# # i want to print all the numbers from 1 to 30
# for i in range(1,31):
#     print(i,end=' ')

# i want to print all the odd numbers from 1 to 30
# for i in range(2,31,2):
#     print(i,end=' ')

# vowels= {'a','e','i','o','u'}
# vowels={}
# print(type(vowels))
# print(vowels)
# for value in vowels:
#     print(value)

# iterative list and fetching values using indexing
# numbers=[20,30,20,40,50]
# numbers_len = len(numbers)  # 5
# for value in range(0,5)
# for 0 in range(5)
# for 1 in range(5)
# for 2 in range(5)
# for 3 in range(5)
# for 4 in range(5)

# for value in range(numbers_len):
#     print(value)
#     print(numbers[value])
# numbers=[20,30,20,40,50]
# i=0
# for value in numbers:
#     print("the value present in index ",i," is ",numbers[i])
#     i=i+1



# write a program to print sum of all numbers present in list
# numbers=[20,30,20,40,50]   # 20+30+20+40+50  = 160
# numbers_sum=0
# for value in numbers:
#     numbers_sum = numbers_sum + value   #
#     print(numbers_sum)
#     # print(value)
# print(numbers_sum)


# while loop
# write a program to print values from 1 to 10
# a=1
# while a<=10:  # 1<=10  --> True
#     print(a)  # 2<=10  --> True
#     a=a+1     # 3<=10  --> True
              # 10<=10 --> True
              # 11<=10  --> False

# a=1
# print(a)
# while a<=10:  #1 3 5 7 9 11
#     print(a)
#     a=a+2
# print(a)  # 11

# while False:
#     print("inside looop")


# inner for loop
# we want to print values from list1 and list2
# list1=[1,2,3,4]   # 4 times
# list2=[10,20,30,40]  # 4 times
# # 4*4
# for i in list1:  # 1 2
#     for j in list2:  # 10 20 30 40
#         print("value from outer for is ",i," and outer for is ",j)


# Pattern programs
# write a program to display * in right angled traingled format
# 1 3 5 7 ? 11   --> 9
# output
# hint -> we need to print * only
# we need to print in 5 lines
# we need to decide based on line numbers how many stars to print
# saperating every start with space
'''
*
* *
* * *
* * * *
* * * * *
'''
# for i in range(1,6):  #     # i=1
#     for j in range(1,i+1):  # j=1
#         print("*",end=" ")
#     print()   # new line


# write a program to display numbers in right angled traingled format
# 5lines
# every line we need print numbers based on the line number
# saperating every digit with space
'''
1
1 2 
1 2 3
1 2 3 4 
1 2 3 4 5
'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 5lines
# every line we need print numbers based on the line number
# saperating every digit with space
'''
1
2 2  
3 3 3
4 4 4 4 
5 5 5 5 5
'''
# for i in range(1,6):         # 1 2
#     for j in range(1,i+1):  # 1,2  --> 1
#                             # 1,3  --> 2
#         print(i,end=" ")  # 1                          # 2 2
#     print()

# 1 2 3     --> skipping 4 and 5 nothing we are stopping
# 1 2 3 5   --> skipping 4
# for i in range(1,6): # 1 2 3 4 5
#     if i>3:
#         break
#     print(i)
# print("after for loop")
# wickets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #
# if 10 wickets are down then we should print all out
# for i in wickets:
#     if i>10:
#         print("all out=, not allowed to continue the game")
#         break   # red
#     print("wicket number ",i," came to bat")

# stations = ["kashmir","pune","banglore","kanyakumari","srilanka"]
# for station in stations:
#     if station == "banglore":
#         continue
#     print("train is reached to " + station)
#     if station == "kanyakumari":
#         print("train has reached to final destination")
#         #print("train is reached to " + station)
#         break

# print only odd numbers between 1 to 10 using continue
# odd --> if number is not devided by 2 that number is called odd number
# for i in range(1,10):
#     if i%2==0:  # if value is even skip that value
#         continue
#     print(i)





