class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0 
        right=len(heights)-1 
        curr = float("-inf")

        while(left<right): 
            curr = max((right-left)*min(heights[left],heights[right]),curr)
            if(heights[left]<heights[right]): 
                left+=1 
            else: right-=1 
        
        return curr