class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for i in range(len(nums)): 
            A.append([nums[i],i])
        
        A.sort() 

        x=0
        y=len(A)-1
        while(y>x):
            sum = A[x][0]+A[y][0]
            if sum==target : return [min(A[x][1],A[y][1]),max(A[x][1],A[y][1])]
            elif sum>target: y-=1 
            else: x+=1 
        return [] 
        