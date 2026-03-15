class Fancy:

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        self.seq.append(((val - self.add) * pow(self.mul, self.MOD - 2, self.MOD)) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.MOD
        self.mul = (self.mul * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.MOD