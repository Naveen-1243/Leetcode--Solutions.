class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n==1:
            return "0"
        middle=2**(n-1)

        if k==middle:
            return "1"
        if k<middle:
            return self.findKthBit(n-1,k)
        if k>middle:
            new_k=k-middle
            left=middle-new_k
            result=self.findKthBit(n-1,left)
            if result=="0":
                return "1"
            else:
                return "0"