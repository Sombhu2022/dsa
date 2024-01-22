# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true


# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 
 
# anagram::-- When any word or any block of word  writen by unorder or unsiquence maner . 
#if two string are contain same alphabate 

s1 = "sombhu"
s2 = "mohbus"

if sorted(s1) == sorted(s2):
    print("this is anagram")
else:
    print("this is not anagram")