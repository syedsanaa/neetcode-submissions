"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap=[]
        for items in sorted(intervals,key=lambda x: x.start): 
            if not heap: 
                heapq.heappush(heap, items.end)
            else: 
                if items.start>=heap[0]: 
                    heapq.heappop(heap)
                    heapq.heappush(heap, items.end)
                else: 
                    heapq.heappush(heap, items.end)
        return len(heap)