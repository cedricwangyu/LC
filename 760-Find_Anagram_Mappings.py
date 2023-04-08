class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        request, seen, res = {}, {}, [0] * len(nums1)
        for i, (n1, n2) in enumerate(zip(nums1, nums2)):
            if n1 == n2:
                res[i] = i
                continue
            if n1 in seen:
                res[i] = seen[n1].pop()
                if len(seen[n1]) == 0:
                    del seen[n1]
            elif n1 in request:
                request[n1].append(i)
            else:
                request[n1] = [i]
                
            if n2 in request:
                res[request[n2].pop()] = i
                if len(request[n2]) == 0:
                    del request[n2]
            elif n2 in seen:
                seen[n2].append(i)
            else:
                seen[n2] = [i]
        return res