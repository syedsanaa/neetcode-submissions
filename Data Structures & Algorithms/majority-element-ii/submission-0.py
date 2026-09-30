class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)
        for i in nums: 
            count[i]+=1 
        res=[]
        target=len(nums)//3
        for keys,values in count.items(): 
            if values>target:
                res.append(keys)
        return res 