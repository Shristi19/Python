string='your article is in queue'

def isvowel(c):

    return (c=='a' or c=='e' or c=='i' or c=='o' or c=='u')
print(string[0],end="")
for i in range(1,len(string)):
    if(isvowel(string[i-1])!=True or isvowel(string[i])!=True):
        print(string[i],end="")
