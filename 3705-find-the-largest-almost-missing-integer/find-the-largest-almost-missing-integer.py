class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        """
        k=1 --> largest in overall nums  (count=1)
        k=n --> largest in nums
        1 k n   if [0] and [n-1] same --> -1   else max
        """

        n= len(nums)
        if k==n:
            return max(nums)
        
        maxi=[]
        for i in nums:
            if nums.count(i) == 1:
                maxi.append(i)
        
        if k == 1:
            if maxi:
                return max(maxi)
            else:
                return -1
        
        if 1 < k < n:
            if nums.count(nums[0]) == 1 and nums.count(nums[n-1])==1:
                return max(nums[0], nums[n-1])
            elif nums.count(nums[0]) == 1 and nums.count(nums[n-1]) != 1:
                return nums[0]
            elif nums.count(nums[0]) !=1 and nums.count(nums[n-1])==1:
                return nums[n-1]
            elif nums.count(nums[0]) > 1 and nums.count(nums[n-1]) > 1:
                return -1