class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0: return True
        string=""
        rev_string=""
        for ch in s:
            if ch.isalpha(): 
                string+=ch.lower()
                rev_string=ch.lower()+rev_string 
            elif ch.isdecimal(): 
                string+=ch
                rev_string=ch+rev_string
            else:continue
        return rev_string==string