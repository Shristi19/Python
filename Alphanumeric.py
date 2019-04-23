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

#Regular expression to find numbers is "\d+". re.findall will find all the patterns matching the argument.
list1=re.findall('\d+',input)

print(list1)

#Since every number in the list is still a string we need to convert it into integers
integer_list=list(map(int,list1))
#The list is converted from a list of string to a list of integers
print(integer_list)
#To print the max of the numbers from the list just use the method max on the list.
print(max(integer_list))
