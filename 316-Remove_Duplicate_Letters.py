import string

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        p = {}
        for letter in string.ascii_lowercase:
            p[letter] = None
            
        for i,letter in enumerate(s):
            if p[letter]:
                p[letter].append(i)
            else:
                p[letter] = [i]
        
        p = {k:p[k] for k in p if p[k] is not None}
        res = ''
        #print(p)
        while len(p) > 0:
            M = min([p[letter][-1] for letter in p])
            for letter in p:
                if p[letter][0] <= M:
                    m = p[letter][0]
                    break
                    
            res = res + letter
            del p[letter]
            
            for letter in p:
                I = next((i for i, x in enumerate(p[letter]) if x > m), None)
                #p[letter] = [val for val in p[letter] if val > m]
                p[letter] = p[letter][I:]

            #print(p)
        
        #print(res)
        return res
        
                
                
                