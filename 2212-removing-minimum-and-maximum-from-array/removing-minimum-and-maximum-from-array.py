class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=max(nums)
        mini=min(nums)

        max_index=nums.index(maxi)
        min_index=nums.index(mini)

        left=min(max_index, min_index)
        right=max(max_index, min_index)

        return min(right+1, n-left, (left+1)+(n-right) )
        