import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_reduce(max_time):
            total_reduction = 0
            for w in workerTimes:
                x = int((-1 + math.isqrt(1 + 8 * max_time // w)) // 2)
                total_reduction += x
                if total_reduction >= mountainHeight:
                    return True
            return total_reduction >= mountainHeight

        low = 1
        
        high = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans