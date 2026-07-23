class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        dp={}
        if total%2!=0: 
            return False 
        def dfs(i,currSum):
            if (i,currSum) in dp: 
                return dp[(i,currSum)]
            if currSum==(total/2): 
                return True 
            if i>=len(nums): 
                return False 
            res1=False 
            if currSum+nums[i]<=(total/2):
                 res1=dfs(i+1,currSum+nums[i])
            res2=dfs(i+1,currSum)
            dp[(i,currSum)]= (res1 or res2)
            return (res1 or res2)
        return dfs(0,0)
