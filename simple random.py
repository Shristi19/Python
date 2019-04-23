"""import random
summ=0
outlist=[1,2,3,4,5,6,7,8,9]
iter=0
ran=random.randint(1 ,5)
while(summ != 45):
    alloc=0
    a=[]
    for i in range(ran):
        add=random.randint(0,45-alloc)
        a.append(add)
        alloc=add
    print(a)
    summ=sum(a)
a.sort()
print(a)
"""


fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
print(fruit_list1)
print(fruit_list2)
print(fruit_list3)
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print (sum)
