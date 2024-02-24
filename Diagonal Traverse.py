class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        direc = 1  # 1 is up , -1 is down
        row, col = 0, 0

        while row < m and col < n:
            # add curr 
            result.append(mat[row][col])

            # next pos ?
            next_row = row - direc
            next_col = col + direc

            # next position is possible ?
            if 0 <= next_row < m and 0 <= next_col < n:
                
                row = next_row
                col = next_col
            else:
                
                if direc == 1:
                    if col == n - 1:
                        row += 1
                    else:
                        col += 1
                else:
                    if row == m - 1:
                        col += 1
                    else:
                        row += 1
                direc = -direc

        return result
