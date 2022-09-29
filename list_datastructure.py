# empty list
# a=[]
# a=list()
# print(type(a))
b="pyt hon"
# b="abcdcf"
# b="kasi,yedumati,java,python"
# print(type(b))
# b=b.split(',')  # this function is used split or saperate given value using space by default if we give some
              # value in parameter it will saperate based on given saperator
# print(b)
# print(type(b))
#a=[10,20,30,10,40]

# Accessing elements of list
# a=['p','y','t','h','o','n']
# print(a[0])
# print(a[4])
# print(a[-2])
# using slice
# print(a[0:3])
# print(a[0:5:2])
# print(a[0:4:3])
ls = [10,20,30,10,40,30,30]
#len()  -->  it returns the number of elements present in the list
#print(len(ls))

# count() -->  it returns the number of occurances of the specified item in the list, if item is not there it will return 0
# print(ls.count(10))
# print(ls.count(30))
# print(ls.count(5))   #0

# index() -->  it retuns the index of first occurannce of the specified item
#               if the specified value is not present in the list it will get ValueError
# print(ls.index(40))
# print(ls.index(10))
# print(ls.index(30))
# print(ls.index(50))

# Manipulating elemens of list
# cricketers = ['dhoni']
# append() --> it is used add a new value in the end of list
# print(cricketers)
# cricketers.append('kohli')
# cricketers.append('yuvraj')
# print(cricketers)

# insert() --> To insert item at the specified index position
# insert(indexposition, elements)
# cricketers.insert(1,'bumrah')
# print(cricketers)
# cricketers.insert(6,'kasi')
# print(cricketers)
# if the specified index is greater than max index then element will be added a last position

# extend()  -->  To add multiple values in to list , to add one list into another list
# extend(listvariable)
# cricketers =[]
# batsmen =['dhoni','rohit','kohli']
# bowlers = ['bumrah','shami','chahal']
# cricketers.extend(batsmen)
# #cricketers.extend(bowlers)  # ['dhoni', 'rohit', 'kohli', 'bumrah', 'shami', 'chahal']
# cricketers.append(batsmen)
# cricketers.append(bowlers)   # [['dhoni', 'rohit', 'kohli'], ['bumrah', 'shami', 'chahal']]
# print(cricketers)
# print(cricketers[0][0])
# print(cricketers[1])

# remove() --> to remove specified item from the list, it the item is present multiple times then
# only first occurance will remove
# batsmen =['dhoni','kohli','rohit','kohli']
# print(batsmen)
# batsmen.remove('kohli')
# print(batsmen)
# batsmen.remove('yuvraj') # if the given item is not present the it returns ValueError

# pop()  --> It removes and returns the last element of the list
# this is the only function which manipulates the list and returns some element
# choclates =['fivestar','asha','dairy milk','munch','kitkat']
# print(choclates)
# print(choclates.pop())
# print(choclates)
# print(choclates.pop())
# print(choclates)
# print(choclates.pop())
# print(choclates.pop())
# print(choclates.pop())
# print(choclates)
# if len(choclates)>0:   #
#     print(choclates.pop())  # if the list is empty then pop() return IndexError
# else:
#     print("choclates is empty you cannot pop")
# i = choclates.index('dairy milk')
# print(choclates.pop(i))  # this will accept index and returns and removes given index element
# print(choclates)

#
# n= [10,5,20,3]
# [3,5,10,20]   # ascending order --> from low to high
# [20,10,5,3]   # descening order --> from high to low
# print(n)
# reverse() --> used to reverse order of elements
# n.reverse()  # no matter what are the vlaues list contains, it will simple reverse the list
# print(n[::-1])
# print(n)

# sort() -->
# in list by default insertion order is preserved, if we want to sort the elements of list according to natural sorting order
# then we should go for sort() function
# n.sort()  --> to sort the values in ascending order
# n.sort(reverse=True)     #--> to sort the value in descedning order
# n.reverse()
# print(n)
# For numbers --> Default natural soring order is Ascending order
# For string -->  default natural soring order is Alphabetiacal Order
# s=["Grapes","Banana","Apple","Pineapple","Apbc"]
# s.sort()
# # s.sort(reverse=True)
# print(s)
# s.clear()   # all the elements it removes at a time
# print(s)
# Note : To use sort(), it is compulsory list should contain only homegenious elements otherwise it will return TypeError



'''
*        --> 1 
* *          
*        --> 3
* *  
*        --> 5
'''
# for i in range(5):
#     if(i%2 == 0):
#         print("*")
#     else:
#         print("* *")
    # for j in range

# aliasing list objects
# a=[10,20,30,40]
# b=a
# b.append(50)
# b[1]=50
# print(id(a))
# print(id(b))
# print(b)
# print(a)

# a=[10,20,30,40,50]
# b=a[:]   # clone using slicing operator
# b=a.copy()
# print(a[:])
# print(id(a))
# print(id(b))
# b.append(60)
# b[3]=60
# print(a)
# print(b)

# x=[10,20,30]
# x=60
# y=[40,50,60]
# y=50
# z=x+y
# print(z)

# x=[10,20,30]
# print(x)
# y=x*3
# print(y)
# ASCII
# x=[]
# y=["Apple",'Banana','"Apple",'Banana','Grapes'GrapeS']  # content
# y=["Apple",'Grapes','Banana']  # order is missed
# y=["Apple",'Banana','Grapes','Pineapple']
# print(x==y)  # False
# print(x!=y)  # True

# whenerver we are using <,<=,>,>= between List objects, only first element will be considered
# x=[10,20,30]
# y=[40,50,60]
# print(x>y)  # 10>40 False
# print(x<y)  # 10<40  True
# print(x<=y)  # 10<=40  True
# print(x>=y)  # 10>=40  False


#membership operators
# a=[20,10,30,40]
# if(60 in a):
#     print("10 is available in a")
# else:
#     print("not available in a")
# print(10 in a)   # True
# print(10 not in a)   # True

# nest_ls = [[10,20,30],[40,50,60],[70,[80,90]]]
# print(nest_ls[1][1])
# print(nest_ls[2][1][0])

# a=[10,20,30]
# a=[]
#a.clear()
#print(a)
# a.sort()
# print(a)
# print(a[::-1])
# a.sort(reverse=True)
# print(a)


# create a list with even numbers between 1 to 10
# even_numbers=[]
# for i in range(1,11):
#     if(i%2==0):
#         even_numbers.append(i)
# print(even_numbers)
# even_numbers = [i for i in range(1,11) if i%2==0]
# **  -> exponential operator to find the powe
#multiply = []
# even_numbers=[]
# for i in range(1,11): # 1,4,9,16,25,36,49,64,81,100
#         multiply.append(i**2)
# print(multiply)
# multiple = [i**2 for i in range(1,11)]
# print(multiple)
