class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])
        return (-result if x < 0 else result) if result.bit_length() < 32 else 0