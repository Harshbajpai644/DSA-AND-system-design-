import sys

def solve():
    n_str = sys.stdin.readline().strip()
    if not n_str:
        return
    n = int(n_str)
    t = list(map(int, sys.stdin.readline().split()))
    
    if n == 1:
        print("1 0")
        return

    left, right = 0, n - 1
    sum_alice, sum_bob = 0, 0
    alice_count, bob_count = 0, 0
    
    while left <= right:
        if sum_alice <= sum_bob:
            sum_alice += t[left]
            alice_count += 1
            left += 1
        else:
            sum_bob += t[right]
            bob_count += 1
            right -= 1
            
    print(f"{alice_count} {bob_count}")

if __name__ == "__main__":
    solve()
