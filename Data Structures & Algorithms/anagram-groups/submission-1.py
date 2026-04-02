class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup=defaultdict(list)

        for s in strs: 
            A = [0]*26 

            for ch in s: 
                A[ord(ch)-ord('a')]+=1 
            lookup[tuple(A)].append(s)
        
        return list(lookup.values())