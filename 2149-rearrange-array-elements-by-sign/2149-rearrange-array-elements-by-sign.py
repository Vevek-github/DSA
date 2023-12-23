class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        flag =[]
        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        for i in range(len(positives)):
                   flag.append(positives[i])
                   flag.append(negatives[i])
                       
            
                    
        return flag
                    