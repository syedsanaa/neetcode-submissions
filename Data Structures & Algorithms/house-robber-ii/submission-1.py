class Solution:
    def rob(self, nums: List[int]) -> int:
        leng=len(nums)
        if leng==1: 
            return nums[0]
        def dfs(i,length): 
            if i<length: 
                if i in dp: 
                    return dp[i]
                res=max(dfs(i+2,length)+nums[i],dfs(i+1,length))
                dp[i]=res 
                return res 
            return 0 
        dp={}
        a=dfs(0,leng-1)
        dp={}
        b=dfs(1,leng)
        return max(a,b)