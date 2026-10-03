class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target=sum(stones)
        cache={}
        def recur(i,ttl): 
            if (i,ttl) in cache: 
                return cache[(i,ttl)]
            #if ttl==(target//2): 
                #return 0  
            if i==len(stones): 
                return abs(target-ttl-ttl)
            res=min(recur(i+1,ttl+stones[i]),recur(i+1,ttl))
            cache[(i,ttl)]=res 
            return res 
        return recur(0,0)

