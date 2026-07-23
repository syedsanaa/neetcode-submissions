class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count=0 
        leng=len(s)
        for r in range(leng): 
            l=r 
            while l>=0 and r<leng and s[l]==s[r]: 
                self.count+=1 
                l-=1 
                r+=1 
        for l in range(leng): 
            r=l+1 
            while l>=0 and r<leng and s[l]==s[r]:
                self.count+=1 
                l-=1 
                r+=1
        return self.count 

