class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if len(tokens) < 1:
            return 0
        tokens.sort()
        score = 0
        while(len(tokens) > 0):
            #print('tokens: {}, power: {}, score: {}'.format(tokens, P, score))
            if P >= tokens[0]:
                score += 1
                P -= tokens[0]
                tokens.pop(0)
            else:
                if len(tokens) >= 2 and score > 0 and tokens[0] <= tokens[-1] + P:
                    P = P + tokens[-1] - tokens[0]
                    tokens.pop(0)
                    tokens.pop(-1)
                else:
                    break
        
        print(score)
        return score