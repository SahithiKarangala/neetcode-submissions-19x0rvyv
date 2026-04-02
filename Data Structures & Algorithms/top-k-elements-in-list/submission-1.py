class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        j=0
        i=0
        freq_list=[]
        while j<len(sorted_nums):
            count=0
            while i<len(sorted_nums):
                if sorted_nums[j]==sorted_nums[i]: 
                    count+=1
                else: 
                    break 
                i+=1
            freq_list.append((count,sorted_nums[j]))
            j=i
        freq_list.sort(key=lambda x: (x[0],x[1]) )
        print(freq_list)
        result=[]
        l=len(freq_list)-1
        while k>0 and l>=0:
            result.append(freq_list[l][1])
            k-=1
            l-=1
        return result
