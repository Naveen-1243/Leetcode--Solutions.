class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res=[[0]*n for _ in range(n)]
        left=0
        right=n-1
        top=0
        bottom=n-1
        num=1
        
        while top <= bottom and left <= right:

            for j in range(left,right+1):
                res[top][j]=num
                num+=1
            top+=1

            for i in range(top,bottom+1):
                res[i][right]=num
                num+=1
            right-=1

            if top<=bottom:
                for j in range(right,left-1,-1):
                    res[bottom][j]=num
                    num+=1
                bottom-=1
            
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res[i][left]=num
                    num+=1
                left+=1
        return res

    