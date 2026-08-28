from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        
        # Step 1: Count character frequencies and check parity
        counts = Counter(s)
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 == 1]
        
        # Palindromes can have at most one odd-frequency character
        if len(odd_chars) > 1:
            return ""
        if n % 2 == 1 and len(odd_chars) != 1:
            return ""
        if n % 2 == 0 and len(odd_chars) != 0:
            return ""
            
        mid = odd_chars[0] if n % 2 == 1 else ""
        
        # Pool of characters available to build the first half
        half_counts = {ch: cnt // 2 for ch, cnt in counts.items() if cnt // 2 > 0}
        
        # --- Candidate 1: First half matches target[:m] exactly ---
        p_equal = ""
        can_match_all = True
        temp_counts = half_counts.copy()
        
        for i in range(m):
            t_ch = target[i]
            if temp_counts.get(t_ch, 0) > 0:
                temp_counts[t_ch] -= 1
            else:
                can_match_all = False
                break
                
        if can_match_all:
            h_equal = target[:m]
            p_cand = h_equal + mid + h_equal[::-1]
            if p_cand > target:
                p_equal = p_cand

        # --- Candidate 2: First half is strictly greater than target[:m] ---
        # Track how far we can successfully match target's characters
        matched_len = 0
        temp_counts = half_counts.copy()
        for i in range(m):
            t_ch = target[i]
            if temp_counts.get(t_ch, 0) > 0:
                temp_counts[t_ch] -= 1
                matched_len += 1
            else:
                break
                
        p_greater = ""
        start_i = min(matched_len, m - 1)
        
        # Prepare the frequency pool up to the maximum match index
        temp_counts = half_counts.copy()
        for i in range(start_i):
            temp_counts[target[i]] -= 1
            
        # Scan backward from right to left to find the first valid divergence index
        for i in range(start_i, -1, -1):
            t_ch = target[i]
            best_c = None
            
            # Find the smallest available character strictly greater than target[i]
            for c in sorted(temp_counts.keys()):
                if temp_counts[c] > 0 and c > t_ch:
                    best_c = c
                    break
                    
            if best_c is not None:
                # Construct the diverging prefix
                h_chars = list(target[:i]) + [best_c]
                temp_counts[best_c] -= 1
                
                # Append the rest of the available characters in ascending sorted order
                rem_chars = []
                for c in sorted(temp_counts.keys()):
                    rem_chars.extend([c] * temp_counts[c])
                    
                h_greater = "".join(h_chars) + "".join(rem_chars)
                p_greater = h_greater + mid + h_greater[::-1]
                break
                
            