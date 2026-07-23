class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==1: 
            return s
        d=defaultdict(list)
        for i in range(numRows): 
            index=i 
            jump=2*numRows-2
            while index<len(s): 
                d[i].append(s[index])
                j=jump-2*i
                if i!=0 and i!=numRows-1 and index+j<len(s): 
                    d[i].append(s[index+j])
                index+=jump
        return ''.join(''.join(v) for v in d.values())
        