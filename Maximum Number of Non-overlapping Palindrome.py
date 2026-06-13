class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        start_idx = 0
        
        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)
            
            while left >= start_idx and right < n and s[left] == s[right]:
                current_length = right - left + 1
                
                if current_length >= k:
                    count += 1
                    start_idx = right + 1
                    break
                    
                left -= 1
                right += 1
                
        return count
