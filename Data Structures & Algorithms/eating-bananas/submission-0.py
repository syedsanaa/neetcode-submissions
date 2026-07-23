from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles): 
            return max(piles)
        def time(k): 
            out=0
            for p in piles: 
                out+= ceil(p/k)
            return out
        l=1
        r=max(piles)
        mink=float("inf")
        while l<r: 
            m=(l+r)//2 
            t=time(m)
            if t>h: 
                l=m+1 
            else: 
                mink=min(mink,m)
                r=m
        return mink