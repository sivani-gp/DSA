class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        count=0
        for i in nums:
            if i!=0:
                i,nums[count] = nums[count],i
                count+=1
        while count<n:
            nums[count]=0
            count+=1



        