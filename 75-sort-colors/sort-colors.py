class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        end = len(nums)-1
        mid = 0
        while mid<=end:
            if nums[mid]==0:
                nums[start],nums[mid] = nums[mid],nums[start]
                start+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[end] = nums[end],nums[mid]
                end-=1
        return nums