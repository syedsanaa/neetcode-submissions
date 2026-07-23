class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for n in nums: 
            if len(h)<k: 
                heapq.heappush(h,n)
            else: 
                if h[0]<n: 
                    heapq.heappop(h)
                    heapq.heappush(h,n)
        return h[0]
        