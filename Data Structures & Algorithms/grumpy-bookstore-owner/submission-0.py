class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sat=0
        n=len(customers) 
        for i in range(n): 
            if grumpy[i]==0:
                sat+=customers[i]
        l=r=0
        maxs=0 
        runs=0 
        while r<n: 
            runs+=customers[r]*grumpy[r]
            if r-l+1==minutes: 
                maxs=max(maxs,runs)
                runs-=customers[l]*grumpy[l]
                l+=1
            r+=1 
        return sat+maxs
         
        