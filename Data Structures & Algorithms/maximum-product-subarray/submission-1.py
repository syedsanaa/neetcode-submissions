class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv=nums[0]
        minv=nums[0]
        res=nums[0]
        for i in range(1,len(nums)): 
            temp=maxv
            maxv=max(nums[i],nums[i]*maxv,nums[i]*minv)
            minv=min(nums[i],nums[i]*minv,nums[i]*temp) 
            res=max(maxv,res)
        return res 

        