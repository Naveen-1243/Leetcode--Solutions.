class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=set(nums)
        max_pos=1
        for i in range(len(nums)):
            if nums[i]>0:
                max_pos = max(max_pos, nums[i])
        for i in range(1, max_pos+1):
            if i not in x:
                return i
        return max_pos+1