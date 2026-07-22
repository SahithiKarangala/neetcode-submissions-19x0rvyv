class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False 
        hash_mp = dict()
        for ch in s: 
            hash_mp[ch]= hash_mp.get(ch,0)+1 
        
        for ch in t: 
            if(not (ch in hash_mp.keys())): return False
            hash_mp[ch]= hash_mp.get(ch,0)-1 
        
        for value in hash_mp.values():
            if(value) != 0: return False 
        
        return True

        