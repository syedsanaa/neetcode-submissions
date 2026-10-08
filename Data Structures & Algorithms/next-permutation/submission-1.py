class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]: 
            i-=1 
        if i==-1: 
            nums.reverse()
            return 
        for j in range(len(nums)-1,i,-1): 
            if nums[j]>nums[i]: 
                nums[i],nums[j]=nums[j],nums[i]
                break 
        j=len(nums)-1 
        i+=1 
        while i<j: 
            nums[i],nums[j]=nums[j],nums[i]
            i+=1 
            j-=1 
        return 