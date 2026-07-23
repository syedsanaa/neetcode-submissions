class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h=[]
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(h, (count, char))
        res=[]
        leng=0
        while h: 
            no,ch=heapq.heappop(h)
            if leng<2 or res[leng-1]!=ch or  res[leng-2]!=ch: 
                res.append(ch)
                if no+1!=0:
                    heapq.heappush(h,(no+1,ch))
            elif h: 
                no1,ch1=heapq.heappop(h)
                res.append(ch1)
                if no1+1!=0:
                    heapq.heappush(h,(no1+1,ch1))
                heapq.heappush(h,(no,ch))

            leng+=1 
        return ''.join(res)