class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s)>k:
            arr=[]
            for i in range(len(s)):
                if i%k==0:
                    arr.append(0)
                arr[-1] += int(s[i])
            
            s="".join(str(x) for x in arr)
        
        return s