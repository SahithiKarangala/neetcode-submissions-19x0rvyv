class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)): 
            target = nums[i]*-1
            left = i+1 
            right = len(nums)-1

            while(left<right): 
                two_sum = nums[left]+nums[right] 
                if(two_sum == target): 
                    result.add((nums[i],nums[left],nums[right]))
                    left+=1
                elif(two_sum > target): 
                    right-=1 
                else: 
                    left+=1 
        l = []   
        for item in result: 
            l.append(list(item))
        return l
            
        