class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_count = 0
        curr_count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_count += 1
            else:
                ans += min(prev_count, curr_count)
                prev_count = curr_count
                curr_count = 1
        
        ans += min(prev_count, curr_count)
        
        return ans