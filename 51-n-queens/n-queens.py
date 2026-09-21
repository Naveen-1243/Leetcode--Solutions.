class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        col=set()
        posd=set()
        negd=set()
        res=[]
        board=[["."] * n for _ in range(n)]
        def backtrack(r):
                if r == n:
                    res.append(["".join(row) for row in board])
                    return
                for c in range(n):
                    if c in col or (r+c) in posd or (r-c) in negd:
                        continue
                    col.add(c)
                    posd.add(r+c)
                    negd.add(r-c)
                    board[r][c]="Q"

                    backtrack(r+1)

                    board[r][c]="."
                    col.remove(c)
                    posd.remove(r+c)
                    negd.remove(r-c)
        backtrack(0)
        return res