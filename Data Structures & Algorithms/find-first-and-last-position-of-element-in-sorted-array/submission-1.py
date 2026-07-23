class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0 
        r=len(nums)-1 
        if len(nums)==0: 
            return [-1,-1]
        while l+1!=r and l<r : 
            m=(r+l)//2 
            if nums[m]>target: 
                r=m-1 
            elif nums[m]<target: 
                l=m+1 
            else: 
                l=m  
        last=None
        if nums[l]==target and nums[r]==target: 
            last=r 
        elif nums[l]==target: 
            last=l 
        elif nums[r]==target: 
            last=r
        l=0 
        r=len(nums)-1 
        while l+1!=r and l<r : 
            m=(r+l)//2 
            if nums[m]>target: 
                r=m-1 
            elif nums[m]<target: 
                l=m+1 
            else: 
                r=m 
        first=None 
        if nums[l]==target and nums[r]==target: 
            first=l 
        elif nums[l]==target: 
            first=l 
        elif nums[r]==target: 
            first=r
        if first!=None and last!=None:
            return [first,last]
        else: 
            return [-1,-1]