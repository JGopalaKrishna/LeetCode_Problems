import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        l=[math.sqrt(i*i+j*j) for i,j in dimensions]
        max_val=max(l)
        indices = [i for i, val in enumerate(l) if val == max_val]
        r=[dimensions[i][0]*dimensions[i][1] for i in indices]
        return max(r)