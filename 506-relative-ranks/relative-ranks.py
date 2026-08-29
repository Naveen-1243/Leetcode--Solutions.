class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        max_heap=[(-score[i], i) for i in range(len(score))]
        heapq.heapify(max_heap)
        
        res=[""] * len(score)
        
        
        count=1
        while max_heap:
            neg_score, index = heapq.heappop(max_heap)
            if count == 1:
                res[index] = "Gold Medal"
            elif count == 2:
                res[index] = "Silver Medal"
            elif count == 3:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(count)
            count+=1
        
        return res