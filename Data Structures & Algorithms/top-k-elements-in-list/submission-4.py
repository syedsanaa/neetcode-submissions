from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for _ in range(max(count.values())+1)]
        for key,v in count.items(): 
            freq[v].append(key)
        res=[]
        for i in range(len(freq)-1,0,-1): 
            for j in freq[i]: 
                res.append(j)
                if len(res)==k: 
                    return res