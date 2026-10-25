class Solution:
    def jump(self, nums: List[int]) -> int:
        dp={len(nums)-1:0}
        for i in range(len(nums)-2,-1,-1): 
            end=min(len(nums),i+nums[i]+1)
            res=float('inf')
            for j in range(i+1,end): 
                res=min(res,dp[j]+1)
            dp[i]=res
        return dp[0]