class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        prod=1
        res=0 
        for r in range(len(nums)):
            while l<r and prod*nums[r]>=k: 
                prod/=nums[l]
                l+=1 
            if prod*nums[r]<k: 
                prod*=nums[r]
                res+=(r-l+1)
            else: 
                prod=1 
                l+=1
        return res 