import sys

def solve():
    name = sys.stdin.readline().strip()
    if not name:
        return
    
    distinct_chars = set(name)
    
    if len(distinct_chars) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == "__main__":
    solve()