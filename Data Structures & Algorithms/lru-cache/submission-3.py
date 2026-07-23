class Node: 

     def __init__(self,key,val): 
        self.prev= None 
        self.nex= None 
        self.key=key 
        self.val=val 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.cap=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.nex,self.right.prev=self.right,self.left

    def remove(self,node): 
        node.prev.nex,node.nex.prev=node.nex,node.prev

    def insert(self,node): 
        prev=self.right.prev 
        prev.nex=self.right.prev=node
        node.prev,node.nex=prev,self.right

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else: 
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap: 
            lru=self.left.nex
            self.remove(lru)
            del self.cache[lru.key]


        
