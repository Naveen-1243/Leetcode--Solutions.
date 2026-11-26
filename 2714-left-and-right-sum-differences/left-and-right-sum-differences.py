class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        N=len(nums)
        prefix=[0] * (N+1)
        

        for i in range(len(nums)):
            prefix[i+1]=prefix[i]+nums[i]

        answer=[]
        for j in range(N):
            pre=prefix[j]

            suf=prefix[-1]-prefix[j+1]
            answer.append(abs(pre-suf))
        
        return answer