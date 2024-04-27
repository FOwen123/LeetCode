class Solution:
    def myAtoi(self, s: str) -> int:
        # You can use this by using DFA (Deterministic Finite Automation) is a state machine that either accepts or rejects a sequence of symbols by running through a state sequence uniquely determined by the string. But below I use a normal way. 

        length = len(s)
        n = 0
        sign = +1
        ans = ""

        max_value = 2 ** 31 - 1
        min_value = -2 ** 31 

        while n < length and s[n] == " ": 
            n += 1

        if n < length and s[n] in ("-", "+"):
            sign = -1 if s[n] == "-" else +1
            n += 1
            
        while n < length and s[n].isdigit():
            ans += s[n]
            n += 1
        
        return max(min_value, min(int(ans or 0) * sign, max_value))