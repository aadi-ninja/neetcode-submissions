class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        # Phase 1: Find the intersection point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow