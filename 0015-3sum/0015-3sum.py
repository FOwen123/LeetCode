class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        ans = set()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
                
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
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates
                    left += 1
                    right -= 1
                    
        return list(ans)