class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair=sorted(zip(position, speed))
        for p, s in pair[::-1]:
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)