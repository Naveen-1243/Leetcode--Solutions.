class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        d={}
        for i, val in enumerate(nums):
            diff = target-val

            if diff in d:
                return [d[diff], i]
            else:
                d[val]=i
        