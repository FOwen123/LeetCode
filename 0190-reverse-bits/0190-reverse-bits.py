class Solution:
    def reverseBits(self, n: int) -> int:
        # Bit wise operator
        # AND('&'), OR('|'), XOR('^'), NOT('~'), Left Shift('<<'), Right Shift('>>')

        result = 0

        for i in range(32):
            # shift the result to the left side and check if the right most bit in the original integer is 1
            result = (result << 1) + (n & 1)
            # shift the original bit to the right
            n = n >> 1 # n >>= 1
        
        return result
