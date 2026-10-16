class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini=arrays[0][0]
        maxi=arrays[0][-1]
        res=0
        for i in range(1,len(arrays)):
            res = max(res, maxi - arrays[i][0])
            res = max(res, arrays[i][-1] - mini)

            maxi = max(maxi, arrays[i][-1])
            mini = min(mini, arrays[i][0])
        
        return res