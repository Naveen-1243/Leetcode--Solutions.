class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel="aeiouAEIOU"
        count=0
        for i in s:
            if i in vowel:
                return True
        return False