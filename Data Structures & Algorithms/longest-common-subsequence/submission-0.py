class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        leni=len(text1)
        lenj=len(text2)
        #out=0 
        def dfs(i,j): 
            if i>=leni or j>=lenj: 
                return 0 
            if(i,j) in dp: 
                return dp[(i,j)]
            if text1[i]==text2[j]:
                #out+=1 
                return 1+dfs(i+1,j+1)
            res1=dfs(i+1,j)
            res2=dfs(i,j+1)
            dp[(i,j)]=max(res1,res2)
            return max(res1,res2)
        return dfs(0,0)