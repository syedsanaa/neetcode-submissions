class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        leng=len(nums)
        s=0 
        self.out=0
        def dfs(i,cursum): 
            if i==leng and cursum==target: 
                self.out+=1
                return 
            elif i==leng: 
                return 
            dfs(i+1,cursum+nums[i])
            dfs(i+1,cursum-nums[i])
        dfs(0,0)
        return self.out

            
