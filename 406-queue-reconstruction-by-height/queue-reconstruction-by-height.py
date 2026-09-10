from collections import deque
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        sorted_q=sorted(people, key=lambda x:(-x[0],x[1]))
        
        q=deque([sorted_q[0]])
        for i in range(1,len(sorted_q)):
            h,k = sorted_q[i]
            q.insert(k, [h,k])
        return list(q)