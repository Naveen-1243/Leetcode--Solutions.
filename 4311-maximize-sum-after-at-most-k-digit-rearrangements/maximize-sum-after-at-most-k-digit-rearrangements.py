class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        
        def rev(x):
            y=str(x)
            return int(''.join(sorted(y, reverse=True)))
        
        gain=[]
        for i in nums:
            res=rev(i)-i
            gain.append(res)
            
        gain.sort(reverse=True)
        return sum(nums) + sum(gain[:k])