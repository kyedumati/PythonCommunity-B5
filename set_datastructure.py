# Creation of Set objects
#s={10,20,30}
# l=[10,20,30]
# s=set(l)
# print(s)
# s=set()
# print(type(s))

# Important fuctions of Set
# add(x)  --> to add item x to the set
# s={10,20,30}
# s.add(40)
# s.add(50)
# print(s)
# update(x,y,z) --> To add multiple items to the set at a time
# arguments(x,y,z) are not single values these are iterable objects like list,range,set,etc..
# s2={40,50,60}
# s3={70,80,90}
# s.update(s2)
# s.update(s2,s3)
# print(s)

# copy()  --> Returns copy() of set, it is used to clone object
# s={10,20,30}
# s2=s.copy()
# print(s)
# print(s2)
# print(id(s))
# print(id(s2))

# pop()  -->  It removes and returns some random element from the list
# print(s)
# a = s.pop()
# print(a)
# print(s)

#remove(x)  -->  It removes the specified value from the set, if the specified value is not present then we will KeyError
s={10,20,30}
# s.remove(10)
# print(s)
# s.remove(60)

# discard(x) --> it removes the specified value from the set, if the specified item not present in the set we won't any error
# s.discard(60)
# print(s)
# s.clear()
# print(s)
# {}


# Mathematical operations on the set:
# union() --> We can use this function to return all elements present in both the sets
# x.union(y)  or x | y
# x={10,20,30,40,50}
# y={40,50,60,70}
# z=x.union(y)
# z = x | y
# print(z)

# x.intersection(y)  -> returns common elements from both x and y
# z = x.intersection(y)   # x & y
# z = x & y
# print(z)

# x.difference(y)  --> it returns the elements present in x but not in y
# x={10,20,30,40,50}
# y={40,50,60,70}
# z= x.difference(y)
# p= y.difference(x)
# z=x-y
# p=y-x
# print(z)
# print(p)

# symmentric_difference() --> returns elements present in either x or y but not n both
# z=x.symmetric_difference(y)
# print(z)

# Membership operators (in, not in)
# z={10,20,30,40}
# print(10 in z)
# print(10 not in z)
# if 10 in z:
#     print("10 is available")
# else:
#     print("10 is not available")

# set comprehension
#  {expression for item in iterableobj if condn}
# s={i for i in range(1,20) if i%2!=0}
# print(s)

# l=[10,20,30,40,40,40,40,40,40,50,50]
# print(l)
# s=set(l)
# print(s)