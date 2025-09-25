class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        current = 0
        for i in range(len(nums)):
            if current<0:
                current = 0
            current += nums[i]
            maxi=max(current,maxi)
        return maxi


        