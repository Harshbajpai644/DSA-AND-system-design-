class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        for char in n:
            digit = int(char)
            if digit > max_digit:
                max_digit = digit
            if max_digit == 9:
                break
        return max_digit