class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars)==0:
            return 0
        res=[chars[0]]
        count=1
        for i in chars[1:]:
            if i == res[-1]:
                count+=1
            
            else:
                if count >1:
                    res.extend(str(count))
                count=1
                res.append(i)

        if count>1:
            res.extend(str(count))
        
        chars[:]=res
        return len(chars)