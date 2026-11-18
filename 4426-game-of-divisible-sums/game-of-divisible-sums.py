from functools import cache
class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        N=len(nums)
        @cache
        def dp(i):
            if i >=N:
                return 0
            
            first=nums[i] - dp(i+1) if nums[i]%3==0 else nums[i]+dp(i+1)
            
            second=float('-inf')
            if i+1<N:
                total=nums[i]+nums[i+1]
                second=total -dp(i+2) if total%3==0 else total + dp(i+2)

            return max(first,second)
        
        return dp(0)
    