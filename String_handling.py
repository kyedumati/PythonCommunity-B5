# a="I want to learn python"
# print(a[1])
# print(a[-5])
#for val in a:
#    print(val)
# i=0
# while i<len(a): # 6
#     print(a[i])
#     i += 1
# slicing
# print(a[10:15])
# print(a[10:])
#print(a[-12:-7])
# tnaw
# print(a[-20:-16])  # -20+1  -19
                   # -19+1  -18
                   # -18+1  -17
                   # -17+1  -16
# print(a[-17:-21:-1]) # -17-1
                     # -18-1  -19
                     # -19-1  -20

# a='python'
# b='java'
# d=20
# c=a+d
# print(a*3)

# a='python'
# if 't' in a:
#     print("t is available in python")
# else:
#     print("not available")
# a='python'
# b='Python'
# if a==b:
#     print("both are same")
# else:
#     print("not same")
# if a>b:   #a=p 100+
#     print("a is greater than b")
# else:
#     print("a is less than b")

# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))

# print(chr(89))
# print(ord('$'))

# a=" ka si  "
# print(a)
# left_rm = a.lstrip()
# print(left_rm)
# right_rm = a.rstrip()
# print(right_rm)
# strip_rm = a.strip()
# print(strip_rm)

# a="I want to learn python"
# a="Python is a java programming language and java it is used to develop applications, it is both object oriented programming language"
  # it will search t in entire string
# print(a.count('t'))  # count(substring)
# count(substring,begin,end)
# print(a.count('t',2,14))
# print(a.count('to',2,14))
# print(a.count('is'))
# print(a.find('language'))
# print(a.find('java'))s
# if(a.find('java')!=-1):
#     print("java is available")
# else:
#     print("java is not available")
# print(a.find('java',0,24))
# print(a.index('java'))  # 12
# print(a.index('kasi'))  # valueerror
# b="python program"
#  0123456789 10 11 12 13
# print(a.rfind('language'))
# print(b.rfind('o')) #9
# print(b.find('o')) # 4
# print(len(a))

# a="Python is a java programming language and java it is used to develop applications, it is both object oriented programming language"
# print(a)
# b = a.replace('java','')
# print(a)
# print(b)
# s="ababababababab"
# s1=s.replace('a','cd')
# s1=s.replace('z','cd')
# print(s1)

# s="java$python$.net$sql$git"
# languages=s.split('$')
# print(languages)  # ['java', 'python', '.net', 'sql', 'git']
# languages = ['java', 'python', '.net', 'sql', 'git']
# s="-".join(languages)
# print(s)

# s="learning Python is Very easy"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# 2.x=[[1,2,3,4],[4,7,5,6]] swap first and last element in nested list
# output :[[4,2,3,1],[6,7,5,4]]
# x=[[1,2,3,4],[4,7,5,6]]
# # 0 len(l)-1
# for i in range(len(x)):  # 0 1
#     x[i][0],x[i][len(x[i])-1] =  x[i][len(x[i])-1],x[i][0]
# print(x)

# a=10
# b=20
# a,b=b,a
# print(a,b)

#8.find the longest palindrom string in list
#x=['hi','madam',java,'mam','python','amma']
# o/p:['madam' ]


# type of characters in string
#print("kasi123".isalnum())
# print("kasi123".isalpha())
# print("kasi".isalpha())
# print("kasi".isdigit())
# print("1234".isdigit())
# print("kasi".islower())
# print("Kasi".isupper())
# print("Kasi".istitle())
# print("Kasi Yedumati".istitle())
# print(" ".isspace())
print("123".isalnum())
# a=input("Enter a value")
# b=input("Enter b value")
# if(a.isdigit() and b.isdigit()):
#     c=int(a)+int(b)
#     print(c)
# else:
#     print("Dear User, you have entered invalid amount, please try numberic value")
#islower() --> just checks the case
#lower()  --> convert the case
# write a program to find type of given character
# ch = input("Enter any character: ")
# if ch.isalnum(): # either chars, either number and both
#     print("Alpha numberic character")
#     if ch.isalpha():
#         print("Alpha character")
#         if ch.islower():
#             print("Lowercase character")
#         else:
#             print("Uppercase character")
#     else:
#         print("it is a digit")
#
# elif ch.isspace():
#     print("it is a space character")
# else:
#     print("it is a special character")


# WAP to reverse the given string
# input : python
# output : nohtyp
# 1st using slicing operator
# s=input("Enter some string:")
# print(s[::-1])
#2nd approach
# print(type(reversed(s)))  # reversed(['n','o','h','t','y','p'])
# for i in reversed(s):
#     print(i)
#print(''.join(reversed(s)))

# 3rd approach
# python   --> nohtyp
# step1 you need to find length of string
# # step2 we need start reading the values from last index
# # step3 every value we need to start appending
# s=input("Enter some string:")
# l=len(s)-1  # python -- 5 4 3 2 1 0
# output_string = ''
# while l>=0:
#     output_string +=s[l]  # output_string = output_string+s[l]
#     l-=1   # # l=l-1
# print(output_string)

# Q2 --> program to reverse  order of words
#  input : virat kohli
#  output : kohli virat

# input: Learning Python Is Very Easy
# Output: Easy Very Is Python Learning
# Step1 : We need to split words --> it returns list of words
# Step2 : Returned list should start iterating in reverse order
# Step3: Need to start appending

S = "Learning Python Is Very Easy"
s_list = S.split() # ["Learning","Python","Is","Very","Easy"]
# l=len(s_list)-1
# output_string=''
# output_string=[]
# while l>=0:
#     # print(s_list[l])
#     #output_string+=s_list[l] + ' '
#     output_string.append(s_list[l])
#     l -= 1
# print(output_string.rstrip())
# output_string=' '.join(s_list[::-1])
# print(output_string)