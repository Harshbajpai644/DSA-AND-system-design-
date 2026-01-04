import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    def simulate(white_first):
        white = a
        dark = b
        size = 1
        layers = 0
        use_white = white_first

        while True:
            if use_white:
                if white < size:
                    break
                white -= size
            else:
                if dark < size:
                    break
                dark -= size

            layers += 1
            size *= 2
            use_white = not use_white

        return layers

    ans = max(simulate(True), simulate(False))
    print(ans)
