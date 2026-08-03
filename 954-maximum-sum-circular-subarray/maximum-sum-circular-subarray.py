class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        cur_max=0
        max_sum=nums[0]
        cur_min=0
        min_sum=nums[0]

        for i in nums:
            total += i
            cur_max = max(i,cur_max+i)
            max_sum=max(max_sum,cur_max)
            cur_min=min(i,cur_min+i)
            min_sum=min(min_sum,cur_min)
        
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)