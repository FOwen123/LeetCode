class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if m < i:
                return False
            m = max(m, i + n)
        return True
        