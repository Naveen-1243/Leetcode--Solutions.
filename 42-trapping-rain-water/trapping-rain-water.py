class Solution:
    def trap(self, height: List[int]) -> int:
        
        l=0
        r=len(height)-1
        lmax=0
        rmax=0
        left=[]
        for i in height:
            lmax=max(lmax,i)
            left.append(lmax)
        
        right=[]
        for j in range(len(height)-1,-1,-1):
            rmax=max(rmax,height[j])
            right.append(rmax)
        
        right.reverse()
        res=0
        z=0
        while z<=r:
            res+=min(left[z],right[z]) - height[z]
            z+=1
        return res