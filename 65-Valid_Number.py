class Solution:
    def __init__(self):
        self.p = {0: {'0': 1, 's': 2, 'd': 3},
                 1: {'0': 1, 'd': 4, 'e': 5},
                 2: {'0': 1, 'd': 3},
                 3: {'0': 4},
                 4: {'0': 4, 'e': 5},
                 5: {'0': 7, 's': 6},
                 6: {'0': 7},
                 7: {'0': 7}}
    def isNumber(self, s: str) -> bool:
        cur_state = 0
        for c in s:
            if c.isdigit():
                if '0' in self.p[cur_state]: cur_state = self.p[cur_state]['0']
                else: return False
            elif c == '.':
                if 'd' in self.p[cur_state]: cur_state = self.p[cur_state]['d']
                else: return False
            elif c in ('E', 'e'):
                if 'e' in self.p[cur_state]: cur_state = self.p[cur_state]['e']
                else: return False
            elif c in ('+', '-'):
                if 's' in self.p[cur_state]: cur_state = self.p[cur_state]['s']
                else: return False
            else: return False
        return True if cur_state in (1,4,7) else False