class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        count_s, count_t = {}, {}
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        
        have, need = 0, len(count_t)
        l = 0
        result, result_len = [-1, -1], float('inf')
        for r in range(len(s)):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if (r - l) + 1 < result_len: 
                    result = [l, r]
                    result_len = (r - l) + 1
                count_s[s[l]] -= 1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l , r = result
        return s[l: r+ 1] if result_len != float('inf') else ""

