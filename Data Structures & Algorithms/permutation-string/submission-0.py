class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_1 = [0] * 26
        count_2 = [0] * 26
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2:
            return False
        
        for i in range(n1):
            count_1[ord(s1[i]) - 97] += 1    
            count_2[ord(s2[i]) - 97] += 1
        
        if count_1 == count_2:
            return True
        
        for r in range(n1, n2):
            count_2[ord(s2[r]) - 97] += 1
            count_2[ord(s2[r - n1]) - 97] -= 1
            if count_1 == count_2:
                return True
        
        return False