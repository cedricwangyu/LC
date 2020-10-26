class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if logs == []:
            return logs
        logs.sort(key = lambda k: k.split(" ")[1].isdigit())
        for i in range(len(logs)):
            if logs[i].split(" ")[1].isdigit():
                break
        logs[:i] = sorted(logs[:i], key = lambda k: [k.split(" ", 1)[1], k.split(" ", 1)[0]])
        return logs
        
        
        