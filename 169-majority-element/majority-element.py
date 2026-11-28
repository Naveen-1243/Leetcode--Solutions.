class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        d={}
        N=len(nums)
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i]=1
        
        
        for k,v in d.items():  # {3:2, 2:1} 
            if v>(N//2):
                return k