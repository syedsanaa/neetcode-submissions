class Solution:
    def largestGoodInteger(self, num: str) -> str: 
        no=defaultdict(int)
        res='-1'
        for i in num:
            if i in no and no[i]+1==3 : 
                res=str(max(int(res),int(i))) 
                no=defaultdict(int)
            elif i in no or len(no)==0 : 
                no[i]+=1 
            else: 
                no=defaultdict(int)
                no[i]+=1 
        return '' if res=='-1' else res*3