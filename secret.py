import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t_cases = int(next(it))
    
    for _ in range(t_cases):
        n = int(next(it))
        k = int(next(it))
        
        strips = [next(it) for _ in range(k)]
        
        char_sets = []
        for j in range(n):
            current_set = 0
            for row in range(k):
                char_val = ord(strips[row][j]) - ord('a')
                current_set |= (1 << char_val)
            char_sets.append(current_set)
            
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i*i != n:
                    divisors.append(n // i)
        divisors.sort()
        
        for d in divisors:
            t_unit = [0] * d
            possible = True
            
            for i in range(d):
                intersection = (1 << 26) - 1
                for j in range(i, n, d):
                    intersection &= char_sets[j]
                
                if intersection == 0:
                    possible = False
                    break
                else:
                    for bit in range(26):
                        if (intersection >> bit) & 1:
                            t_unit[i] = chr(ord('a') + bit)
                            break
            
            if possible:
                res = "".join(t_unit) * (n // d)
                sys.stdout.write(res + "\n")
                break

if __name__ == "__main__":
    solve()