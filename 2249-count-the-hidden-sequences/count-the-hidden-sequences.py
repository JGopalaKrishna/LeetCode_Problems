class Solution:
    def numberOfArrays(self, a: List[int], l: int, u: int) -> int:
        return max((u-l)-(max(accumulate([0]+a))-min(accumulate([0]+a)))+1,0)