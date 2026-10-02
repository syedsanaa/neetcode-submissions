class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: 
            return False 
        hand.sort()
        count=defaultdict(int)
        for i in hand: 
            count[i]+=1 
        while count: 
            least=min(count.keys())
            for i in range(least,least+groupSize): 
                if not count[i]: 
                    return False 
                count[i]-=1 
                if count[i]==0: 
                    del count[i]
        return True 



