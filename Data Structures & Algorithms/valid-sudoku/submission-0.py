class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rhash=defaultdict(list)
        chash=defaultdict(list)
        shash=defaultdict(list)
        for r in range(9): 
            for c in range(9): 
                no=board[r][c]
                if no=='.': 
                    continue 
                sq=(r//3)*3 + (c//3)
                if no in rhash[r] or no in chash[c] or no in shash[sq]: 
                    return False 
                rhash[r].append(no)
                chash[c].append(no)
                shash[sq].append(no)
        return True
