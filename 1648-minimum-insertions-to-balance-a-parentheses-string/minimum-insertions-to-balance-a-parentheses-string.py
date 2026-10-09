class Solution:
    def minInsertions(self, s: str) -> int:
        count=0
        cur=0
        for i in s:
            if i == "(":
                if count % 2 == 1:
                    count -= 1
                    cur += 1
                count += 2
            else:
                count -= 1

                if count < 0:
                    cur += 1
                    count += 2
        return count + cur