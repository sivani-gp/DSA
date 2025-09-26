class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        n = len(arr) - 1
        for i in range(n,-1,-1):
            arr[i],maxi = maxi,max(maxi,arr[i])
        return arr

        