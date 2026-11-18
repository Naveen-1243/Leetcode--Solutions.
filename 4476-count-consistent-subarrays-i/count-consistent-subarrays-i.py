class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        N=len(nums)
        count=0
    
        for i in range(N):
            mini=nums[i]
            and_val=nums[i]

            for j in range(i,N):
                mini=min(mini,nums[j])
                and_val &= nums[j]

                if mini==and_val:
                    count += 1
        
        return count