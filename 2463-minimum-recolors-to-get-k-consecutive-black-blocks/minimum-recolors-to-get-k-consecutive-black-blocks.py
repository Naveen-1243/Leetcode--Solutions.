class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        for i in blocks[:k]:
            if i == "W":
                count+=1
        minimum=count
        for i in range(k,len(blocks)):
            if blocks[i] == "W":
                count+=1
            if blocks[i-k] == "W":
                count-=1
            minimum=min(minimum,count)
        return minimum