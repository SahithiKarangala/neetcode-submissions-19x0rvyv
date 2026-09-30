class Solution:
    def concatArrays(self, nums): 
        return [*nums,*nums]

    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = self.concatArrays(nums)
        return result