class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for i in nums: 
            d[i]+=1 
        heap=[]
        for a,v in d.items(): 
            heapq.heappush(heap,(-v,a))
        i=0 
        out=[]
        while heap and i<k: 
            v,a=heapq.heappop(heap)
            out.append(a)
            i+=1
        return out 