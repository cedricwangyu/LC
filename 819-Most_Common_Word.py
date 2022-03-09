class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words, curr, banned, res_time, res = defaultdict(int), "", set(banned), 0, ""
        for c in paragraph + " ":
            if c.isalpha():
                curr += c
            elif len(curr) > 0:
                curr = curr.lower()
                if curr not in banned: 
                    words[curr] += 1
                    if words[curr] > res_time:
                        res_time, res = words[curr], curr
                curr = ""
        return res
        
        