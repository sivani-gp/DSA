class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 1 , max(bloomDay)
        n = m * k
        if n > len(bloomDay):
            return -1
        flowers, bouquets = 0, 0
        while l <= r:
            mid = (l + r) // 2
            flowers, bouquets = 0, 0
            for day in bloomDay:
                if mid >= day:
                    flowers += 1
                else:
                    flowers = 0

                if flowers >= k:
                    bouquets += 1
                    flowers = 0
                    if bouquets == m:
                        break
            
            if bouquets == m:
                r = mid - 1
            else:
                l = mid + 1
        return l

            
            
            
            

        