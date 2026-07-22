class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        look_up = defaultdict(list)

        for word in strs: 
            ch_arr = [0]*26 

            for ch in word: 
                ch_arr[ord(ch)-ord('a')]+=1 
            key = tuple(ch_arr)
            look_up[key].append(word)

        result = []
        for value in look_up.values():
            result.append(value) 
        
        return result 
        