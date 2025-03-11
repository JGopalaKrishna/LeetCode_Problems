class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x=0
        for i in range(n):
            x^=start
            start+=2
        return x