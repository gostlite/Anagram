# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


# def find_anagrams(word):
#     # [assignment] Add your code here

#     return True


# Python3 program for the above approach
from collections import Counter
 
# function to check if two strings are
# anagram or not
def check(word1, word2):
   
    # implementing counter function
    if(Counter(word1) == Counter(word2)):
        return True
    else:
        return False
 
 
# driver code
s1 = "listen"
s2 = "silent"
print(check(s1, s2))


