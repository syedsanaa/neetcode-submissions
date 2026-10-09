class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        res=float('-inf')
        for i in range(len(nums)): 
            curr=max(curr+nums[i],nums[i])
            res=max(curr,res)
        return max(curr,res)