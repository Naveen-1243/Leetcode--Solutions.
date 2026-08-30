class Solution:
    def myAtoi(self, s: str) -> int:
        a=""
        start=0
        while start < len(s) and s[start] == " ":
            start += 1
        a=s[start:]
        if a == "":
            return 0
        
        res=0
        number={'1','2','3','4','5','6','7','8','9','0'}
        negative=False
        if a[0] == "-":
            negative=True
            a=a[1:]
        elif a[0] == "+":
            a=a[1:]
        for i in a:
        
            if i in number:
                res =res*10 + int(i)
            else:
                break
        
        
        if res == 0:
            return 0
        if negative and res > 2**31:
            return -2**31
        
        if not negative and res > 2**31 - 1:
            return 2**31 - 1
        
        if negative:
            return -res
        return res


