class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window=sum(nums[:k])
        m_avg= window / k
        s=0
        for i in range(k,len(nums)):
            window += nums[i] - nums[i-k]
            avg = window / k
            m_avg=max(avg,m_avg)
        return m_avg