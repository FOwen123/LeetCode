class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        interval = sorted(intervals)
        
        while i < len(interval):
            start = interval[i][0]
            end = interval[i][1]
            
            while i + 1 < len(interval) and end >= interval[i + 1][0]:
                start = min(start, interval[i + 1][0])
                end = max(end, interval[i + 1][1])
                i += 1
        
            ans.append([start, end])
            i += 1
            
        return ans
            
        