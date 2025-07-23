class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        for q,t in sorted(((x,'ab'),(y,'ba')))[::-1]:
            while t in s: res += q*(len(s)-len(s:=re.sub(t,'',s)))

        return res//2