# class FreqStack:

#     def __init__(self):
#         self.i = 0
#         self.p = {}
#         self.freq_rank = []
#     def moveright(self, x):
#         if self.p[x][1] < len(self.freq_rank) - 1:
#             if len(self.p[x][0]) < len(self.p[self.freq_rank[self.p[x][1] + 1]][0]): return True
#             elif len(self.p[x][0]) == len(self.p[self.freq_rank[self.p[x][1] + 1]][0]):
#                 if self.p[x][0][-1] < self.p[self.freq_rank[self.p[x][1] + 1]][0][-1]: return True
#         return False
#     def moveleft(self, x):
#         if self.p[x][1] > 0:
#             if len(self.p[x][0]) > len(self.p[self.freq_rank[self.p[x][1] - 1]][0]): return True
#             elif len(self.p[x][0]) == len(self.p[self.freq_rank[self.p[x][1] - 1]][0]):
#                 if self.p[x][0][-1] > self.p[self.freq_rank[self.p[x][1] - 1]][0][-1]: return True
#         return False
#     def push(self, x: int) -> None:
#         # print("push:", x)
#         if x in self.p: 
#             self.p[x][0].append(self.i)
#             self.i += 1
#         else:
#             self.freq_rank.append(x)
#             self.p[x] = [[self.i], len(self.freq_rank) - 1]
#             self.i += 1
#         while self.moveleft(x): 
#             self.freq_rank[self.p[x][1]], self.freq_rank[self.p[x][1] - 1] = self.freq_rank[self.p[x][1] - 1], self.freq_rank[self.p[x][1]]
#             self.p[self.freq_rank[self.p[x][1]]][1] += 1
#             self.p[x][1] -= 1
#         # print(self.p)
#         # print(self.freq_rank)
#         # print("---------------------------------")
#     def pop(self) -> int:
#         x = self.freq_rank[0]
#         # print("pop:", x)
#         self.p[x][0].pop()
#         while self.moveright(x):
#             self.freq_rank[self.p[x][1]], self.freq_rank[self.p[x][1] + 1] = self.freq_rank[self.p[x][1] + 1], self.freq_rank[self.p[x][1]]
#             self.p[self.freq_rank[self.p[x][1]]][1] -= 1
#             self.p[x][1] += 1
#         if len(self.p[x][0]) <= 0:
#             del self.p[x]
#             self.freq_rank.pop()
#         # print(self.p)
#         # print(self.freq_rank)
#         # print("---------------------------------")
#         return x
        
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()