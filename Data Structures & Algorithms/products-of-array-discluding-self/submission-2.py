class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1]*n
        prefix = nums[0]

        for i in range(1,n): 
            arr[i] = arr[i]*prefix
            prefix*=nums[i]
        
        prefix = nums[n-1] 
        for i in range(n-1-1,-1,-1): 
            arr[i] = arr[i]*prefix 
            prefix*=nums[i] 

        return arr
        