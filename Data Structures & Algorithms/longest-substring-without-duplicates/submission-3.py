class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: 
            return 0
        l=0 
        hash={s[0]:1}
        maxl=1
        for r in range(1,len(s)): 
            while s[r] in hash and l<r: 
                del hash[s[l]]
                l+=1  
            hash[s[r]]=1 
            maxl=max(maxl,r-l+1)
        return maxl
