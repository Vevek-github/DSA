class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n =len(nums)
        sol =0
        if n<=2:
            for i in nums:
                if i ==1:
                    sol+=1
            return sol
        maxi=0
        i=1
        if nums[0]==1:
            maxi=1
        while i < n:
            if nums[i]==nums[i-1] and nums[i]==1:
                maxi = maxi+1
                sol= max(maxi ,sol)
                i+=1
            elif nums[i]!=nums[i-1] and nums[i]==1:
                maxi = 1
                sol= max(maxi ,sol)
                i+=1
            
            elif nums[i]==0 :
                maxi=0
                i+=1
        sol= max(maxi,sol)
        return sol
                
            
                
            