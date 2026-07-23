class Solution:
    def numDecodings(self, s: str) -> int:
        #self.ways=0 
        leng=len(s)
        dp={}
        def dfs(i): 
            if i in dp: 
                return dp[i]
            if i==leng: 
                return 1
            if s[i]=='0':
                return 0 
            res=dfs(i+1)
            if i+2<=leng and int(s[i:i+2])<=26: 
                res+=dfs(i+2)
            dp[i]=res
            return res 
        return dfs(0)