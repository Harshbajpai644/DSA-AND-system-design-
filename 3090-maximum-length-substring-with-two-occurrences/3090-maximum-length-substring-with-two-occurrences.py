class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        count = {}
        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans