class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s[0]
        res = s[0]
        maxlen = 0
        currstr = ''
        for i in range(len(s)):
            currstr += s[i]
            if i == len(s) - 1:
                if len(currstr) > maxlen:
                    return currstr
            elif s[i+1] == s[i]:
                continue
            else:
                j = 1
                while(i + j < len(s) and i + 1 - len(currstr) - j >= 0):
                    # print(s[i + j] != s[i + 1 - len(currstr) - j])
                    if s[i + j] != s[i + 1 - len(currstr) - j]:
                        break
                    j += 1
                j -= 1
                if 2 * j + len(currstr) > maxlen:
                    res = s[i + 1 - len(currstr) - j: i + j + 1]
                    maxlen = 2 * j + len(currstr)
                currstr = ''
        
        return res
        
                
                
            
            
            
        