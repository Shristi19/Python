"""
The game of Nim.
This is a well-known game with a number of variants.
The following variant has an interesting winning strategy.
Two players alternately take marbles from a pile. In each move, a player chooses how
many marbles to take. The player must take at least one but at most half of the marbles.
Then the other player takes a turn. The player who takes the last marble loses.
Write a program in which the computer plays against a human opponent.
Generate a random integer between 10 and 100 to denote the initial size of the pile.
Generate a random integer between 0 and 1 to decide whether the computer or the human
takes the first turn.
Generate a random integer between 0 and 1 to decide whether the computer plays smart
or stupid. In stupid mode the computer simply takes a random legal value (between 1 and
n / 2) from the pile whenever it has a turn.
In smart mode the computer takes off enough marbles to make the size of the pile a
power of two minus 1—that is, 3, 7, 15, 31, or 63. That is always a legal move, except
when the size of the pile is currently one less than a power of two. In that case, the
computer makes a random legal move. You will note that the computer cannot be beaten
in smart mode when it has the first move, unless the pile size happens to be 15, 31, or 63.
Of course, a human player who has the first turn and knows the winning strategy can win
against the computer.


"""




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
