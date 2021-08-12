class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            p[ss].append(s)
        return [p[k] for k in p]
