class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        water=0
        max_water=0
        i=0
        j=len(height)-1

        while i<j:
            base=j-i
            hei=min(height[i],height[j])

            water=base * hei
            max_water=max(max_water,water)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        
        return max_water