class Solution:
    def longestPalindrome(self, s: str) -> str:
        leng=len(s)
        maxl=0 
        ml=0
        mr=0
        for i in range(leng): 
            r=l=i 
            while l>=0 and r<leng and s[l]==s[r]:
                if maxl<r-l+1: 
                    maxl=r-l+1
                    ml=l 
                    mr=r 
                l-=1 
                r+=1 
            l=i 
            r=i+1 
            while l>=0 and r<leng and s[l]==s[r]:
                if maxl<r-l+1: 
                    maxl=r-l+1
                    ml=l 
                    mr=r 
                l-=1 
                r+=1 
        return s[ml:mr+1]
                