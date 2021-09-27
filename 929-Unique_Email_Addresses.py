class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for add in emails:
            local, domain = add.split("@")
            new_local = ""
            for c in local:
                if c == ".": continue
                elif c == "+": break
                else: new_local += c
            res.add(new_local + "@" + domain)
        return len(res)
