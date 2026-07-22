class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = len(nums)-1
        left = 0 
        num_idx = dict()

        for i in range(len(nums)): 
            n = target - nums[i] 
            if n in num_idx : return [num_idx[n],i]
            num_idx[nums[i]]=i


        
        return []