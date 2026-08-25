class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set=set(nums)
        for i in range(1,101):
            product=k*i
            if product not in nums_set:
                return product
        return k*101