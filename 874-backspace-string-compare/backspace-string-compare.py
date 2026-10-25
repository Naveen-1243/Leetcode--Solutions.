class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]

        for i in s:
            if i.isalpha():
                s1.append(i)
            else:
                if s1:
                    s1.pop()
        
        for i in t:
            if i.isalpha():
                s2.append(i)
            else:
                if s2:
                    s2.pop()
        return s1==s2