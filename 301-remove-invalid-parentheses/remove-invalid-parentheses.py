class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        n=len(s)
        set1=set()
        max_length=0
        def backtrack(i,count,cur):
            nonlocal max_length
            if count<0:
                return

            if i == n:
                if count==0:
                    if len(cur) > max_length:
                        max_length=len(cur)
                        set1.clear()
                    
                    if len(cur) == max_length:
                        set1.add("".join(cur))
                return
            
            if s[i]!= "(" and s[i]!=")":
                cur.append(s[i])
                backtrack(i+1,count,cur)
                cur.pop()
                return
            
            cur.append(s[i])
            backtrack(i+1,count + (1 if s[i]=="(" else -1),cur)
            cur.pop()

            backtrack(i+1,count,cur)
    
        backtrack(0,0,[])
        return list(set1)