class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        
        def rev(x):
            y=str(x)
            z=int("".join(sorted(y, reverse=True)))
            return z

        res=[]
        for i in nums:
            z=abs(i-rev(i))
            res.append(z)
        
        res.sort(reverse=True)
        return sum(nums) + sum(res[:k])