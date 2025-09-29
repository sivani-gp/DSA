class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftproduct = 1
        rightproduct = 1
        n = len(nums)
        ans = nums[0]
        for i in range(n):
            leftproduct = 1 if leftproduct==0 else leftproduct
            rightproduct = 1 if rightproduct==0 else rightproduct

            leftproduct *= nums[i]
            rightproduct *= nums[n-1-i]

            ans = max(ans,max(leftproduct,rightproduct))
        return ans