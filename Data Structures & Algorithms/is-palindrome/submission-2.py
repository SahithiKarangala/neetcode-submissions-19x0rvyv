class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0: return True
        left=0
        right=len(s)-1
        while left<=right:
            ch_left = s[left]
            ch_right = s[right]
            if not ch_left.isalnum(): 
                left+=1 
                continue
            elif not ch_right.isalnum(): 
                right-=1 
                continue 
            
            if ch_left.lower()==ch_right.lower():
                 left+=1
                 right-=1
            else: 
                return False
        
        return True


