# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string ='' #create a new empty string .
        for i in s.lower():
            if i.isalnum(): #isalnum() is use to only accept alphanumaric words 
                string += i  
        def palindrom(i,string):
            if i>=len(string)/2: return True
            if string[i] != string[len(string)-i-1]: return False
            return palindrom(i+1,string)

        return palindrom(0,string)
        