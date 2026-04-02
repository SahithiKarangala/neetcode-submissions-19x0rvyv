class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print("nums=",nums)
        sorted_nums = sorted(nums)
        print("sorted nums",sorted_nums)
        result=[]
        for i in range(len(sorted_nums)-2):
            sum=sorted_nums[i]
            if sum>0: break 
            if i>0 and sorted_nums[i]==sorted_nums[i-1]: continue
            left=i+1
            right=len(sorted_nums)-1 

            while left<right: 
                total=sum+sorted_nums[left]+sorted_nums[right]
                if total>0: right-=1
                elif total<0: left+=1
                else: 
                    result.append([sorted_nums[i],sorted_nums[left],sorted_nums[right]])
                    left+=1
                    right-=1
                    while (left<right and sorted_nums[left]==sorted_nums[left-1]): left+=1

        return result