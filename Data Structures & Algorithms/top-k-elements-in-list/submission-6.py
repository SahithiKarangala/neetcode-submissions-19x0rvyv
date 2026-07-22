class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        look_up={}
        for num in nums: 
            look_up[num] = look_up.get(num,0)+1 

        min_heap = [] 
        for num in look_up.keys():
            if(len(min_heap)>=k): heapq.heappushpop(min_heap,(look_up[num],num))
            else: heapq.heappush(min_heap,(look_up[num],num))
        
        result=[]
        while(min_heap):
            result.append(heapq.heappop(min_heap)[1])
        return result
