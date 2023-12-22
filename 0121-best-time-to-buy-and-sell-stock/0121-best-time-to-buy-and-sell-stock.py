class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = len(prices)
        if x == 1:
            return 0
        left = 0 
        right = 1
        maximum = 0 
        while right < x:
            diff =prices[right] - prices[left]
            if diff > 0:
                right +=1
                
            if diff<= 0:
                left=right
                right+=1
            maximum = max(maximum ,diff )
        return maximum
        