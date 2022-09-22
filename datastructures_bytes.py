# byte data type
# Bytes represents a group of numbers and numbers allowed is 0 to 256  :   (0, 256)

# once we created bytes we cannot modify the values, immutable
# a=bytes([1,2,3,4,6,2560])
# print(a)
# print(type(a))

# bytesarray  it is exactly same as bytes datatype, except it can be modified
#
# b=bytearray([70,10,40,50])
# print(b)
# print(type(b))
# print(b[0])
# print(b[3])
# for i in b:
#     print(i,end=" ")
#
# print()
# # print('before',b[1])
# b[1]=100
# b[0]=123
# # print('after', b[1])
# # to print all values in b
# for i in b:
#     print(i,end=" ")
# x="hellopython"
# print(x[-1::-6])
# x="hi kasi"
# print(x[-1:-3:-1])

# b=bytearray([70,10,40,'kasi'])