class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        given=[0]*(n+1)
        recieved=[0] * (n+1)

        for x,y in trust:
            given[x-1] -= 1
            recieved[y-1] += 1
        
        for i in range(n):
            if given[i] == 0 and recieved[i]==n-1:
                return i+1
        return -1