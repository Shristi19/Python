import numpy
import random

sizeOfPile = random.randint(10,100)
currentTurn = random.randint(0,1)
computerIntellect = random.randint(0,1)
print("Computer intellect: ",computerIntellect)
while(sizeOfPile>0):
    print("\nNumber of marbles: ",sizeOfPile)
    if currentTurn==1:
        print("Your move!")
        halfPileSize = sizeOfPile/2;
        marblesToRemove = 0;
        while True:
            print("Choose no. of marbles to remove from the pile: ")
            marblesToRemove=int(input())
            if(marblesToRemove == 1 or (marblesToRemove > 0 and marblesToRemove < halfPileSize)):
                break;
        sizeOfPile=sizeOfPile-marblesToRemove
        print("size of pile after your move is : ",sizeOfPile)
        currentTurn=0
    else:
        countOfMarbles = 0
        if(computerIntellect==0):
            if(sizeOfPile%2==0):
                countOfMarbles=random.randint(1,(sizeOfPile/2))
            else:
                countOfMarbles = random.randint(1,((sizeOfPile-1) / 2)+1)
        elif(computerIntellect==1):
            if (sizeOfPile == 3 or sizeOfPile == 7 or sizeOfPile == 15 or sizeOfPile == 31 or sizeOfPile == 63):
                countOfMarbles = random.randint(1,((sizeOfPile-1) / 2)+1)
            else:
                if(sizeOfPile>63):
                    sizeOfPile=63
                elif(sizeOfPile>31):
                    sizeOfPile=31
                elif(sizeOfPile>15):
                    sizeOfPile=15
                elif(sizeOfPile>7):
                    sizeOfPile=7
                elif(sizeOfPile>3):
                    sizeOfPile=3
                elif(sizeOfPile==2):
                    sizeOfPile=1
                elif(sizeOfPile==1):
                    sizeOfPile=0

        sizeOfPile=sizeOfPile-countOfMarbles
        print("size of pile after computer move is : ",sizeOfPile)
        currentTurn=1
if(currentTurn==0):
    print("Computer wins")
else:
    print("You win")
