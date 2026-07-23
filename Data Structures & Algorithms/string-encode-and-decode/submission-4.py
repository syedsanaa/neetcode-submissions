class Solution:

    def encode(self, strs: List[str]) -> str:
        out=''
        for i in strs: 
            out=''.join([out,str(len(i)),'#',i])
        return out 

    def decode(self, s: str) -> List[str]:
        i=0
        out=[]
        while i<len(s): 
            j=''
            while s[i]!='#': 
               j=''.join([j,s[i]])
               i+=1 
            j=int(j)
            i+=1
            temp=''
            while j>0: 
                temp=''.join([temp,s[i]])
                i+=1
                j-=1
            out.append(temp)
        return out
            

