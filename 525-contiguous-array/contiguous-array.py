class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=0
        max_count=0
        res=0
        first_seen={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            else:
                count+=1

            if count in first_seen:
                res=i-first_seen[count]
                max_count=max(max_count,res)
            else:
                first_seen[count]=i

        return max_count