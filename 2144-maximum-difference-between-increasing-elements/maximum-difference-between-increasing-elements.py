class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini=nums[0]
        max_diff=-1
        for i in range(1,len(nums)):
            if nums[i]>mini:
                max_diff=max(max_diff,nums[i]-mini)
            else:
                mini=nums[i]
        return max_diff
        