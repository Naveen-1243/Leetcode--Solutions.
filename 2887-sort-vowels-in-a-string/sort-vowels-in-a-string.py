class Solution:
    def sortVowels(self, s: str) -> str:
        
        n=""
        vowel="aeiouAEIOU"

        for i in s:
            if i in vowel:
                n+=i
        
        n=sorted(n)
        s=list(s)
        v_index=0
        for i in range(len(s)):
            if s[i] in vowel:
                s[i]=n[v_index]
                v_index+=1
        return "".join(s)