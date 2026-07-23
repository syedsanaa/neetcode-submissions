from math import ceil
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days==1: 
            return sum(weights)
        def day(minc): 
            days=1  
            s=0
            for w in weights: 
                if s+w>minc: 
                    days+=1
                    s=0 
                s+=w
            return days 

        l=max(weights)
        r=sum(weights)
        mind=sum(weights)
        while l<r: 
            m=(l+r)//2 
            d=day(m)
            if d>days: 
                l=m+1 
            else:  
                mind=min(mind,m)
                r=m
        return mind