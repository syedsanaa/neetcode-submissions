class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        leng=len(nums)
        def dfs(i,cursum): 
            if i==leng and cursum==target: 
                return 1
            elif i>=leng: 
                return 0
            if (i,cursum) in dp: 
                return dp[(i,cursum)]
            res=dfs(i+1,cursum+nums[i])+dfs(i+1,cursum-nums[i])
            dp[(i,cursum)]=res
            return res 
        dfs(0,0)
        return dfs(0,0)

            
