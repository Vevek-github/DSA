class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_increase = 0
        flag = True
        neg_all = float(-inf)
        for n in nums :
            if n > 0:
                flag = False
                break
            if n > neg_all:
                neg_all = n
        if flag == True:
            return neg_all 
        
        min_elevation = 0
        cur_elevation = 0
        for n in nums:
            cur_elevation += n 
            if cur_elevation < min_elevation:
                min_elevation = cur_elevation
            if largest_increase < cur_elevation -min_elevation:
                largest_increase = cur_elevation -min_elevation
        return largest_increase