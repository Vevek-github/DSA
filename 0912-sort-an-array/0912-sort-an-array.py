class Solution:
    # mergeSOrt DIVIDE AND CONQUER
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # time complexity O(nlog(n))
        
        def merge(nums , L, M , R):
            left_arr =nums[L:M+1]
            right_arr =nums[M+1:R+1]
            i , j ,k = L , 0 ,0
            while j < len(left_arr) and k < len(right_arr):
                if left_arr[j]<=right_arr[k]:
                    nums[i]=left_arr[j]
                    j+=1
                else :
                    nums[i]=right_arr[k]
                    k+=1
                i+=1
            while j< len(left_arr):
                nums[i]=left_arr[j]
                j+=1
                i+=1
                
            while k< len(right_arr):
                nums[i]=right_arr[k]
                k+=1
                i+=1
            return nums
        
        
        def merge_divide(nums, left , right):
            if left == right :
                return nums
            mid = (left + right)//2
            merge_divide(nums,left, mid)
            merge_divide(nums , mid+1,right)
            merge(nums , left , mid , right)
            return nums
        
        return merge_divide(nums, 0, len(nums)-1)
    
    
    
    
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