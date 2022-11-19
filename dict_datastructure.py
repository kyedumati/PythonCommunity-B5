# student_data = {
# 	"rollno":"1234",
# 	"name":"naresh",
# 	"marks": [90,100,80],
# 	"address": {
# 		"city":"ongole",
# 		"district":{"name":"Prakasam"},
# 		"state":"AP",
# 		"country":"india",
# 		"pincode":"500000"
# 	}
# }
# d= {}
# d= dict()
# if student_data.has_key('city'):
# if 'name' in student_data:
#     print(student_data['name'])
# else:
#     print('name is not exist')
# print(student_data['marks'][1])
# print(student_data['address']['district']['name'])
# print(student_data['rollno'])
# print(student_data['address']['state'])
# print(student_data['address']['pincode'])


student_data = {"rollno":"1234","name":"naresh","marks": [90,100,80],
	"address": {"city":"ongole","district":{"name":"Prakasam"},"state":"AP","country":"india","pincode":"500000"}}
# update dictionary
# student_data['name'] = 'Mahesh'  # if key is available it will update the value
# student_data['college'] = 'SSN'  # if key is not exist it will create new key and value
# print(student_data)

# delete element from dict
# del dict[key]   --> it deletes entry associated with the speicified key if key is not found then we wil keyError
#del student_data['marks']
# del student_data['address']['district']['name']
# print(student_data)
# clear() --> To remove all entries from dictionary
# student_data.clear()
# del student_data
# print(student_data)

# len() --> returns number of items in the dictionary
# print(len(student_data))

# get() -- To get the value associated with the key
  # it returns value if key exists , if key does not exist it returns None
# print(student_data.get('address'))
# print(student_data.get('college'))
# get(key,defaultvalue)
student_data['college'] = 'Pace Engineering' #
# student_data['college'] = ''
# print(student_data)
# print(student_data.get('college','SSN'))

# pop(key) --> it removes the entry associated with the key and returns the corresponding vlaue
#  if the speicified key not available then we will get KeyError
# print(student_data.pop('college'))
# print(student_data)

#popitem() --> it removes random item(key-value) from dict and returns it
# print(student_data.popitem())
# print(student_data.popitem())

# keys() --> it returns all the keys associated with that dict
print(student_data.keys())
# for key in student_data.keys():
#     print(key)

# values() --> to reutn all the values associated with that dict
# for value in student_data.values():
#     print(value)

# items() --> it returns list of tuples representing key-value pairs
# for item in student_data.items():
#     print(item)

# copy() --> To create exactly duplicate dictionary (cloned copy)
# student_data_copy = student_data.copy()
# print(student_data)
# del student_data_copy['marks']
# print(student_data_copy)

# d.update(x)  --> All the items present in the dictionary x will be added to dictonary d
# d={"1":"prabhas","2":"Pawan"}
# d.update(student_data)
# print(d)

# dictionary comprehension
# {expression for item in iterablobj if condition}
# write a program to get square of every odd from 1-10
# {1:1,3:9,5:25,7:49,9:81}
# square_dict = {i:i**2 for i in range(1,10) if i%2!=0}
# square_list = [i**2 for i in range(1,10) if i%2!=0]   # list compression
# square_tuple = (i**2 for i in range(1,10) if i%2!=0)   # generator compression
# square_set = {i**2 for i in range(1,10) if i%2!=0}   # generator compression
# print(square_dict)
# print(square_list)
# print(square_tuple)
# print(square_set)