"""
With a given list L of integers, write a program to print this list L after removing all
duplicate values with original order preserved.
Example:
If the input list is
12 24 35 24 88 120 155 88 120 155
Then the output should be
12 24 35 88 120 155

"""
lis=[12,24,35,24,88,120,155,88,120,155]

oplis=[]

for item in lis:
    if item not in oplis:
        oplis.append(item)



print(oplis)



