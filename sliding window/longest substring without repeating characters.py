class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        unique = set()
        ans = 1
        start = 0
        end = 1
        flag = False
        while start < end and end <= len(s):
            
            if len(s[start: end]) == len(set(s[start: end])):
                if len(s[start: end])> ans:
                    ans = len(s[start:end])
                end += 1
                
                
            else:
                
                start += 1
        
            print(s[start: end])
        return ans
        