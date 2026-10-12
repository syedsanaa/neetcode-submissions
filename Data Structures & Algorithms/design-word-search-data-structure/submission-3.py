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
        def dfs(root,i): 
            if i==len(word): 
                return root.end
            if word[i] in root.child: 
                return dfs(root.child[word[i]],i+1)
            if word[i]=='.': 
                for values in root.child.values():
                    if dfs(values,i+1): 
                        return True 
            return False 
        return dfs(self.root,0)

            