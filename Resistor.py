"""
Resistor Band Display Program
You all know that in an electronic circuit, the value of a resistor is coveyed using cour
band, where every color band has significance.
Suppose a resistor has a value 6.2 kΩ ±5 percent. The resistor tolerance of ±5 percent
indicates the acceptable variation in the resistance. A 6.2 kΩ ±5 percent resistor could
have a resistance as small as 5.89 kΩ or as large as 6.51 kΩ.
We say that 6.2 kΩ is the nominal value of the resistance and that the actual value of the
resistance can be any value between 5.89 kΩ and 6.51 kΩ.
Now write a program outputs the description of the “color bands” for an input given by
the user as nominal value of the resistance and tolerance in percentage.
A resistor has four color bands:
• The first band is the first significant digit of the resistance value.
• The second band is the second significant digit of the resistance value.
• The third band is the decimal multiplier.
• The fourth band indicates the tolerance.

"""
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
