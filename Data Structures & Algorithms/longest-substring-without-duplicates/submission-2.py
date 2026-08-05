class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup_set = set() 
        max_len=0
        left = 0
        
        for i in range(len(s)): 
            while s[i] in lookup_set:
                lookup_set.remove(s[left]) 
                left+=1 
            max_len = max(max_len,i-left+1)
            
            lookup_set.add(s[i])
        return max_len
                