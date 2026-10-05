class Solution:
    def integerBreak(self, n: int) -> int:
        cache=defaultdict(int)
        def recur(num): 
            if num in cache: 
                return cache[num]
            if num==1: 
                return 1 
            res=0 if num == n else num
            for i in range(1,num): 
                res=max(res,recur(i)*recur(num-i))
            cache[num]=res
            return res 
        return recur(n)