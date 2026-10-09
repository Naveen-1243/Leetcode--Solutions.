class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        s=[0]+flowerbed+[0]
        for i in range(1,len(s)-1):
            if s[i] == 0 and s[i-1] ==0 and s[i+1] ==0:
                n-=1
                s[i]=1
                if n<=0:
                    return True
        return n<=0