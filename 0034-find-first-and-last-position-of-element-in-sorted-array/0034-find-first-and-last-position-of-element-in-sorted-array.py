class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
                    
            return left
        
        def find_last(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return right
        
        first = find_first(nums, target)
        last = find_last(nums, target)
        
        if first <= last and first < len(nums) and nums[first] == target:
            return [first, last]
        else:
            return [-1, -1]