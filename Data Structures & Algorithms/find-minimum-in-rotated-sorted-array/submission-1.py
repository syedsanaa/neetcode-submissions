class Solution:
    def findMin(self, nums: List[int]) -> int:
        r=len(nums)-1
        l=0
        while r-l>1: 
            m=(l+r)//2 
            if nums[m]<nums[l]: 
                r=m
            elif nums[m]>nums[r]: 
                l=m
            else: 
                r=l
        return min(nums[l],nums[r])