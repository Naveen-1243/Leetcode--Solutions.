class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump=0
        for index, value in enumerate(nums):
            if index > max_jump:
                return False
            max_jump = max(max_jump, index+value)

            if max_jump >= len(nums):
                return True
        
        return True