class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n < 100:
                return 0
            
            s = str(n)
            L = len(s)
            
            memo = {}
            
            def dp(pos, tight, last, second_last, is_less_than_3):
                state = (pos, tight, last, second_last, is_less_than_3)
                if state in memo:
                    return memo[state]
                
                if pos == L:
                    return (0, 1)
                
                limit = int(s[pos]) if tight else 9
                total_waviness = 0
                total_count = 0
                
                for digit in range(limit + 1):
                    new_tight = tight and (digit == limit)
                    
                    if is_less_than_3:
                        if last == -1 and digit == 0:
                            w_sub, c_sub = dp(pos + 1, new_tight, -1, -1, True)
                        elif last == -1:
                            w_sub, c_sub = dp(pos + 1, new_tight, digit, -1, True)
                        else:
                            w_sub, c_sub = dp(pos + 1, new_tight, digit, last, False)
                    else:
                        is_peak = last > second_last and last > digit
                        is_valley = last < second_last and last < digit
                        wave_contribution = 1 if (is_peak or is_valley) else 0
                        
                        w_sub, c_sub = dp(pos + 1, new_tight, digit, last, False)
                        total_waviness += wave_contribution * c_sub
                        
                    total_waviness += w_sub
                    total_count += c_sub
                    
                memo[state] = (total_waviness, total_count)
                return memo[state]
            
            return dp(0, True, -1, -1, True)[0]
            
        return solve(num2) - solve(num1 - 1)
