class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered=set()
        for s,e in ranges:
            for num in range(s,e+1):
                covered.add(num)
        
        for x in range(left,right+1):
            if x not in covered:
                return False
        return True