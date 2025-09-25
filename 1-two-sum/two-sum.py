class Solution:
    def twoSum(self,nums: List[int],target: int):
        dict1={}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in dict1:
                return [dict1[diff],index]
            dict1[value] = index       
    
