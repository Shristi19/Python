import numpy as np


def price_input(price):
    flag=0
    for i in range(0,9):
        for j in range(0,10):
            if array[i][j]==price:
                array[i][j]=0
                flag=1
                return flag
    return flag








array=np.array(
[[10,10 ,10 ,10, 10, 10 ,10 ,10 ,10 ,10],
[10 ,10 ,10 ,10 ,10, 10 ,10, 10 ,10 ,10],
[10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10],
[10 ,10 ,20 ,20 ,20 ,20 ,20 ,20 ,10 ,10],
[10 ,10 ,20 ,20 ,20 ,20 ,20 ,20 ,10 ,10],
[10 ,10 ,20 ,20 ,20 ,20, 20, 20, 10, 10],
[20 ,20 ,30, 30, 40 ,40 ,30 ,30 ,20 ,20],
[20 ,30 ,30 ,40 ,50, 50, 40 ,30, 30 ,20],
[30,40 ,50 ,50 ,50 ,50, 50 ,50 ,40,30]])
userinput= int(input("TYPE 1 FOR SEAT AND 2 FOR PRICE and 0 to exit"))
while userinput!=0:

    if userinput==1:
        row=int(input("Tell the row number youd like to seat in"))
        column=int(input("Tell the seat in that row youd like to seat in"))
        if(array[row-1][column-1]!= 0):
            array[row-1][column-1]=0
            print("Seat booked")
        else:
            print("Seat not available")
        print("Array/Theatre arrangement after booking")
        print(array)

    if userinput==0:
        break
    if userinput==2:
        price=int(input("Enter price from 10,20,30,40,50 ruppess:"))
        while price not in [10,20,30,40,50]:
            price=int(input("Enter price from 10,20,30,40,50 ruppess:"))



        flag=price_input(price)
        if flag==0:
            print("Tickets not availalble for this price")
        if flag==1:
            print("Tickets and seats are confirmed")
        print("Array/Theatre arrangement after booking")
        print(array)




    userinput= int(input("TYPE 1 FOR SEAT AND 2 FOR PRICE and 0 to exit"))


""""
item=np.where(array==10)
print(item)
list=list(zip(item[0],item[1]))
print(list)
"""
