import collections
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # def bisect_insert(row):
        #     if row[0] <= mat[0][0]: mat.insert(0, row)
        #     elif row[0] >= mat[-1][0]: mat.append(row)
        #     else:
        #         l, r = 0, len(mat) - 1
        #         while r - l > 1:
        #             m = (l + r) // 2
        #             if mat[m][0] == row[0]: 
        #                 mat.insert(m, row)
        #                 return
        #             elif mat[m][0] < row[0]: l = m
        #             else: r = m
        #         mat.insert(r, row)
        # mat.sort(key=lambda x: x[0])
        # while(True):
        #     if mat[0][0] == mat[-1][0]: return mat[0][0]
        #     row = mat.pop(0)
        #     row.pop(0)
        #     if len(row) <= 0: return -1
        #     bisect_insert(row)
        p = Counter([j for i in mat for j in i])
        try: return min(i for i in p if p[i] == len(mat))
        except: return -1    