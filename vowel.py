"""
Given a string S of lowercase letters, remove consecutive vowels from S. After removing,
the order of the list should be maintained.
Input Format:
Sentence S in a single line
Output Format:
Print S after removing consecutive vowels
Example:
Input:
your article is in queue
Output:
yor article is in qu

"""



string='your article is in queue'

def isvowel(c):

    return (c=='a' or c=='e' or c=='i' or c=='o' or c=='u')
print(string[0],end="")
for i in range(1,len(string)):
    if(isvowel(string[i-1])!=True or isvowel(string[i])!=True):
        print(string[i],end="")
