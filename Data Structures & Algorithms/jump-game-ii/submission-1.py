class Solution:
    def jump(self, nums: List[int]) -> int:
        self.min=10000000000000000
        l=len(nums)
        def backtracking(i,c): 
            if i==l-1: 
                self.min= min(self.min,c)
                return 
            if i>=l: 
                return
            for j in range(1,nums[i]+1): 
                 backtracking(i+j,c+1) 
            return
        backtracking(0,0)
        return self.min