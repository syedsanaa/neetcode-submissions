class StockSpanner:

    def __init__(self):
        self.s=deque()
        self.span={}
        

    def next(self, price: int) -> int:
        temp=1
        while self.s and self.s[-1]<=price: 
            e=self.s.pop()
            temp+=self.span[e]
        self.span[price]=temp 
        self.s.append(price)
        return temp 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)