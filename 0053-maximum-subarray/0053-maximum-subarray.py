class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        real_max = -inf
        
        for i in nums:
            curr_max = max(i, curr_max + i)
            real_max = max(real_max, curr_max)
        return real_max
        