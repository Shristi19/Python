import re

input='100klh564abc365bg'

list1=re.findall('\d+',input)

print(list1)

integer_list=list(map(int,list1))

print(integer_list)

print(max(integer_list))
