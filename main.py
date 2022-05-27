# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


# def find_anagrams(word):
#     # [assignment] Add your code here

#     return True


# Python3 program for the above approach
 
# function to check if two strings are
# anagram or not
def check(firstwor, secondword):
   
    # implementing counter function
    if(sorted(firstword.replace(" ", "").lower()) == sorted(secondword.replace(" ", "").lower())):
        return True
    else:
        return False
 
 
 
# driver code
word1 = input("Write a word or sentence: ")
word2 = input("Write the second word or sentence: ")
print(check(word1, word2))


