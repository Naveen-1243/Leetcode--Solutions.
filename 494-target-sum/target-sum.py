class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo={}
        def backtrack(i,total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            
            if (i,total) in memo:
                return memo[(i,total)]
            
            plus=backtrack(i+1,total+nums[i])
            
            minus=backtrack(i+1,total-nums[i])

            memo[(i,total)]=plus + minus
            return memo[(i,total)]

        return backtrack(0,0)