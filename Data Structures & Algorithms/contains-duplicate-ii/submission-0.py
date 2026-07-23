class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash1=defaultdict(list)
        l=0
        for r in range(len(nums)): 
            if abs(r-l)>k: 
                del hash1[nums[l]]
                l+=1 
            if nums[r] in hash1: 
                return True 
            hash1[nums[r]]=0 
        return False