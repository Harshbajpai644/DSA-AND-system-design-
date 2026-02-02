import sys

def solve():
    line = sys.stdin.read().split()
    if not line:
        return
    
    scores = [int(x) for x in line]
    
    max_score = max(scores)
    min_score = min(scores)
    
    if max_score - min_score >= 10:
        print("check again")
    else:
        scores.sort()
        median = scores[1]
        print(f"final {median}")

if __name__ == "__main__":
    solve()