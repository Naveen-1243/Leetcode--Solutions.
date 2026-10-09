class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel={"a","e","i","o","u","A","E","I","O","U"}
        count=0
        max_count=0
        window=s[:k]
        for i in range(k):
            if s[i] in vowel:
                count+=1
                max_count=max(max_count,count)
        
        j=0
        for i in s[k:]:
            if s[j] in vowel:
                count-=1
                
            if i in vowel:
                count+=1
            max_count=max(count,max_count)
            j+=1
        return max_count