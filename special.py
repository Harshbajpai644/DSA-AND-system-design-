class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                inner_content = s[i + 1:j]
                processed_inner = self.makeLargestSpecial(inner_content)
                res.append("1" + processed_inner + "0")
                i = j + 1
        
        res.sort(reverse=True)
        return "".join(res)