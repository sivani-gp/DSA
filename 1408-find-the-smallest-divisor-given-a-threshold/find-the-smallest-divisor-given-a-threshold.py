class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def helper(divisor):
            ans = 0
            for i in nums:
                ans += math.ceil(i / divisor)
            return ans <= threshold

        l, r = 1, max(nums)
        while l <= r:
            mid = l + ((r - l) // 2)
            if helper(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        