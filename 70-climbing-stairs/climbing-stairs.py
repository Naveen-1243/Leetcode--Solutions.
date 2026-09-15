class Solution:
    def climbStairs(self, n: int) -> int:
        
        s={}

        def dfs(n):
            if n<=1:
                return 1
            
            if n in s:
                return s[n]
            s[n]=dfs(n-1) + dfs(n-2)
            return s[n]
        
        return dfs(n)