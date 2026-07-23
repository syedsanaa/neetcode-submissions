class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq=defaultdict(int)
        for i in s: 
            freq[i]+=1 
        part=defaultdict(int)
        out=[]
        add=True
        for i in s:
            add=True
            part[i]+=1  
            for k,v in part.items(): 
                if freq[k]!=v: 
                    add=False 
            if add: 
                out.append(sum(part.values())) 
                part=defaultdict(int)
                add=True 
        return out 


            
                         


        