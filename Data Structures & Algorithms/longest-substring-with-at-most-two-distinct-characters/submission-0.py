class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l=0 
        leng=len(s)
        d=defaultdict(int)
        maxl=0
        for r in range(len(s)): 
            d[s[r]]+=1 
            if len(d)<=2: 
                maxl=max(maxl,r-l+1)
            else: 
                while l<leng and len(d)>2: 
                    d[s[l]]-=1  
                    if d[s[l]]==0: 
                        del d[s[l]]
                    l+=1
        return maxl
            