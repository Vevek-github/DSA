class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n =len(nums)
        flag = 0
        sol =0
        for i in range(len(nums)):
            if nums[i]==1:
                flag+=1
            else :
                flag =0
            sol = max(flag, sol)
        
        return sol
                
            
                
            