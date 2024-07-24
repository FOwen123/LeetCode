class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        
        for s in strs:
            sort = "".join(sorted(s))
            anagram[sort].append(s)
        
        return list(anagram.values())