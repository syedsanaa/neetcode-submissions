class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h=[]
        currcap=0 
        trip=sorted(trips,key=lambda x:x[1])
        for psngr,f,t in trip: 
            while h and h[-1][0]<=f: 
                time,psngrdrop=heapq.heappop(h)
                currcap-=psngrdrop
            if currcap+psngr<=capacity: 
                currcap+=psngr
                heapq.heappush(h,[t,psngr])
            else: 
                return False 
        return True 


        