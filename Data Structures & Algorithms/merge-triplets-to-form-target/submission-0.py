class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res1=False 
        res2=False 
        res3=False 

        l=target[0]
        m=target[1]
        n=target[2]
        for x,y,z in triplets: 
            if x<=l and y<=m and z<=n: 
                if x==l: 
                    res1=True 
                if y==m: 
                    res2=True 
                if z==n: 
                    res3=True 
        if res1 and res2 and res3 : 
            return True 
        else: 
            return False 