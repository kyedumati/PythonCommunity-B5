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
#cricketers.extend(batsmen)
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

# pop()
