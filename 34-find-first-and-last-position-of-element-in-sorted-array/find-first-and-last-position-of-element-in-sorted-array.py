class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to perform modified binary search
        def binary_search(nums, target, search_left):
            start = 0
            end = len(nums) - 1
            result = -1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    result = mid
                    if search_left:
                        end = mid - 1  # Keep looking to the left
                    else:
                        start = mid + 1  # Keep looking to the right

            return result

        # Find the first and last occurrences of the target
        left_index = binary_search(nums, target, True)
        right_index = binary_search(nums, target, False)

        return [left_index, right_index]
    
    
        