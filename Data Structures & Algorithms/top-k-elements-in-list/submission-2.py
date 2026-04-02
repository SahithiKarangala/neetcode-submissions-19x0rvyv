class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}

        for ele in nums: 
            lookup[ele]=lookup.get(ele,0)+1 
        
        min_heap=[] 
        for key in lookup.keys():
            heapq.heappush(min_heap,(lookup[key],key))

            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        result=[] 
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])
        return result
