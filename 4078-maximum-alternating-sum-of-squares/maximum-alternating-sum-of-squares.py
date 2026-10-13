class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        q=collections.deque(sorted(x**2 for x in nums))
        res=0
        while len(q)>=2:
            res -= q.popleft()
            res += q.pop()
        
        while len(q)>0:
            ans = q.pop()
            res += ans
        return res