class TrieNode: 
    def __init__(self): 
        self.children={}
        self.end=False 
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root 
        for c in word: 
            if c not in cur.children: 
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.end=True 

    def search(self, word: str) -> bool:
        def find(i,cur):
            if i==len(word) : 
                return cur.end 
            if word[i]!='.' and word[i] in cur.children: 
                return find(i+1,cur.children[word[i]])
            elif word[i]!='.' and word[i] not in cur.children:
                return False 
            elif word[i]=='.': 
                res=False 
                for suitors in cur.children: 
                    res= (res or find(i+1,cur.children[suitors]))
                return res 
        return find(0,self.root)
