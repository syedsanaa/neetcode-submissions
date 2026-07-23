class TreeNode():
    def __init__(self): 
        self.child={}
        self.word=False 
class WordDictionary:

    def __init__(self):
        self.root=TreeNode()
        

    def addWord(self, word: str) -> None:
        temp=self.root
        for ch in word: 
            if ch not in temp.child: 
                temp.child[ch]=TreeNode()
            temp=temp.child[ch]
        temp.word=True 
        

    def search(self, word: str) -> bool:

        def dfs(i,root): 
            if i==len(word): 
                return root.word 
            if word[i]=='.': 
                for children in root.child.values(): 
                    if dfs(i+1,children): 
                        return True 
                return False 
            else: 
                if word[i] in root.child: 
                    return dfs(i+1,root.child[word[i]])
                else: 
                    return False 
        return dfs(0,self.root)            
        
