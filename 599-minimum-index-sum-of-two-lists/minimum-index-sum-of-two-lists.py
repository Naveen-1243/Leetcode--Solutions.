class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        
        s1=set(list1)
        s2=set(list2)
        
        d={}
        for i,v in enumerate(list1):
            if v in s2:
                d[v]=i
        
        for i,v in enumerate(list2):
            if v in s1:
                d[v] += i

        mini=min(d.values())
        output=[]
        for k,v in d.items():
            if v==mini:
                output.append(k)
        return output