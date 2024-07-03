class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        mid = (len(merged) - 1) // 2
        med = 0
        
        if len(merged) % 2 == 0:
            med = (merged[mid] + merged[mid + 1]) / 2
        else:
            med = merged[mid]
        
        return med
        
    
    def merge(self, left, right):
        a = []
        l = 0
        r = 0
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                a.append(left[l])
                l += 1
            else:
                a.append(right[r])
                r += 1
                
        while l < len(left):
            a.append(left[l])
            l += 1
            
        while r < len(right):
            a.append(right[r])
            r += 1
        
        return a
            