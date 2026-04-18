class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        reversed_s = s[::-1]
        reversed_n = int(reversed_s)
        
        return abs(n - reversed_n)
