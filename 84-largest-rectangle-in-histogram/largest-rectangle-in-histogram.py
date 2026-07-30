class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]
        for i,v in enumerate(heights):
            start=i
            while stack and v < stack[-1][1]:
                index, value = stack.pop()
                max_area=max(max_area, value * (i-index))
                start=index
            stack.append((start,v))
        
        for i,v in stack:
            max_area = max(max_area, v * (len(heights) - i))
        return max_area
        