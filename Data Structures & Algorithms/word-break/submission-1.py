class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd=set(wordDict)
        memo={}
        def dfs (i): 
            #base case 
            if i in memo: 
                return memo[i]
            if i>=len(s): 
                return True 
            res=False
            for j in range(i+1,len(s)+1): 
                word=s[i:j]
                if word in wd: 
                    res=res or dfs(j)
            memo[i]=res
            return res 
        return dfs(0)