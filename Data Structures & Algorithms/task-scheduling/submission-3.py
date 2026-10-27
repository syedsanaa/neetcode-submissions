import heapq 
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heap=[-cnt for cnt in count.values()]
        heapq.heapify(heap)
        q=deque()
        i=0
        while heap or q:
            if heap:
                i+=1
                count=heapq.heappop(heap)
                if count+1:
                    q.append([i+n,count+1])
            else: 
                i=q[0][0]
            while q and q[0][0]<=i: 
                heapq.heappush(heap,q.popleft()[1])
        return i 




