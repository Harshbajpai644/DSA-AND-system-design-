class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for char in ['a', 'b', 'c']:
            curr_run = 0
            for c in s:
                if c == char:
                    curr_run += 1
                    max_len = max(max_len, curr_run)
                else:
                    curr_run = 0

        for char1, char2, forbidden in [('a', 'b', 'c'), ('b', 'c', 'a'), ('a', 'c', 'b')]:
            diff_map = {0: -1}
            diff = 0
            start = 0
            for i, c in enumerate(s):
                if c == forbidden:
                    diff_map = {0: i}
                    diff = 0
                    start = i + 1
                else:
                    if c == char1:
                        diff += 1
                    else:
                        diff -= 1
                    
                    if diff in diff_map:
                        max_len = max(max_len, i - diff_map[diff])
                    else:
                        diff_map[diff] = i

        three_map = {(0, 0): -1}
        ca, cb, cc = 0, 0, 0
        for i, c in enumerate(s):
            if c == 'a': ca += 1
            elif c == 'b': cb += 1
            else: cc += 1
            
            key = (cb - ca, cc - ca)
            if key in three_map:
                max_len = max(max_len, i - three_map[key])
            else:
                three_map[key] = i
                
        return max_len