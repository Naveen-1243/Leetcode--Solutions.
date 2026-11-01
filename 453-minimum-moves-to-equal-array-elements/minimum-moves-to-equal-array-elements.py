class Solution:
    def minMoves(self, nums: list[int]) -> int:
        
        res=0
        mini=min(nums)

        for i in nums:
            res += i-mini
        
        return res