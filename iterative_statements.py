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
list1=[1,2,3,4]   # 4 times
list2=[10,20,30,40]  # 4 times
# 4*4
for i in list1:  # 1 2
    for j in list2:  # 10 20 30 40
        print("value from outer for is ",i," and outer for is ",j)
