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
a="Python is a programming language and it is used to develop applications, it is both object oriented programming language "
  # it will search t in entire string
print(a.count('t'))  # count(substring)
# count(substring,begin,end)
# print(a.count('t',2,14))
# print(a.count('to',2,14))
print(a.count('is'))