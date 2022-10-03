# t=()
# t=10,20,30
# t=(10,)
# t=(10,20,30)
list=[10,20,30]
t=tuple(list)
# print(type(t))
#print(t[1])
#print(t[1:])
# t[1] = 40
# t1=(10,20,30)
# t2=(40,50,60)
# a=30,
# t3=t1+a
# print(t3)
# print(t1*4) # operands --> t1 operand 4 op
# print(t1*t2)
# print(len(t2))
# print(t2.count(50)) # 0
# print(t2.index(60))
# print(t2.index(70))

# t2=(5,40,50,10,50,60)
# t3= sorted(t2)  # ascending order
# print(t3)
# t3= sorted(t2,reverse=True)  # descending order
# print(t3)
# t2=(5,40,50,10,"python",60)
# print(min(t2))
# print(max(t2))

# t1=(10,20,30)
# t2=(40,50,60)
# t3=(10,20,30)
# print(cmp(t1,t2))   # 0 -1 +1
# print(t1 == t2)
# print(t1 < t2)
# print(t1 == t3)
# a=10
# b="kasi"
# c=30
# t=a,b,c   # 10,20,30  --> it is a tuple # packing
# print(t)
# print(type(t))
# t2=(20,30,40,50)
# x,y,z,p = t2  # unpacking
# print(x)
# print(y)
# print(z)

# for x in range(1,6):
#     print(x**2)
# t=(x**2 for x in range(1,6))
# # t=[x**2 for x in range(1,6)]
# print(type(t))
# for i in t:
#     print(i,end=" ")


# write a program to take tuple of numbers from the keyboard and print its sum and average
# ex: input =(10,20,30)
# output, sum = 60, average= sum(input)/len(input)
t=  eval(input("Enter tuple of numbers"))  # (10,30,30)  # "(10,20,30)"
sum_output = 0
for x in t:
    sum_output= sum_output+x
average = sum_output/len(t)
print("sum_output ",sum_output)
print("average ",average)