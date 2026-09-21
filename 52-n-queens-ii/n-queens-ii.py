class Solution:
    def totalNQueens(self, n: int) -> int:
        
        count=0
        col=set()
        posd=set()
        negd=set()
        path=[["."]*n for _ in range(n)]
        def backtrack(r):
            nonlocal count
            if r==n:
                count+=1
            for c in range(n):
                if c in col or (r+c) in posd or (r-c) in negd:
                    continue
                col.add(c)
                posd.add(r+c)
                negd.add(r-c)
                path[r][c]="Q"

                backtrack(r+1)

                path[r][c]="."
                col.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
        backtrack(0)
        return count