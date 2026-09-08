class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        
        heap=[-i for i in nums]
        heapq.heapify(heap)

        for i in range(1,len(nums),2):
            top=-heapq.heappop(heap)
            nums[i]=top
        
        for i in range(0,len(nums),2):
            top=-heapq.heappop(heap)
            nums[i]=top
        