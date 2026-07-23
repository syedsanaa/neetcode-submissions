class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0 
        out=0
        r=len(people)-1 
        while r>=l: 
            if people[l]+people[r]<=limit: 
                l+=1
            out+=1  
            r-=1
        return out 