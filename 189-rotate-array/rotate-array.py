class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N=len(nums)

        if k>N:
            k=k%N
        
        
        x=nums[N-k:] + nums[:N-k]
        nums[:]=x