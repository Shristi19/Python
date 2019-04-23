"""
With a given list of numbers where certain numbers are repeated 
Print the numbers which are not repeated with their order preserved
"""

lis=[12,24,35,24,88,120,155,88,120,155]

oplis=[]

iter=0
for element in lis:
    iter=iter+1
    for i in range(iter,len(lis)):
        if element == lis[i]:
            if element not  in oplis:
                 oplis.append(element)



print(oplis)
