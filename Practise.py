from string import ascii_lowercase
import collections
from orderedset import OrderedSet

string='The quick brown fox the lazy dog'

set_panagram=set(string.lower())

print(set_panagram)

set_alpha=set(ascii_lowercase)

if(set_alpha-set_panagram==set([])):
    print("is")
else:
    print("isnot")
