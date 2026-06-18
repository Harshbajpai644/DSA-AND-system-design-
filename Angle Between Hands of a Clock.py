class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        diff = abs(hour_angle - min_angle)
        
        return min(diff, 360 - diff)
