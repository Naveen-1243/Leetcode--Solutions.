class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        stack=[nums[0]]
        count=0
        for i in nums[1:]:
            if i^stack[-1]==0:
                count+=1
            else:
                stack.append(i)
        return count
        