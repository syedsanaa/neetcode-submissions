class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp={}
        def dfs(l,r): 
            if (l,r) in dp: 
                return dp[(l,r)]
            if l>r: 
                return 0 
            if l==r: 
                return 1 
            res=0 
            if s[l]==s[r] : 
                res= max(dfs(l+1,r-1)+2,res)
            else:
                res=max(res,dfs(l+1,r))
                res=max(res,dfs(l,r-1))
            dp[(l,r)]=res
            return res 
        return dfs(0,n-1)