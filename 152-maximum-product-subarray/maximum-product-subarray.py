class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod=max(nums)
        cur_max=1
        cur_min=1

        for i in nums:
            if i==0:
                cur_max=1
                cur_min=1
                continue
            temp=cur_max*i
            cur_max=max(cur_max*i,cur_min*i,i)
            cur_min=min(temp,cur_min*i,i)
            max_prod=max(max_prod,cur_max)
        return max_prod