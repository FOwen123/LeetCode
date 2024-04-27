class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Check only the 1 bits, by subtracting the n with 1
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count