class Solution(object):
    def threeSumMulti(self, A, target):
        count = collections.Counter(A)
        keys, res = sorted(count), 0
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T: j += 1
                elif y + z > T: k -= 1
                else:
                    if i < j < k: res += count[x] * count[y] * count[z]
                    elif i == j < k: res += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k: res += count[x] * count[y] * (count[y] - 1) // 2
                    else: res += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    j, k = j + 1, k - 1
        return res % (10**9 + 7)