class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        ans = []
        
        def backtrack(index, curr_combinations):
            if index == len(digits):
                ans.append(curr_combinations)
                return
            
            curr_digit = digits[index]
            for l in digit_to_letter[curr_digit]:
                backtrack(index + 1, curr_combinations + l)
        
        backtrack(0, "")
        return ans
        
    
        
        