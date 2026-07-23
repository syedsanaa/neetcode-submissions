class Solution:
    def rob(self, nums: List[int]) -> int:
        leng=len(nums)
        dp={}
        def dfs(i): 
            if i<leng: 
                if i in dp: 
                    return dp[i]
                res=max(dfs(i+2)+nums[i],dfs(i+1))
                dp[i]=res
                return res
            return 0 
        return dfs(0)