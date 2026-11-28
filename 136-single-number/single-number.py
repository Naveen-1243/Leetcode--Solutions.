class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        d={}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i]=1
        
        for k,val in d.items():
            if val == 1:
                return k