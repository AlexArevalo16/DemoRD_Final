
# Libs imported
import sys
import json
from collections import Counter

# parameter to expect a value
word = sys.argv[1]

# function to check how many times is repeated the letters
def times_letter(word):
    times = {}
    for i in word:
        if i in times.keys():
            times[i] += 1
        else:
            times[i] = 1
    return times

"""
Function recieve a parameter that you enter, and use a reversed to check 
if the word is the same > to right and to the < left
"""
"""
Use a variable a = bool(variable)
"""
def palindrome(word):
    re_verse =''.join(reversed(word))
    b = bool(re_verse)
    if word == re_verse:
        print("")
        #print("The word is palindrome, you enter: " + word)
        #print("")
        r1 = {'name':f"{word}", 'palindrome': True, 'sorted': times_letter(word)}
        r1.update({'length': len(word)})
        return json.dumps(r1, indent=0)
    else:
        #print("")
        #print("The word isn't palindrome, you enter: " + word)
        print("")
        r1 = {'name':f"{word}", 'palindrome': False}
        return json.dumps(r1, indent=0)
print(palindrome(word))
