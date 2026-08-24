import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        j=0
        min_heap=[]
        for i in range(len(nums1)):
            heapq.heappush(min_heap, (nums1[i]+nums2[j], i, j))
        
        ans=[]
        for _ in range(k):
            total, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
        return ans