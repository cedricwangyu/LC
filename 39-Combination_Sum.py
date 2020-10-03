class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        T = [None] * (target + 1)
        #print(T)
        for x in range(1, target + 1):
            for c in candidates:
                #print(x,c)
                if(x < c):
                    continue
                elif (x == c):
                    if T[x] == None:
                        T[x] = [[c]]
                    else:
                        T[x].append([c])
                else:
                    if T[x - c] == None:
                        continue
                    else:
                        if T[x] == None:
                            T[x] = [item + [c] for item in T[x - c]]
                        else:
                            T[x] += [item + [c] for item in T[x - c]]
                            
                #print(T)
        res = []
        if T[target] == None:
            return []
        
        for item in T[target]:
            item.sort()
            if item not in res:
                res.append(item)
            
        return res