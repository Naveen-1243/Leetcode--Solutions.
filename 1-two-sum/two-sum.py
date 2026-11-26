class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        
        # 3,10,5,20   t=15  3 5 10 20   
        #dictionary   d=3-0 5-1 
        
        d={}

        for i,val in enumerate(nums):
            diff=target-val

            if diff in d:
                return [d[diff],i]
            else:
                d[val]=i  