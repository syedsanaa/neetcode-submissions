class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0 
        currsum=0
        minl=float("inf")
        for r in range(len(nums)): 
            currsum+=nums[r]
            while currsum>=target and l<=r: 
                minl=min(minl,r-l+1)
                currsum-=nums[l]
                l+=1 
        return 0 if minl==float("inf") else minl