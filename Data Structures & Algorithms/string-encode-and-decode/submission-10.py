class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs: 
            n = len(s)
            encoded_string+=str(n)+"#"+s
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        curr=""
        i=0
        while(i<len(s)):
            if(s[i]=="#"): 
                length = int(curr)
                decoded_string.append(s[i+1:i+1+length])
                i=i+length
                curr=""
            else: 
                curr+=s[i]
            i+=1
                
        return decoded_string;
