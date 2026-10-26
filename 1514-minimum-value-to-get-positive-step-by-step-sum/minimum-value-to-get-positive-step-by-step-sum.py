class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        
        total=0
        mini=0

        for i in nums:
            total+=i
            mini=min(mini,total)
        return 1-mini