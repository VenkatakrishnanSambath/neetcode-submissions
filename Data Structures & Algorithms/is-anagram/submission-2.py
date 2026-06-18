class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
        for j in range(len(t)):
            countT[t[j]] = countT.get(t[j], 0) + 1
        print('CountT: ',countT)
        print('CountS: ', countS)
        return countS == countT

soln = Solution()
s = 'racecar'
t = 'carrace'
soln.isAnagram(s, t)