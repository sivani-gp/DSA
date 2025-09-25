class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        result = 0
        prefixSum = {0:1}
        for n in nums:
            currentSum+=n
            diff = currentSum - k
            result += prefixSum.get(diff,0)
            prefixSum[currentSum] = 1 + prefixSum.get(currentSum,0)
        return result

        


        