class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for row in boxGrid:
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    empty_pos = j - 1
                elif row[j] == '#':
                    row[j], row[empty_pos] = row[empty_pos], row[j]
                    empty_pos -= 1

        res = []
        for j in range(n):
            new_row = []
            for i in range(m - 1, -1, -1):
                new_row.append(boxGrid[i][j])
            res.append(new_row)
            
        return res
