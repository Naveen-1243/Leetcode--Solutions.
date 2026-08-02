class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mini=nums[0]
        for i in nums[1:]:
            mini=min(abs(mini)-0, abs(i-0))
        
        for i in nums:
            if mini in nums:
                return mini
        return mini*(-1)