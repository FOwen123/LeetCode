class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        maxLength = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right

        return maxLength

        