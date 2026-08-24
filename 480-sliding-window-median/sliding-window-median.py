import heapq
from collections import defaultdict
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap=[]
        min_heap=[]
        deleted=defaultdict(int)
        max_size=0
        min_size=0
        result=[]

        def add(num):
            nonlocal max_size, min_size
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
                max_size += 1
            else:
                heapq.heappush(min_heap, num)
                min_size += 1
        
        def remove(num):
            nonlocal max_size, min_size
            deleted[num] += 1
            if num <= -max_heap[0]:
                max_size -= 1
            else:
                min_size -= 1

        def clean():
            while max_heap and deleted[-max_heap[0]] > 0:
                num = -heapq.heappop(max_heap)
                deleted[num] -= 1
            
            while min_heap and deleted[min_heap[0]] > 0:
                num = heapq.heappop(min_heap)
                deleted[num] -=1
        
        def balance():
            nonlocal max_size, min_size
            while max_size > min_size+1:
                popped=heapq.heappop(max_heap)
                heapq.heappush(min_heap, -popped)
                max_size -= 1
                min_size += 1
            while min_size > max_size:
                popped=heapq.heappop(min_heap)
                heapq.heappush(max_heap, -popped)
                min_size -=1
                max_size += 1
            clean()
        
        def median():
            if max_size != min_size:
                return float(-max_heap[0])
            else:
                return (-max_heap[0] + min_heap[0])/2

        for i in range(k):
            add(nums[i])
        balance()
        result.append(median())
        
        for num in range(k,len(nums)):
            remove(nums[num - k])
            add(nums[num])
            balance()
            result.append(median())
        
        return result