class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0 
        r=len(nums)-1 
        nums.append(float('-inf'))
        while l<=r: 
            m=(r+l)//2 
            if m==0 and nums[m]>nums[m+1]: 
                return 0 
            if nums[m-1]<nums[m] and nums[m+1]<nums[m]: 
                return m
            if nums[m-1]>nums[m]: 
                r=m-1
            elif nums[m+1]>nums[m]: 
                l=m+1 
        