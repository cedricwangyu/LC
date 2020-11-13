class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def isRight(p11, p12, p21, p22):
            vec1 = [p12[0] - p11[0], p12[1] - p11[1]]
            vec2 = [p22[0] - p21[0], p22[1] - p21[1]]
            if vec1 == [0, 0] or vec2 == [0, 0]:
                return False
            inner = vec1[0] * vec2[0] + vec1[1] * vec2[1]
            #print(inner)
            if inner == 0: return True
            else: return False
        
        if isRight(p1, p2, p1, p3):
            p1, p2, p3, p4 = p1, p4, p2, p3
        elif isRight(p1, p2, p1, p4):
            p1, p2, p3, p4 = p1, p3, p2, p4
        elif isRight(p1, p3, p1, p4):
            pass
        else:
            return False
        
        if isRight(p1, p2, p3, p4):
            return True
        else:
            return False
        