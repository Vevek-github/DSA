class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums.sort()
        n = len(nums)
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                mini = i
                if nums[mini] < nums[j]:
                    mini = j
                nums[mini],nums[j]= nums[j],nums[mini]
                j+=1