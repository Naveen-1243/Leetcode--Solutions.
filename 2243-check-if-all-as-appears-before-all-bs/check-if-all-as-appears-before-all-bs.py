class Solution:
    def checkString(self, s: str) -> bool:
        count_b=0
        for i in s:
            if i =="b":
                count_b+=1
            else:
                if count_b>0:
                    return False
        return True
