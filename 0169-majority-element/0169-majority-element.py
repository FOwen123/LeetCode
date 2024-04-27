class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore Voting Algorithm 
        # The algorithm starts by assuming the first element as the majority candidate and sets count to 1, and through traversing the array it will compare the candidate, if it is different, it will decrement the count by 1, if it is the same, it will increment the count by 1. At the end of it, you will find the majority element

        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
            
