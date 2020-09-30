def matchs(stamp, target, i, j, ans, pos):
        S = len(stamp)
        T = len(target)
        if (target[i] != stamp[j]) or (T - i < S - j) or (j > i):
            return False
            
        res = ['?'] * T 
        res[i - j : i - j + S] = list(stamp)
        for poss in range(pos, len(ans)):
            if ans[poss] in range(i - j - S + 1, i):
                res[ans[poss]: min(ans[poss] + S, T)] = list(stamp[:min(S, T - ans[poss])])
        
        res = "".join(res)
        if (res[i - j : i] == target[i - j : i]):
            return True
        else:
            return False
        
class Solution:            
    def movesToStamp(self, stamp: str, target: str):
        S = len(stamp)
        T = len(target)
        j = 0
        pos = -1
        ans = []
        for i in range(T):
            j = j % S
            if(target[i] == stamp[j]):
                if(j == 0):
                    reached = False
                    for j in range(S-1, 0, -1):
                        if matchs(stamp, target, i, j, ans, pos):
                            reached = True
                            ans.insert(pos, i - j)
                            break
                    if not reached:
                        if matchs(stamp, target, i, 0, ans, pos + 1):
                            j = 0
                            pos += 1
                            ans.insert(pos, i)
                        else:
                            return []
            else:
                reached = False
                if (j == 0):
                    for j in range(S-1, 0, -1):
                        if matchs(stamp, target, i, j, ans, pos):
                            reached = True
                            ans.insert(pos, i - j)
                            break
                else:
                    for j in range(S):
                        if matchs(stamp, target, i, j, ans, pos + 1):
                            reached = True
                            pos += 1
                            ans.insert(pos, i - j)
                            break
                if not reached:
                    return []
            j += 1
        return ans

                
                        
    
        
        vdef matchs(stamp, target, i, j, ans, pos):
        S = len(stamp)
        T = len(target)
        if (target[i] != stamp[j]) or (T - i < S - j) or (j > i):
            return False
            
        res = ['?'] * T 
        res[i - j : i - j + S] = list(stamp)
        for poss in range(pos, len(ans)):
            if ans[poss] in range(i - j - S + 1, i):
                res[ans[poss]: min(ans[poss] + S, T)] = list(stamp[:min(S, T - ans[poss])])
        
        res = "".join(res)
        if (res[i - j : i] == target[i - j : i]):
            return True
        else:
            return False
        
class Solution:            
    def movesToStamp(self, stamp: str, target: str):
        S = len(stamp)
        T = len(target)
        j = 0
        pos = -1
        ans = []
        for i in range(T):
            j = j % S
            if(target[i] == stamp[j]):
                if(j == 0):
                    reached = False
                    for j in range(S-1, 0, -1):
                        if matchs(stamp, target, i, j, ans, pos):
                            reached = True
                            ans.insert(pos, i - j)
                            break
                    if not reached:
                        if matchs(stamp, target, i, 0, ans, pos + 1):
                            j = 0
                            pos += 1
                            ans.insert(pos, i)
                        else:
                            return []
            else:
                reached = False
                if (j == 0):
                    for j in range(S-1, 0, -1):
                        if matchs(stamp, target, i, j, ans, pos):
                            reached = True
                            ans.insert(pos, i - j)
                            break
                else:
                    for j in range(S):
                        if matchs(stamp, target, i, j, ans, pos + 1):
                            reached = True
                            pos += 1
                            ans.insert(pos, i - j)
                            break
                if not reached:
                    return []
            j += 1
        return ans

                
                        
    
        
        