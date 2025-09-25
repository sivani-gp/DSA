class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        i,j = 0,1
        k=0
        for k in range(len(nums)):
            if nums[k]>0:
                result[i]=nums[k]
                i+=2
            else:
                result[j]=nums[k]
                j+=2
        return result
            

        




        