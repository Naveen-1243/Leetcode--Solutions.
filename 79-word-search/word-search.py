class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        w=len(word)

        def dfs(pos, index):
            i,j = pos
            if index == w:
                return True
            
            if i<0 or i>=m or j<0 or j >=n or board[i][j] != word[index]:
                return False
            temp=board[i][j]
            board[i][j]="#"
            found= (
                dfs((i+1,j),index+1) or
                dfs((i-1,j),index+1) or 
                dfs((i,j+1),index+1) or
                dfs((i,j-1),index+1)
            )
            board[i][j]=temp
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0]:
                    if dfs((r,c),0):
                        return True
        return False