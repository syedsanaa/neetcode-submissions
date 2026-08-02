class Solution:
    def rob(self, nums: List[int]) -> int:
        maxs=0
        prevmaxs= 0
        prev=-1 #index of the last element in maxs 
        for i in range(len(nums)): 
            res=max(prevmaxs+nums[i],maxs)
            temp=i 
            if prev+1!=i: 
                if res<maxs+nums[i]: 
                    res=maxs+nums[i]
                    temp=i 
            prevmaxs=maxs 
            maxs=res 
            prev=i 

        return maxs
