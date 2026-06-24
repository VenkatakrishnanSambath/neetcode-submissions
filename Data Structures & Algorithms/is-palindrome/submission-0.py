class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if str.isalnum(c))
        s = s.lower()
        rev = ''
        for i in range(len(s)):
            j = -i - 1
            rev += s[j] 
        return rev == s
                
        