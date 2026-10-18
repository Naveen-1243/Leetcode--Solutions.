class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n==1:
            return False
        n1=0
        n2=0
        n3=1
        res=[0,0,1]
        total=1
        while total <= n:
            temp=n3+n2
            total=temp
            res.append(temp)
            n2,n3=n3,temp
            
        

        for i in range(1,len(res)-1):
            if res[i]+res[i-1]+res[i+1] == n:
                return True
        
        return False