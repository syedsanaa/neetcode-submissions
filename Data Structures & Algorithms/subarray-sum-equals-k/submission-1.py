class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        haset=defaultdict(int)
        haset[0]=1 
        out=0
        total=0 
        for i in nums : 
            total+=i 
            if total-k in haset: 
                out+=haset[total-k]
            haset[total]+=1 
        return out 