class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0 
        r=len(nums)-1 
        while l<r: 
            m=(l+r)//2 
            if nums[m]>nums[r]: 
                l=m+1 
            else: 
                r=m
        pivot=l 
        l=0
        r=len(nums)-1 
        if nums[pivot]<= target and target <= nums[r]: 
            l=pivot 
        else: 
            r=pivot-1 

        while l<=r: 
            m=(l+r)//2 
            if target>nums[m]: 
                l=m+1
            elif target<nums[m]: 
                r=m-1
            elif nums[m]==target: 
                return m 
        return -1 


        