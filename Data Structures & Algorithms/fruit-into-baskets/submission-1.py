class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket=defaultdict(int)
        l=0 # l is inclusive 
        res=0
        for r in range(len(fruits)): 
            basket[fruits[r]]+=1 
            if len(basket)==2: 
                res=max(res,sum(basket.values()))
            while len(basket)>2: 
                basket[fruits[l]]-=1 
                if basket[fruits[l]]==0: 
                    del basket[fruits[l]]
                l+=1 
        res=max(res,sum(basket.values()))
        return res