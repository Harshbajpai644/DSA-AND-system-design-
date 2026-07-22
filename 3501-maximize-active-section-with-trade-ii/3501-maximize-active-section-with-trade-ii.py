import math

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        
       
        zero_blocks = []
        zero_block_idx = [-1] * n
        
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                length = i - start
                block_id = len(zero_blocks)
                zero_blocks.append((start, length))
                for k in range(start, i):
                    zero_block_idx[k] = block_id
            else:
                i += 1
        
        num_blocks = len(zero_blocks)
        if num_blocks == 0:
            return [total_ones] * len(queries)
        
        merged_lengths = []
        for b in range(num_blocks - 1):
            merged_lengths.append(zero_blocks[b][1] + zero_blocks[b + 1][1])
        
        m = len(merged_lengths)
        if m > 0:
            LOG = m.bit_length()
            st = [[0] * m for _ in range(LOG)]
            st[0] = list(merged_lengths)
            
            for j in range(1, LOG):
                length = 1 << (j - 1)
                for k in range(m - (1 << j) + 1):
                    st[j][k] = max(st[j - 1][k], st[j - 1][k + length])
            
            def query_st(L: int, R: int) -> int:
                if L > R:
                    return 0
                j = (R - L + 1).bit_length() - 1
                return max(st[j][L], st[j][R - (1 << j) + 1])
        else:
            def query_st(L: int, R: int) -> int:
                return 0

        ans = []
        
        for l, r in queries:
            if zero_block_idx[l] != -1:
                b_start = zero_block_idx[l]
                start_len = zero_blocks[b_start][0] + zero_blocks[b_start][1] - l
            else:
                b_start = -1
                for idx in range(l, r + 1):
                    if zero_block_idx[idx] != -1:
                        b_start = zero_block_idx[idx]
                        break
                if b_start != -1:
                    start_len = zero_blocks[b_start][1]
                else:
                    start_len = 0
            
            if zero_block_idx[r] != -1:
                b_end = zero_block_idx[r]
                end_len = r - zero_blocks[b_end][0] + 1
            else:
                b_end = -1
                for idx in range(r, l - 1, -1):
                    if zero_block_idx[idx] != -1:
                        b_end = zero_block_idx[idx]
                        break
                if b_end != -1:
                    end_len = zero_blocks[b_end][1]
                else:
                    end_len = 0
            
            if b_start == -1 or b_end == -1 or b_start > b_end:
                ans.append(total_ones)
                continue
            
            max_gain = 0
            
            if b_start + 1 == b_end:
                max_gain = max(max_gain, start_len + end_len)
            
            
            if b_start + 1 <= b_end - 1:
                max_gain = max(max_gain, query_st(b_start + 1, b_end - 2))
                

                max_gain = max(max_gain, start_len + zero_blocks[b_start + 1][1])
                max_gain = max(max_gain, zero_blocks[b_end - 1][1] + end_len)
            
            ans.append(total_ones + max_gain)
            
        return ans