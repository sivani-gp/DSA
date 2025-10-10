class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights) , sum(weights)

        while l <= r:
            mid = l + ((r - l) // 2)

            day = 1
            weightSum = 0
            for weight in weights:
                if (weightSum + weight) > mid:
                    day += 1
                    weightSum = 0
                weightSum += weight
            
            if day > days:
                #if more days r reqd, increase capacity
                l = mid + 1
            else:
                r = mid - 1
        return l


