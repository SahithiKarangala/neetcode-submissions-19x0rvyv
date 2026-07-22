class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        result_min_heap = []
        nums.sort()
        while(left<len(nums)): 
            curr = nums[left]
            right = left 
            count=0
            while(right<len(nums)and nums[right]==curr): 
                if(nums[right]==curr): count+=1
                right+=1
            if(len(result_min_heap)>=k): heapq.heappushpop(result_min_heap,(count,curr))
            else: heapq.heappush(result_min_heap,(count,curr))
            left=right
        result = [] 
        while(result_min_heap): 
            freq,val = heapq.heappop(result_min_heap)
            result.append(val)
        return result
