class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxk=float("-inf")
        mink=float("inf")
        cmax=float("-inf")
        cmin=float("inf")
        for i in range(len(nums)): 
            if cmax+nums[i]>nums[i]: 
                cmax+=nums[i]
            else: 
                cmax=nums[i]
            maxk=max(maxk,cmax)
            if cmin+nums[i]<nums[i]: 
                cmin+=nums[i]
            else: 
                cmin=nums[i]
            mink=min(mink,cmin)
        if mink==sum(nums): 
            return maxk 
        else: 
            return max(maxk,sum(nums)-mink)