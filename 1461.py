class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed_count = 1 << k
        seen = set()
        
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            if substring not in seen:
                seen.add(substring)
                if len(seen) == needed_count:
                    return True
        
        return False