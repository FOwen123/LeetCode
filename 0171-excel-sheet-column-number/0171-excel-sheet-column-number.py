class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # ord is a method in python to return the Unicode code of the letter

        result = 0
        for i in columnTitle:
            # 64 is from ord(i) - ord('A') + 1 = ord(i) - 65 + 1
            
            result = result * 26 + (ord(i) - 64)
        
        return result