class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                quotient += 1 << i
                dividend -= divisor << i
        
        if negative:
            quotient = -quotient
        
        return min(max(-2 ** 31, quotient), 2 ** 31 - 1)
                
        