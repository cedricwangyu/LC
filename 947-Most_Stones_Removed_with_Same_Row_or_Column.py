class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_dic = {}
        for r, c in stones:
            if r not in row_dic:
                row_dic[r] = {c}
            else:
                row_dic[r].add(c)
        res = []
        for r in row_dic:
            cols = row_dic[r]
            ids = []
            for i, s in enumerate(res):
                if len(cols.intersection(s)) > 0:
                    ids.append(i)
            for i in ids[::-1]:
                cols = cols.union(res.pop(i))
            res.append(cols)
        return len(stones) - len(res)
        
                
        
        
        
        