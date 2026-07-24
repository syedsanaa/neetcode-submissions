class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr=len(nums)-1
        cost=0
        res=0
        prev=0
        prevprev=0
        for r in range(len(nums)-1,-1,-1): 
            target=nums[r] 
            if r!=len(nums)-1:
                cost-=((nums[r+1]-nums[r])*(r+1-curr))
            prev=prevprev
            while curr>=1 and target-nums[curr-1]+cost<=k: 
                cost+=(target-nums[curr-1])
                curr-=1
            res=max(res,r-curr+1)
        return res 
