class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp={}
        def dfs(i,j,ind): 
            if (i,j,ind) in dp: 
                return dp[(i,j,ind)]
            if i==0 and j==0: 
                return 0
            if ind>=len(strs): 
                return 0
            one=sum(int(d) for d in strs[ind])
            zero=len(strs[ind])-one
            res=dfs(i,j,ind+1)
            if one<=i and zero<=j: 
                res=max(res,dfs(i-one,j-zero,ind+1)+1)
            dp[(i,j,ind)]=res
            return res 
        return dfs(n,m,0)