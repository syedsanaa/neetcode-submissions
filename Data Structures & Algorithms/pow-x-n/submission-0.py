class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache={}
        def recur(n): 
            if n in cache: 
                return cache[n]
            if n==1 : 
                return x
            if n==0: 
                return 1 
            res=0
            if n%2==0: 
                res=recur(n/2)*recur(n/2)
            else:
                res=recur((n-1)/2)*recur((n-1)/2)*x 
            
            cache[n]=res 
            return res 
        if n>0:
            return recur(n)
        else: 
            return 1/recur(-n)