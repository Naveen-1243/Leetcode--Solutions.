class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        mod=10**9 + 7
        base=257
        def check(size):
            mp={}
            h=0
            power=pow(base, size-1, mod)
            for i in range(size):
                h=(h*base+nums[i])%mod
            mp[h]=1

            for i in range(size, N):
                h=(h - nums[i-size]*power)%mod
                h=(h*base+nums[i])%mod

                mp[h]=mp.get(h,0)+1
            return any(count==1 for count in mp.values())

        l,r=1,N
        res=N
        while l<=r:
            mid=(l+r)//2

            if check(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        
        return res