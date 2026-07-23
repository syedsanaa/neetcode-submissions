class Solution:
    def reorganizeString(self, s: str) -> str:
        h=[]
        count=defaultdict(int)
        for i in s: 
            count[i]+=1 
        for k,v in count.items(): 
            heapq.heappush(h,(-v,k))
        temp=()
        out=''
        while h: #check
            value,string=heapq.heappop(h)
            out += string
            if temp!=():
                heapq.heappush(h,temp)
                temp=()
            if value+1!=0:
                temp=(value+1,string)
        return out if len(out)==len(s) else ""


        