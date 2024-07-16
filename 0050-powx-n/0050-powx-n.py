class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        curr = x
        
        while n > 0:
            if n & 1:
                ans *= curr
            
            curr *= curr
            
            n >>= 1
        
        return ans
            
        
        