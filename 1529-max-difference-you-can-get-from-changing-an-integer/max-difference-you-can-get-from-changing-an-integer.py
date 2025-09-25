class Solution:
    def maxDiff(self, num: int) -> int:
        nums=str(num)
        num=str(num)
        for i in nums:
            if i!='9':
                max=nums.replace(i,'9')
                break
            else:
                max=nums
        
        if num[0]!='1':
            min=num.replace(num[0],'1')
        else:
            for j in num[1::]:
                if j!='1' and j!='0':
                    min=num.replace(j,'0')
                    break
                else:
                    min=num
        return int(max)-int(min)