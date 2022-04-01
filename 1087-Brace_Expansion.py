class Solution:
    def expand(self, s: str) -> List[str]:
        ans = [""]
        for z in s.replace("{", " ").replace("}", " ").split():
            ans = [x + y for x in ans for y in sorted(z.split(","))]
                
        return ans