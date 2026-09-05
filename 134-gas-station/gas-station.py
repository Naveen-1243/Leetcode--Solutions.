class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total=0
        diff=0
        start=0
        for i in range(n):
            total += gas[i] - cost[i]
            diff += gas[i]-cost[i]
        
            if diff<0:
                diff=0
                start = i+1
        
        return start if total>=0 else -1