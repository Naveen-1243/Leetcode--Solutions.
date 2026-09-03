class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        first=nums[-1] * nums[-2]
        second=nums[0] * nums[1]
        return first - second