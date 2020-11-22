import string
class Solution:
    def __init__(self):
        self.table = dict(zip(list(string.ascii_lowercase), [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        p = {''.join([self.table[c] for c in word]) for word in words}
        return len(p)
        
        