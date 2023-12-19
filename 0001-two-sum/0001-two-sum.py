class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        presum = {}
        for i in range(n):
            temp=nums[i]
            presum[temp]= i
        j = 0
        while j < n :
            if (target-nums[j]) in presum:
                if presum[target-nums[j]] != j:
                    return presum[target-nums[j]] , j
            j+=1    
        return -1     
            