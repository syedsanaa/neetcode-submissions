class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h=defaultdict(int)
        for i in s: 
            h[i]+=1 
        out=''
        for i in order: 
            out+=h[i]*i 
            del h[i]
        for i in h: 
            out+=i*h[i] 
        return out 
        
        