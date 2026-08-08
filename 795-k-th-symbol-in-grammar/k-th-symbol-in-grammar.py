class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        res=self.kthGrammar(n-1,(k+1)//2)
        if k%2==1:
            return res
        else:
            return 1-res