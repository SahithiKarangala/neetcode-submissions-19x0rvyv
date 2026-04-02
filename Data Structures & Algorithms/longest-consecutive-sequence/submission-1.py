class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0 
        if len(nums)==0: return 0
        i,j=0,0 
        sorted_nums=sorted(set(nums))
        n=len(sorted_nums)
        while j+1<n : 
            if sorted_nums[j+1]-sorted_nums[j]>1: 
                max_len=max(max_len,j-i+1) 
                i=j+1 
            j=j+1
        
        return max(max_len,j-i+1)

