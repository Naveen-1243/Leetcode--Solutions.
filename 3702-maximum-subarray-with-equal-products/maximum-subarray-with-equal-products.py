import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res=0
        
        for i in range(len(nums)):
            x=[]
            for j in range(i,len(nums)):
                x.append(nums[j])
                prod=math.prod(x)
                y=math.gcd(*x)
                z=math.lcm(*x)
                if prod==y*z:
                    res=max(res, len(x))
        
        return res
            