class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        res=curr
        least=curr
        for i in range(1,len(nums)): 
            curr+=nums[i]
            res=max(res,curr,curr-least)
            least=min(least,curr)
        return res