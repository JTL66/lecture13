import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dict = collections.Counter(s)#dictionary to hold the counts
        
        #if we have more than one count that is odd, then 
        #the string permutation cannot be turned into a palindrome
        odds = 0
        for v in dict.values():
            odds+=v%2
            
        return odds <= 1