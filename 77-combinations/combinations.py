class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        res=[]
        path=[]

        def dfs(i):
            if len(path)== k:
                res.append(path.copy())
                return
            elif i>n:
                return
            else:
                path.append(i)
                dfs(i+1)
                
                path.pop()
                dfs(i+1)
        dfs(1)
        return res