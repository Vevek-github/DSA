class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i]= hashmap.get(i ,0)+1
        for i in hashmap:
            if hashmap[i]==1:
                return i
        return -1