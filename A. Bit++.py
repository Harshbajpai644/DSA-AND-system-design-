n = int(input())
x = 0
 
for _ in range(n):
    statement = input()
    # If '+' is in the statement, it's an increment
    if '+' in statement:
        x += 1
    else:
        x -= 1
 
print(x)
