class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        mini = min(need1, need2)

        return min(
            need1 * cost1 + need2 * cost2,

            mini * costBoth
            + (need1-mini) * cost1
            + (need2-mini) * cost2,

            max(need1, need2) * costBoth
        )