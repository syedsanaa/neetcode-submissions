class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l,r=0,0 
        minh=[]
        maxh=[]
        res=0
        for r in range(len(nums)): 
            heapq.heappush(minh,[nums[r],r])
            heapq.heappush(maxh,[-nums[r],r])
            while -maxh[0][0]-minh[0][0]>limit and l<r : 
                l+=1 
                while maxh[0][1]<l: 
                    heapq.heappop(maxh)
                while minh[0][1]<l: 
                    heapq.heappop(minh)
            res=max(res,r-l+1)
        return res 




