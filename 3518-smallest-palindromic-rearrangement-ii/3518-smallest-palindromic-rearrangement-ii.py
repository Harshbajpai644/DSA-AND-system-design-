import collections

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        
        half_count = [0] * 26
        mid_letter = ""
        
        for c, freq in count.items():
            half_count[ord(c) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid_letter = c
                
        def nCr(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res > 10**6:
                    return 10**6 + 1
            return res

        def count_arrangements(counts: list[int]) -> int:
            total = sum(counts)
            ways = 1
            for freq in counts:
                if freq > 0:
                    ways *= nCr(total, freq)
                    total -= freq
                    if ways > 10**6:
                        return 10**6 + 1
            return ways

        total_permutations = count_arrangements(half_count)
        if k > total_permutations:
            return ""

        half_len = sum(half_count)
        left_half = []

        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                
                half_count[i] -= 1
                arrangements = count_arrangements(half_count)
                
                if arrangements >= k:
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1

        left_str = "".join(left_half)
        return left_str + mid_letter + left_str[::-1]