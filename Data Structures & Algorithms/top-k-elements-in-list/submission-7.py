class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #idea is to store the [freq,ele] in a minheap
        #hence, when size of the min heap reaches k, 
        #we push [freq,ele] and pop the min frq element. 
        #This way, we keep removing the elements with min frequency
        # from min heap while maintaining k most frequent elements. 
        # Approach: create a hashmap with key=ele and value=ele's freq 
        #time complexity: O(n) for iterating throught the list + O(m)*O(logm) iterating through hashmap
        #m is the number of unique elements in nums

        lookup = dict()

        for ele in nums: 
            lookup[ele] = lookup.get(ele,0)+1 
        
        minHeap = []
        for key,val in lookup.items():
            if(len(minHeap)==k): 
                heapq.heappushpop(minHeap, (val,key))
            else: 
                heapq.heappush(minHeap,(val,key))
        result=[]
        while(len(minHeap)>0):
            result.append(heapq.heappop(minHeap)[1])
        
        return result
        
