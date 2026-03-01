import sys

def solve():
    # Read n and the dishes array
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        line2 = sys.stdin.readline()
        if not line2: return
        a = list(map(int, line2.split()))
    except ValueError:
        return

    winners = set()

    # Simulate the game starting with each player i (0-indexed)
    for start_player in range(n):
        current_dishes = list(a)
        total_dishes = sum(current_dishes)
        current_turn = start_player
        last_winner = -1

        while total_dishes > 0:
            if current_dishes[current_turn] > 0:
                current_dishes[current_turn] -= 1
                total_dishes -= 1
                last_winner = current_turn + 1 # Convert back to 1-indexed
            
            # Move to the next player in the circle
            current_turn = (current_turn + 1) % n
        
        winners.add(last_winner)

    print(len(winners))

# Read number of test cases
line = sys.stdin.readline()
if line:
    t = int(line.strip())
    for _ in range(t):
        solve()