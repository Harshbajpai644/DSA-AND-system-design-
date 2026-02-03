import sys

grid = ""
for line in sys.stdin:
    grid += line.strip()

is_symmetric = True
for i in range(4):
    if grid[i] != grid[8 - i]:
        is_symmetric = False
        break

if is_symmetric:
    print("YES")
else:
    print("NO")