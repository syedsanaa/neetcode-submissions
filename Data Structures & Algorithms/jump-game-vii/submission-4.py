class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        leng=len(s)
        dp={} 
        def backtracking(i):
            if i in dp: 
                return dp[i]
            if i>=leng or s[i]!='0': 
                return False 
            if i==leng-1: 
                return True 
            for j in range(maxJump,minJump-1,-1):
                res=backtracking(i+j)
                dp[i]=res
                if res: 
                    return True 
            return False 
        return backtracking(0)