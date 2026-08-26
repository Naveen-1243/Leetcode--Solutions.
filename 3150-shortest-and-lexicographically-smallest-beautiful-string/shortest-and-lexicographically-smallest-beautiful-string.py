class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        smallest_length=float('inf')
        smallest_s=""
        for i in range(len(s)):
            count_one=0
            for j in range(i, len(s)):
                if s[j] == "1":
                    count_one += 1
                
                if count_one > k:
                    break
                
                if count_one == k:
                    length = j - i + 1
                    if length < smallest_length:
                        smallest_length = length
                        smallest_s = s[i:j+1]
                    
                    if length == smallest_length and smallest_s > s[i:j+1]:
                        smallest_s = s[i:j+1]
        return smallest_s