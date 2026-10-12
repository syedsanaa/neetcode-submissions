class Treenode: 
    def __init__(self): 
        self.child={}
        self.end=False
class PrefixTree:

    def __init__(self):
        self.root=Treenode()

    def insert(self, word: str) -> None:
        curr=self.root
        for ch in word: 
            if ch not in curr.child:
                curr.child[ch]=Treenode()
            curr=curr.child[ch] 
        curr.end=True


    def search(self, word: str) -> bool:
        curr=self.root
        for ch in word: 
            if ch not in curr.child: 
                return False 
            curr=curr.child[ch]   
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for ch in prefix: 
            if ch not in curr.child: 
                return False 
            curr=curr.child[ch] 
        return True
        