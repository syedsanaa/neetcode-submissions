class TrieNode: 
    def __init__(self): 
        self.child={}
        self.end=False 
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for ch in word: 
            if ch not in cur.child:
                cur.child[ch]=TrieNode()
            cur=cur.child[ch]
        cur.end=True 
    def search(self, word: str) -> bool:
        def dfs(i,root): 
            cur=root
            if i>=len(word): 
                return cur.end
            if word[i] in cur.child: 
                return dfs(i+1,cur.child[word[i]])
            elif word[i]=='.': 
                for c in cur.child.values(): 
                    if dfs(i+1,c): 
                        return True
            return False 
        return dfs(0,self.root)




            