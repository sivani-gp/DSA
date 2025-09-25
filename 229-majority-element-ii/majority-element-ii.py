class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        n=len(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        for j in d.keys():
            if d[j]>(n//3):
                l.append(j)
        return l

        