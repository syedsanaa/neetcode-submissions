class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)
        def backtracking(i):
            if i==l-1: 
                return True  
            if i>=l: 
                return False
            for j in range(1,nums[i]+1): 
                if backtracking(i+j): 
                    return True 
            return False 
        return backtracking(0)
