class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        # XOR, short for "exclusive or," is a logical operation that takes two binary values as input and returns a binary value as output. 
        for i in nums:
            xor ^= i
        
        return xor
