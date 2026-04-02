class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        
        s=""
        for ele in strs: 
            length=len(ele)
            s+=str(length)+"#"+ele 
        
        return s


    def decode(self, s: str) -> List[str]:
        print("string is",s)
        result=[]
        i=0
        while i<len(s): 
            j=i 
            while s[j] != "#":
                j+=1 
            
            length=int(s[i:j])
            end_of_string=j+1+length
            string=s[j+1:end_of_string]
            i=end_of_string

            result.append(string)
            
        return result