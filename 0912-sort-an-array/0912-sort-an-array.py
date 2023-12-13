class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        return nums
    
    # time complexity O(n2)
    
    # Insertion Sort
    
    def sortInsertionArray(self, nums: List[int]) -> List[int]:
        length =len(nums)
        for i in range(length):
            j = i
            while j < length:
                if nums[i] > nums[j]:
                    nums[i],nums[j]= nums[j],nums[i]
                j+=1
            
            
        return nums
    
    # Bubble Sort
    
    def sortBubbleArray(slef,nums: List[int])-> List[int]:
        length = len(nums)
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]> nums[j+1]:
                    nums[j+1],nums[j]= nums[j],nums[j+1]
        return nums
    
    # selection Sort 
    
    def sortselectionsortArray(self, nums: List[int]) -> List[int]:
        length =len(nums)
        for i in range(length):
            j = i+1
            min = i
            while j < length:
                if nums[j] < nums[min]:
                    min = j
                j+=1
            nums[i],nums[min]= nums[min],nums[i]
            
        return nums