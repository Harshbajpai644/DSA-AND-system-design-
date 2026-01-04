import sys, random
MOD = 10**9 + 7

class Node:
    __slots__ = ("v","p","l","r","sz","s")
    def __init__(self,v):
        self.v=v
        self.p=random.random()
        self.l=None
        self.r=None
        self.sz=1
        self.s=v

def sz(t): return t.sz if t else 0
def s(t): return t.s if t else 0

def pull(t):
    if not t: return
    t.sz = 1 + sz(t.l) + sz(t.r)
    t.s = t.v + s(t.l) + s(t.r)

def split(t,k):
    if not t: return None,None
    if sz(t.l) >= k:
        a,b = split(t.l,k)
        t.l = b
        pull(t)
        return a,t
    else:
        a,b = split(t.r,k - sz(t.l) - 1)
        t.r = a
        pull(t)
        return t,b

def merge(a,b):
    if not a or not b: return a or b
    if a.p > b.p:
        a.r = merge(a.r,b)
        pull(a)
        return a
    else:
        b.l = merge(a,b.l)
        pull(b)
        return b

def solve():
    data = sys.stdin
    t = int(data.readline())
    for _ in range(t):
        q = int(data.readline())
        root = None
        L = 0
        sumA = 0
        S = 0
        for _ in range(q):
            cmd = data.readline().split()
            if cmd[0] == "2":
                x = int(cmd[1])
                newL = 2*L + 1
                S = (2*S + sumA + x*(newL*(newL+1)//2)) % MOD
                sumA = (2*sumA + x*(L+1)) % MOD
                root = merge(merge(Node(x), root), Node(x))
                L = newL
            elif cmd[0] == "1":
                mid = (L-1)//2
                a,b = split(root, mid)
                m,c = split(b, 1)
                S = (S - m.v*(mid+1) - s(c)) % MOD
                sumA = (sumA - m.v) % MOD
                root = merge(a, c)
                L -= 1
            else:
                if L == 1:
                    print(root.v % MOD)
                else:
                    print(S * pow(2, L-2, MOD) % MOD)

if __name__ == "__main__":
    solve()
