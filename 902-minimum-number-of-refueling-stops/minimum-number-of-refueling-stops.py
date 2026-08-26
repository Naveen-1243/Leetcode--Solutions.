import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if not stations:
            if startFuel >= target:
                return 0
            return -1

        if startFuel < stations[0][0]:
            return -1
        heap=[]
        stops=0
        startFuel -= stations[0][0]
        heapq.heappush(heap, -stations[0][1])
        for i in range(len(stations)):
            if i+1 < len(stations):
                distance = stations[i+1][0] - stations[i][0]

                while startFuel < distance:
                    if not heap:
                        return -1
                    startFuel += -heapq.heappop(heap)
                    stops += 1

                if startFuel >= distance:
                    startFuel -= distance
                    heapq.heappush(heap, -stations[i+1][1])
        
        distance = target - stations[-1][0]
        while startFuel < distance:
            if not heap:
                return -1
            startFuel += -heapq.heappop(heap)
            stops += 1
        
        return stops
