class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        if len(s2) > len(s1): return ""
        if len(s2) == 1:
            return s2 if s2 in set(s1) else ""
        n = len(s2)
        profile = [] # start_id, curr_num
        manager = defaultdict(list) # key = letters looking for, val = idx in profile
        curr, curr_idx = len(s1)+1, (-1, -1)
        for i, c in enumerate(s1):
            if c in manager:
                indices = manager[c].copy()
                manager[c].clear()
                for idx in indices:
                    profile[idx][1] += 1
                    if i - profile[idx][0] + 1 < curr:
                        if profile[idx][1] >= n:
                            curr, curr_idx = i - profile[idx][0] + 1, (profile[idx][0], i)
                        else:
                            manager[s2[profile[idx][1]]].append(idx)
            if c == s2[0]:
                profile.append([i, 1])
                manager[s2[1]].append(len(profile)-1)
        
        return s1[curr_idx[0]:curr_idx[1]+1] if curr_idx[0] >= 0 else ""




            

            
