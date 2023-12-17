class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        set_= set()
        for i in nums:
            set_.add(i) 
        temp = [x for x in range(n+1)]
        for i in temp:
            if i not in set_:
                return i