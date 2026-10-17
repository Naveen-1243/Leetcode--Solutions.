class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob1(a):
        
            if len(a)==1:
                return a[0]
            if len(a)==2:
                return max(a[0],a[1])

            arr=[a[0],max(a[0],a[1])]
            
            for i in range(2,len(a)):
                cur=max(a[i]+arr[i-2],arr[i-1])
                arr.append(cur)
            return arr[-1]

        x=len(nums)
        if x==1:
            return nums[0]
        res1=nums[:x-1]
        res2=nums[1::]
        return max(rob1(res1),rob1(res2))