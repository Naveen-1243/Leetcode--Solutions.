from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        x=list(map(str, nums))

        def compare(a, b):
            if a+b > b+a:
                return -1
            if b+a>a+b:
                return 1
            return 0
        
        x.sort(key=cmp_to_key(compare))
        res="".join(x)
        return "0" if res[0]==("0") else res