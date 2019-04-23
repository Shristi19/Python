"""
The game of Bulgarian Solitaire
In this assignment, you will model the game of Bulgarian Solitaire. The game starts with
45 cards. (They need not be playing cards. Unmarked index cards work just as well.)
Randomly divide them into some number of piles of random size. For example, you
might start with piles of size 20, 5, 1, 9, and 10. In each round, you take one card from
each pile, forming a new pile with these cards. For example, the sample starting
configuration would be transformed into piles of size 19, 4, 8, 9, and 5. The solitaire is
over when the piles have size 1, 2, 3, 4, 5, 6, 7, 8, and 9, in some order. (It can be shown
that you always end up with such a configuration.) In your program, produce a random
starting configuration and print it. Then keep applying the solitaire step and print the
result. Stop when the solitaire final configuration is reached.

"""



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
