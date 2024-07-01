class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        ans = set()
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
        return list(ans)