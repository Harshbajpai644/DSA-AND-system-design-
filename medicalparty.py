import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t_idx = 0
    t = int(input_data[t_idx])
    t_idx += 1
    
    results = []
    
    for _ in range(t):
        x_prime = input_data[t_idx]
        y_prime = input_data[t_idx + 1]
        t_idx += 2
        
        n = len(x_prime)
        
        
        dp = [0, float('inf')]
        
        for i in range(n):
            new_dp = [float('inf'), float('inf')]
            xi_orig = int(x_prime[i])
            yi_orig = int(y_prime[i])
            
            
            for prev_p in range(2):
                if dp[prev_p] == float('inf'):
                    continue
                
                for curr_p in range(2):
                    req_xi = curr_p ^ prev_p
                    
                    flips = (1 if xi_orig != req_xi else 0) + \
                            (1 if yi_orig != curr_p else 0)
                    
                    if dp[prev_p] + flips < new_dp[curr_p]:
                        new_dp[curr_p] = dp[prev_p] + flips
            dp = new_dp
            
        results.append(str(min(dp)))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()