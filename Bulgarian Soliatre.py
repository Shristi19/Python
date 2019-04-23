import random
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
    summ=sum(a)


a.sort()
print(a)


flag=False

while(flag == False):
    newpile=0
    iter+=1
    print("Iteration:",iter)
    for i in range(len(a)):
        if a[i]!=0 :
           a[i]=a[i]-1
           newpile=newpile+1
    a.append(newpile)


    a=[j for j in a if j!=0]
    print(a)

    if a == outlist:
        flag=True
