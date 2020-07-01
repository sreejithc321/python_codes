class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =  0
        right = 0
        result = 0
        seen = []    
        size = len(s)
        
        while(left < size and right < size):
            char = s[right]
            if char in seen:
                left = left + 1
                right = left
                seen = []
            else:
                seen.append(char)
                right = right + 1
            result = max(result, right - left)
        return result
                
        
