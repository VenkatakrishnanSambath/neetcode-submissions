from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in '+-*/':
                b, a = s.pop(), s.pop()

                if t == '+':
                    s.append(a + b)
                if t == '-':
                    s.append(a - b)
                if t == '*':
                    s.append(a * b)
                if t == '/':
                    division = a / b
                    if division < 0:
                        s.append(ceil(a / b))
                    if division > 0:
                        s.append(floor(a / b))
                    if division == 0:
                        s.append(int(a / b))
            else:
                s.append(int(t))
        return s[0]