class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)): 
            l=i+1 
            r=len(nums)-1
            if nums[i]>0: 
                return res
            if i>0 and nums[i-1]==nums[i]: 
                continue 
            while l<r: 
                if nums[l]+nums[r]>-nums[i]: 
                    r-=1 
                elif nums[l]+nums[r]<-nums[i]: 
                    l+=1
                else: 
                    res.append([nums[i],nums[l],nums[r]])
                    while l<len(nums)-1 and nums[l]==nums[l+1]:
                        l+=1
                    l+=1 
        return res 