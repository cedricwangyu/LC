class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini = [item[0] for item in arrays]
        maxi = [item[-1] for item in arrays]
        M = max(maxi)
        M_ind = maxi.index(M)
        m = min(mini)
        m_ind = mini.index(m)
        if (m_ind != M_ind):
            return M - m
        else:
            maxi.remove(M)
            MM = max(maxi)
            mini.remove(m)
            mm = min(mini)
            return max(M - mm, MM - m)