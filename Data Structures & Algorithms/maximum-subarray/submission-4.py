class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        res=float('-inf')
        for i in range(1,len(nums)): 
            res=max(curr,res)
            curr=max(curr+nums[i],nums[i])

        return max(curr,res)