class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        result =[]

        while(left<right):
            summation = numbers[left]+numbers[right] 
            if(summation > target): right-=1 
            elif(summation < target): left+=1 
            else :
                result.append(left+1)
                result.append(right+1) 
                break 
        return result
        