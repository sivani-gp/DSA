class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        nums=str(num)
        max=0
        
        for i in nums:
            #for max
            if i!='9':
                max=i
                break
        max_num = nums.replace(max,'9') if max else nums
        min=nums[0]
        min_num= nums.replace(min,'0') if min else nums

        return int(max_num)-int(min_num)
        