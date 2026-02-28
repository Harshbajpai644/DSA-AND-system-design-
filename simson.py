import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        blogs = []
        for i in range(n):
            l = int(input_data[idx])
            idx += 1
            temp = []
            for j in range(l):
                temp.append(int(input_data[idx]))
                idx += 1
            
            unique_in_blog = []
            seen = set()
            for j in range(l - 1, -1, -1):
                if temp[j] not in seen:
                    unique_in_blog.append(temp[j])
                    seen.add(temp[j])
            blogs.append(unique_in_blog)

        used = [False] * n
        final_q = []
        global_seen = set()

        for _ in range(n):
            best_blog = -1
            best_suffix = None

            for i in range(n):
                if used[i]:
                    continue

                current_suffix = []
                for user in blogs[i]:
                    if user not in global_seen:
                        current_suffix.append(user)

                if best_blog == -1 or current_suffix < best_suffix:
                    best_blog = i
                    best_suffix = current_suffix

            used[best_blog] = True
            for user in best_suffix:
                final_q.append(user)
                global_seen.add(user)

        results.append(" ".join(map(str, final_q)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()