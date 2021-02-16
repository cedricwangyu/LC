class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        p = {}
        for i in range(len(pid)):
            if ppid[i] in p: p[ppid[i]].append(pid[i])
            else: p[ppid[i]] = [pid[i]]
        res = []
        def helper(root):
            res.append(root)
            if root not in p: return
            for node in p[root]: helper(node)
        helper(kill)
        return res
                
        
        