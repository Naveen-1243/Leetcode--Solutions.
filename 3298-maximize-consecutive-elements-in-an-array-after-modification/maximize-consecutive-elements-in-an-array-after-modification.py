class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp={}
        res=0

        for i in nums:
            dp[i+1]=max(dp.get(i+1,0),dp.get(i,0)+1)
            dp[i]=max(dp.get(i,0), dp.get(i-1,0)+1)

            res=max(res,dp[i+1],dp[i])
        
        return res
