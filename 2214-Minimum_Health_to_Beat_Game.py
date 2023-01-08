class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        s, m = 0, 0
        for d in damage:
            s += d
            m = d if d > m else m
            
        return s - armor + 1 if armor <= m else s - m + 1