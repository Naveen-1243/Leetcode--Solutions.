class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isprefix(x,y):
            if len(x)>len(y):
                return False
            for i in range(len(x)):
                if x[i] != y[i]:
                    return False
            return True
        
        def issufix(x,y):
            for i in range(len(x)):
                if x[i]!=y[len(y)-len(x)+i]:
                    return False
            return True
        

        count=0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isprefix(words[i],words[j]) and issufix(words[i],words[j]):
                    count+=1
        
        return count