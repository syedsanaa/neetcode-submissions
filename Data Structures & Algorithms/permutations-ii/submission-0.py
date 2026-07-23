class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used=set()
        have=defaultdict(int)
        for i in nums: 
            have[i]+=1 
        def bactrack(out,curr): 
            if out not in used and curr==have  : 
                used.add(out)
                return 
            for key in have.keys(): 
                if curr[key]<have[key]:
                    curr[key]+=1 
                    outnew=''.join([out,str(key)])
                    bactrack(outnew,curr)
                    curr[key]-=1 
                    if curr[key]==0: 
                        del curr[key]
            return
        a=defaultdict(int)
        bactrack('',a) 
        output=[]
        for items in used : 
            output.append([int(x) for x in items])
        return output
