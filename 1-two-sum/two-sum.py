class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        #two loops
        #sort two pointers 
        #dictionary
        N=len(nums)
        for i in range(N):
            for j in range(i+1, N):
                total = nums[i] + nums[j]

                if total == target:
                    return [i,j]
        