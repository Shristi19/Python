print("Enter resistance ")
resistance = input().split("+")
print(resistance)
r = resistance[0]
print(r[0],r[1],len(r))
t = resistance[1]
print(t)
def rcolor(i):
    switcher={
              0:"Black",
              1:"Brown",
              2:"Red",
              3:"Orange",
              4:"Yellow",
              5:"Green",
              6:"Blue",
              7:"Violet",
              8:"Grey",
              9:"White"
             }
    return switcher.get(i,"Invalid digit")

def tcolor(i):
    switcher={
              1:"Brown",
              2:"Red",
              0.5:"Green",
              0.25:"Blue",
              0.1:"Violet",
              0.05:"Grey",
              5:"Gold",
              10:"Silver",
              20:"None"

             }

    return switcher.get(i,"Invalid tolerance")

first = rcolor(int(r[0]))
second = rcolor(int(r[1]))
third = rcolor(len(r)-2)
fourth = tcolor(float(t))

print("The color code is ",first,second,third,fourth)

# Output:
# 
# Enter resistance
# 6200+5
# The color code is  Blue Red Red Gold
