class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict() 
        for i in range(len(nums)): 
            difference = target - nums[i]
            if difference in lookup: return [lookup.get(difference), i]
            else: lookup[nums[i]]=i