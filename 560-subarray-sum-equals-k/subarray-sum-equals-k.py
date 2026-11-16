class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d={0:1}
        count=0
        cur_sum=0

        for i in nums:
            cur_sum += i
            if cur_sum-k in d:
                count += d[cur_sum-k]
            d[cur_sum]=d.get(cur_sum, 0)+1
        
        return count