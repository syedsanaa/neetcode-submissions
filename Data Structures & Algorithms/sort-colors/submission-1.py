class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=defaultdict(int)
        for num in nums: 
            count[num]+=1 
        for i in range(len(nums)): 
            if count[0]!= 0 : 
                count[0]-=1 
                nums[i]=0
            elif count[1]!=0: 
                count[1]-=1
                nums[i]=1
            elif count[2]!=0: 
                count[2]-=1
                nums[i]=2
        