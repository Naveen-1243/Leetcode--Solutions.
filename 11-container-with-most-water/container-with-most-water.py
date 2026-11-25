class Solution:
    def maxArea(self, height: list[int]) -> int:
        N=len(height)
        left=0
        right=N-1
        res=0
        while left < right:
            base=right-left
            h=min(height[left], height[right])
            total=base*h
            res=max(res, total)
            if height[left]<=height[right]:
                left += 1
            else:
                right -= 1
        return res