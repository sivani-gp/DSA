class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return nums
        k %= n
        if k == 0:
            return nums

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse(0, n-1)    # reverse whole -> B + A
        reverse(0, k-1)    # reverse A
        reverse(k, n-1)    # reverse B
        
        return nums