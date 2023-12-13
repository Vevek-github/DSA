from collections import deque


class Solution:
    def check(self, nums: List[int]) -> bool:
        a = deque()
        n = sorted(nums)
        
        for i in nums:
            a.append(i)
        
        for i in range(len(nums)):
            b = a.pop()
            a.appendleft(b)
            
            if list(a) == n:
                return True
        
        return False