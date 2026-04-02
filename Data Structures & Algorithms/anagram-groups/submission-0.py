class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup=dict()

        for s in strs: 
            string = "".join(sorted(s))
            if string in lookup: lookup[string].append(s)
            else: lookup[string] = [s]
        
        result=[]
        for key in lookup: 
            result.append(lookup[key])

        return result