class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = "".join(str(x) for x in digits)
        string = str(int(string) + 1)
        return [int(x) for x in string]