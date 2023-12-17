class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s2 = 0
        for i in nums:
            s2 +=i
        return ((n*(n+1)//2)-s2)
        
            