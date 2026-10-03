class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0 
        r=len(nums)-1
        while l<r:
            m=(l+r)//2 
            if nums[m]==target: 
                return m 
            if nums[l]<=nums[m]:
                if nums[l]<=target and nums[m]>=target: 
                    r=m-1
                else: 
                    l=m+1 
            else:
                if nums[m]<target and nums[r]>=target: 
                    l=m+1
                else: 
                    r=m-1
        if nums[l]==target: 
            return l 
        if nums[r]==target: 
            return r 
        else: 
            return -1
        
            