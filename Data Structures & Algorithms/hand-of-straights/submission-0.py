class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h=defaultdict(int)
        for i in hand: 
            h[i]+=1
        minh=list(h.keys())
        heapq.heapify(minh)
        while minh:
            first =minh[0]
            for i in range(first,first+groupSize): 
                if h[i]!=0: 
                    h[i]-=1 
                    if h[i]==0: 
                        heapq.heappop(minh)
                else: 
                    return False 
        return True 




        


