class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=[x for x in s]
        i=0
        j=len(s)-1
        vowel={'a','e','i','o','u','A','E','I','O','U'}
        while i < j:
            if arr[i] not in vowel:
                i+=1
            elif arr[j] not in vowel:
                j-=1
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        return "".join(arr)