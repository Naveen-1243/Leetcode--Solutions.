class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        start=pairs[0][0]
        end=pairs[0][1]
        new=[]
        for i in range(1,len(pairs)):
            first,second=pairs[i]

            if end>=first:
                end=min(end,second)
            
            else:
                new.append([start,end])
                start=first
                end=second
        new.append([start,end])
        return len(new)