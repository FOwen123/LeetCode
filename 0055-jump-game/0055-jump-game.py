class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Dynamic programming approach
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        
        for i in range(n):
            if dp[i]:
                for k in range(i + 1, min(i + nums[i] + 1, n)):
                    dp[k] = True
        
        return dp[-1]
        
