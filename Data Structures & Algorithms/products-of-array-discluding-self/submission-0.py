class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n 

        #prefix product goes from left to right
        i=n-2
        while(i>=0):
            prefix[i]=prefix[i+1]*nums[i+1]
            i-=1 
        #suffix product goes from right to left
        j=1 
        while(j<n):
            suffix[j]=suffix[j-1]*nums[j-1]
            j+=1 
        
        result=[1]*n
        for index in range(n):
            result[index]=prefix[index]*suffix[index]

        return result