class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]        
        
        for _ in range(numRows - 1): 
            # Minus 1 because we have make the first line ans = [[1]]
            dummy_row = [0] + ans[-1] + [0]
            row = []

            for i in range(len(ans[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i + 1])
            ans.append(row)

        return ans 
        