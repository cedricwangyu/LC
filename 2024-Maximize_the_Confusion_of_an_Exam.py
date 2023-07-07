class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left_T, curr_T, left_F, curr_F, res = 0, int(answerKey[0] == 'T'), 0, int(answerKey[0] == 'F'), k
        for i in range(1, len(answerKey)):
            ans = answerKey[i]
            if ans == 'T':
                curr_T += 1
            else:
                curr_F += 1
            if curr_T > k:
                while answerKey[left_T] == 'F':
                    left_T += 1
                curr_T -= 1
                left_T += 1
            elif curr_F > k:
                while answerKey[left_F] == 'T':
                    left_F += 1
                curr_F -= 1
                left_F += 1
            res = max(res, i - left_T + 1, i - left_F + 1)
        return res

        