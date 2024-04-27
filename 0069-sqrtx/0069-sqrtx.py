class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        first = 1
        last = x
        while first <= last:
            mid = first + (last - first) // 2
            if mid < x // mid:
                first = mid + 1
            elif mid > x // mid:
                last = mid - 1
            else:
                return mid
        return last
