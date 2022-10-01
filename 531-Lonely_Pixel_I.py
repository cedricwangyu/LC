class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_c, col_c = [0] * len(picture), [0] * len(picture[0])
        row_col, col_row = {}, {}
        for i, row in enumerate(picture):
            for j, col in enumerate(row):
                if col == "B":
                    if row_c[i] == 0 and col_c[j] == 0:
                        row_col[i], col_row[j] = j, i
                    else:
                        if i in row_col:
                            del col_row[row_col[i]]
                            del row_col[i]
                        if j in col_row:
                            del row_col[col_row[j]]
                            del col_row[j]
                        
                    row_c[i] += 1
                    col_c[j] += 1
        return len(row_col)
                
                    
            