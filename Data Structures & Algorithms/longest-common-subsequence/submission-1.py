class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def dfs(i,j): 
            if (i,j) in dp: 
                return dp[(i,j)]
            if i==len(text1): 
                return 0
            if j==len(text2): 
                return 0
            if text1[i]==text2[j]: 
                 res=dfs(i+1,j+1)+1 
            else: 
                 res=max(dfs(i+1,j+1),dfs(i,j+1),dfs(i+1,j))
            dp[(i,j)]=res
            return res 
        return dfs(0,0)