class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=r=0 
        # l is first available place
        count=0
        curr=nums[0]
        for r in range(len(nums)): 
            if nums[r]==curr and count<2: 
                nums[l]=nums[r]
                l+=1 
                count+=1  
            elif nums[r]!=curr: 
                count=1  
                nums[l]=nums[r]
                l+=1 
                curr=nums[r]
        return l 