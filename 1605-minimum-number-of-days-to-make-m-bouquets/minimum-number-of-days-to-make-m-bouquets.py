class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 1 , max(bloomDay)
        n = m * k
        if n > len(bloomDay):
            return -1
        def make_bouquets(bloomDay, m, k, day):
            total = 0
            flowers = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                        total += 1
                        flowers = 0
                else:
                    flowers = 0
                
                if total >= m:
                    return True
            return False

        while l <= r:
            mid = (l + r) // 2
            if make_bouquets(bloomDay, m ,k, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

            
            
            
            

        