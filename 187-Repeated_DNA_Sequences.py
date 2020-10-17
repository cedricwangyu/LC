class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        code = s.replace('A','0').replace('C','1').replace('G','2').replace('T','3')
        #print(code)
        nums = [int(code[i:i+10], 4) for i in range(len(code) - 9)]
        #print(nums)
        p = {}
        res = []
        for i, num in enumerate(nums):
            if num in p:
                if p[num] == 1:
                    res.append(s[i:i+10])
                
                p[num] += 1
            else:
                p[num] = 1
        
        #print(res)
        return res