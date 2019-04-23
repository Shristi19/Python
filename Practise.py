"""
A panagram is a sentence containing every 26 letters in the English alphabet. Given a
string S, check if it is panagram or not.
Input Format:
The first line contains the sentence S.
Output Format:
Print &#39;YES&#39; or &#39;NO&#39; accordingly
Example:
Input:
The quick brown fox jumps over the lazy dog
Output:
YES
"""

"""
LOGIC:
Since we need to compare all the alphabets
Create a list with all the ascii letters, this list can be easily found in string module ascii_lowercase method
if you create a set of the input string all the individual non repetitive alphabets can be created
If you do a simple set subtraction from all ascii set to the string set created 
If you find the set subtraction to be empty that simply indicates that the input string to be checked is a panagram

"""

from string import ascii_lowercase
import collections
from orderedset import OrderedSet

string='The quick brown fox the lazy dog'

set_panagram=set(string.lower())

print(set_panagram)

set_alpha=set(ascii_lowercase)

if(set_alpha-set_panagram==set([])):
    print("YES")
else:
    print("NO")
