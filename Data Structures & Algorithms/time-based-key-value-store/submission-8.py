class TimeMap:

    def __init__(self):
        self.out=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
       self.out[key].append([value,timestamp])

    def bs(self,sortl,ts): 
        l=0
        r=len(sortl)-1
        while l<=r: 
            m=(r+l)//2
            if sortl[m][1]==ts: 
                return sortl[m][0]
            if sortl[m][1]<ts:
                l=m+1
            else:
                r=m-1
        if r>=0 and sortl[r][1]<=ts: 
            return sortl[r][0]
        else: 
            return ''

    def get(self, key: str, timestamp: int) -> str:
        return self.bs(self.out[key],timestamp)
        
