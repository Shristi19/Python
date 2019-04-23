"""
Given an alphanumeric string S, extract maximum numeric value from that string. All the
alphabets are in lower case. Take the maximum consecutive digits as a single number.
Input Format:
The first line contains the string S.
Output Format:
Print the maximum value
Example:
Input:
23dsa43dsa98
Output:
98

"""
import re

input='100klh564abc365bg'                       #or you can simply take an input from the user


list1=re.findall('\d+',input)

print(list1)

integer_list=list(map(int,list1))

print(integer_list)

print(max(integer_list))
