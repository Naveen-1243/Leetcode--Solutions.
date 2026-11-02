class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        mid = n//2
        res=0
        for i in nums:
            res += abs(nums[mid]-i)
        
        return res