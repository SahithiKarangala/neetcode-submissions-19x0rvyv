class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)
        if(n==0):
            return 0
        if(n==1):
            return 1 

        nums.sort() 
        length = 1
        curr = 1
        i=1 
        while(i<n): 
            diff = nums[i]-nums[i-1] 
            if(diff == 1):
                curr+=1 
            elif(diff > 1):
                length = max(curr,length) 
                curr = 1
            i+=1 
        
        length = max(curr,length)

        return length

        