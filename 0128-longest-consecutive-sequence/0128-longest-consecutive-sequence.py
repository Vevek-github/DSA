class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        count = 1
        if n == 0:
            return 0
        elif n==1:
            return 1
        nums = list(set(nums)) 
        nums.sort()
        n = len(nums)
        maxtill = 0
        counter = 0
        n = len(nums)
        while i <n-count and counter < n:
            if nums[i]+count== nums[i+count]:
                count+=1
                maxtill = max(maxtill,count)
                
            else :
                i += count
                count=1
            counter+=1 
        maxtill = max(maxtill,count)    
        return maxtill