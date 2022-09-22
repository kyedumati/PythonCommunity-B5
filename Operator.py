# a=20
# b=3
# a=30
# b=4
#arithmatic operators
'''
print(a+b)  # 34
print(a-b)  # 26
print(a*b)  # 120
print(a/b)  # 7.5
print(a%b)  # reminder  2
print(a//b) # 7
print(a**b) # power
'''

# comparison operators
# a=30
# b=30
# a="kasi yedumati"
# b="kasi"
# print(a>b) # False
# print(a<b) # False
# print(a>=b) # True
# print(a<=b) # True
# print(a==b) # True
# print(a!=b) # False


#Logical Operators : and, or , not
# a=True
# b=False
# print("a and b ",a and b)
# print("a or b ",a or b)
# print("not a ", not a) # not True  --> False
# print("not b ",not b) # not False --> True

# a=20  # True  -->
# b=0  # True  -->
# print("a and b ",a and b) # 0
# print("a or b ",a or b)  # 20
# print("not a ", not a)   # False
# print("not b ",not b)    # True

# a="kasi"    # True
# b="yedumati" # True
# print("a and b ",a and b) # Yedumati
# print("a or b ",a or b)  # kasi
# print("not a ", not a)   # False
# print("not b ",not b)    # False


# Assignment operators
# a=36
# a+=20  # a=a+20
# print(a)  # 50
# a-=20  # a=a-20
# print(a) # 10
# a*=20  # a=a*20
# print(a) # 200
# a/=30  # --> a=a/30
# print(a)
# a%=30  # --> a=a%30
# print(a)


# Special operators
# Identity operators -->  is , is not
# a=10
# b=20
# a=True
# b=False
# a="Kasi"
# b="kasi"
# print(id(a))
# print(id(b))
# print(a is b) # to check address comparision
# print(a is not b)
# a="10"
# # a=int(10) # 10
# b=10  # 10
# print(id(a))
# print(id(b))
# print(a is b)
# # a==b


# Membership operator : in, not in
# lang="python"
# print('p' in lang) # True
# print('k' in lang) # False
# print('n' in lang) # False
# print('o' not in lang) # False
# roll_numbers=[12,13,14,15,16,18]
# print(20 in roll_numbers)
# print(16 in roll_numbers)

# a=frozenset({'a','e','i','o','u'})
# print(a)
# b='i'
# print(b in a)
# print('a' in a)
# if b in a:
#     print(b," is a vowel")
# else:
#     print(b," is a consonant")
