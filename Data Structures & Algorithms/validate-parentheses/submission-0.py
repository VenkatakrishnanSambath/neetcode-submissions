class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    rem = stack.pop()
                    if rem != hashmap[c]:
                        return False
        return not stack 