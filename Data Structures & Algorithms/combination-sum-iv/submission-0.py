class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        leng=len(nums)
        dp={}
        def backtrack(total): 
            if total>target: 
                return 0
            if total==target: 
                return 1 
            res=0 
            if total in dp: 
                return dp[total]
            for i in nums: 
                res+=backtrack(total+i)
            dp[total]=res 
            return res 
        return backtrack(0)