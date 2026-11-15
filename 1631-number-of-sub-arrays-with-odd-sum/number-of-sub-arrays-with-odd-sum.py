class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9 +7
        n=len(arr)

        even=1
        odd=0
        res=0

        prefix=[0]
        for i in arr:
            prefix.append(i+prefix[-1])
        
        for i in prefix[1:]:
            if i%2!=0:
                res += even
                odd+=1
            else:
                res+=odd
                even+=1
    
        return res % mod