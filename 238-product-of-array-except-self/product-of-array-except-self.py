class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        zero_count=0
        for x in nums:
            if x == 0:
                zero_count +=1 
            if zero_count>=2:
                return [0]*n
        product=1
        for i in nums:
            if i != 0:
                product *= i
        
        res=[]
        for i in nums:
            if zero_count==1:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
                
            else:
                res.append(product//i)
        
        return res