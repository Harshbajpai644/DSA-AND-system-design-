import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    results = []
    
    for _ in range(t):
        nums = []
        for i in range(7):
            nums.append(int(input_data[pointer]))
            pointer += 1
        
        total_sum = sum(nums)
        max_val = max(nums)
        
        # Result = max_val - (total_sum - max_val)
        ans = 2 * max_val - total_sum
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
