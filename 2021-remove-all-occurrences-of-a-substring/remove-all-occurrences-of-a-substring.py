class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l=len(part)
        while part in s:
            ind=s.index(part)
            s=s[:ind]+s[ind+l:]
        return s