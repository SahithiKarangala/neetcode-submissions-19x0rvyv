class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)): 
            if(nums[i]>0): break 
            if(i>0 and nums[i-1]==nums[i]): continue
            target = nums[i]*-1
            left = i+1 
            right = len(nums)-1

            while(left<right): 
                print(left,right)
                two_sum = nums[left]+nums[right] 
                if(two_sum == target): 
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1 
                    while(nums[left]==nums[left-1] and left<right):
                        left+=1
                elif(two_sum > target): 
                    right-=1 
                else: 
                    left+=1 
        return result 
            
        