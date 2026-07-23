class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        List = [[] for _ in range(len(nums) + 1)]
        for keys,values in count.items(): 
            List[values].append(keys)
        NewL=[]
        for i in range(len(List)-1,0,-1):
            for n in List[i]:
                NewL.append(n)
                if len(NewL)==k:
                    return NewL