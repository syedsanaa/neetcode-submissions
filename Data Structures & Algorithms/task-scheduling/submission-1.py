import heapq 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap=[]
        count=defaultdict(int)
        for i in tasks: 
            count[i]+=1 
        for i in count.values(): 
            heapq.heappush(heap,[0,-i])
        time=0
        while heap: 
            if heap[0][0]<=time: 
                t,freq=heapq.heappop(heap)
                if freq+1!=0:
                    heapq.heappush(heap,[t+n+1,freq+1])
            time+=1 
        return time 