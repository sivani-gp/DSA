class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1,len(nums)+1):
            ans^=i
        for i in nums:
            ans^=i
        return ans
        