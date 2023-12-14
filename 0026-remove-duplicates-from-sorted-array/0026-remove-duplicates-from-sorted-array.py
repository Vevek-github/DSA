class Solution:
    def removeDuplicates(self, nums: List[int]) -> Tuple[int, List[int]]:
        pivot = 1
        right = 1
        length = len(nums)
        
        while right < length:
            
            if nums[right] != nums[right-1]:
                nums[pivot]=nums[right]
                pivot+=1
                
            right+=1
        return pivot
        
        
        
