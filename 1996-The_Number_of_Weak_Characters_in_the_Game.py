class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        curr, res = 0, 0
        for atta, defe in properties:
            if defe >= curr:
                curr, res = defe, res+1
        return len(properties)-res
            
        
        
                