class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n =len(nums)
        #hash ={}
        #for i in nums:
         #   hash[i]=hash.get(i,0)+1
        #for i in hash:
        #    if hash[i]>n//2:
         #      return i
        count = 0                      #moore voting algorithim
        candidate = 0
        j = 0
        while j < n:
            if count == 0:
                nums[candidate]=nums[j]
                count=1
            elif nums[j]==nums[candidate]:
                count+=1
            else :
                count-=1
            j+=1
        return nums[candidate]