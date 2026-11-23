class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        N=len(nums)
        left=-1
        res=0
        for right in range(N):
            if nums[right]>=minK and nums[right]<=maxK:
                res += right-left
            else:
                left=right
        return res