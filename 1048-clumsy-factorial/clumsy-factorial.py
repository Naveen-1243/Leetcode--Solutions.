class Solution:
    def clumsy(self, n: int) -> int:
        
        count=0
        s=[n]

        for i in range(n-1,0,-1):
            if count==0:
                s[-1]=s[-1]*i
            elif count==1:
                s[-1]=int(s[-1]/i)
            elif count==2:
                s.append(i)
            else:
                s.append(-i)
            count+=1
            if count==4:
                count=0
        return sum(s)